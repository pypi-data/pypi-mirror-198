import enum
import time
from kabaret import flow
from kabaret.flow_entities.entities import Entity, Property

from ..utils.kabaret.flow_entities.entities import EntityView

from .file import FileSystemMap, TrackedFile, FileSystemRefs
from .maputils import SimpleCreateAction
from .task_manager import CreateTaskDefaultFiles, ManageTasksAction, FileTypeValue
from .users import ToggleBookmarkAction


class IconSize(enum.Enum):

    SMALL  = 0
    MEDIUM = 1
    LARGE  = 2


class Task(Entity):
    """
    Defines an arbitrary task containing a list of files.

    Instances provide the `task` and `task_display_name` keys
    in their contextual dictionary (`settings` context).
    """
    
    display_name = Property().ui(hidden=True)
    code         = Property().ui(hidden=True)
    enabled      = Property().ui(hidden=True, editor='bool')
    icon_small   = Property().ui(hidden=True)
    icon_medium  = Property().ui(hidden=True)
    icon_large   = Property().ui(hidden=True)

    files = flow.Child(FileSystemMap).ui(
        expanded=True,
        action_submenus=True,
        items_action_submenus=True
    )
    file_refs = flow.Child(FileSystemRefs).ui(
        expanded=True,
        action_submenus=True,
        items_action_submenus=True
    )
    primary_files = Property().ui(hidden=True)
    priority_actions  = Property().ui(hidden=True)

    @classmethod
    def get_source_display(cls, oid):
        split = oid.split('/')
        indices = list(range(len(split) - 1, 2, -2))
        return ' · '.join([split[i] for i in reversed(indices)])
    
    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                task=self.name(),
                task_display_name=self.get_display_name(),
                task_code=self.get_code()
            )
    
    def get_sized_icon(self, size=IconSize.SMALL):
        if size == IconSize.SMALL:
            icon = self.icon_small.get()
        elif size == IconSize.MEDIUM:
            icon = self.icon_medium.get()
        else:
            icon = self.icon_large.get()
        
        return icon and tuple(icon)
    
    def get_display_name(self):
        return self.display_name.get() or self.name()
    
    def get_code(self):
        return self.code.get() or self.name()
    
    def get_primary_files(self):
        '''
        Returns the oids of the primary files of this task as a list.
        '''
        primary_names = [n.replace('.', '_') for n in self.get_primary_file_names() or []]
        mapped_names = self.files.mapped_names()
        primary_files = []
        
        for n in mapped_names:
            if n in primary_names or self.files[n].is_primary_file.get():
                primary_files.append(self.files[n].oid())
        
        return primary_files
    
    def get_primary_file_names(self):
        return self.primary_files.get() or None
    
    def _fill_ui(self, ui):
        ui['custom_page'] = 'libreflow.baseflow.ui.task.TaskPageWidget'


class TaskCollection(EntityView):
    """
    Defines a collection of tasks.
    """

    add_task = flow.Child(SimpleCreateAction)

    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(Task)
    
    def collection_name(self):
        mgr = self.root().project().get_entity_manager()
        return mgr.get_task_collection().collection_name()


# Managed tasks
# -------------------------


class ProjectUserNames(flow.values.SessionValue):

    DEFAULT_EDITOR = 'choice'

    STRICT_CHOICES = False

    _task = flow.Parent(2)

    def choices(self):
        users = set(self.root().project().get_users().mapped_names())
        assigned_users = set(self._task.assigned_users.get())
        
        return list(users - assigned_users)
    
    def revert_to_default(self):
        names = self.choices()
        if names:
            self.set(names[0])


class SubtaskNames(flow.values.SessionValue):

    DEFAULT_EDITOR = 'multichoice'

    STRICT_CHOICES = False

    _action = flow.Parent()
    _task = flow.Parent(2)

    def choices(self):
        tm = self.root().project().get_task_manager()
        return tm.get_subtasks(self._task.name())
    
    def update_assigned_tasks(self):
        assigned_subtasks = self._task.get_assigned_subtasks(
            self._action.user.get()
        )
        self.set(assigned_subtasks)


class EditUserAssignations(flow.Action):

    user     = flow.SessionParam(value_type=ProjectUserNames).watched()
    subtasks = flow.SessionParam(list, value_type=SubtaskNames)

    _task = flow.Parent()

    def needs_dialog(self):
        self.user.revert_to_default()
        self.subtasks.update_assigned_tasks()
        return True
    
    def get_buttons(self):
        return ['Save', 'Close']
    
    def run(self, button):
        if button == 'Close':
            return
        
        assigned = set(self.subtasks.get())
        unassigned = set(self.subtasks.choices()) - assigned

        for st in assigned:
            self._task.assign_users(self.user.get(), subtask_name=st)
        for st in unassigned:
            self._task.unassign_users(self.user.get(), subtask_name=st)
        
        return self.get_result(close=False)
    
    def child_value_changed(self, child_value):
        if child_value is self.user:
            self.subtasks.update_assigned_tasks()


class ManagedTask(Task):
    """
    A ManagedTask provides features handled by the task
    manager of the project.
    """

    assigned_users         = Property().ui(hidden=True)
    subtask_assigned_users = Property().ui(hidden=True)
    current_subtask        = Property().ui(hidden=True)
    color                  = Property().ui(hidden=True)
    
    toggle_bookmark = flow.Child(ToggleBookmarkAction).ui(hidden=True)
    create_dft_files = flow.Child(CreateTaskDefaultFiles).ui(
        label='Create default files'
    )

    edit_assignations = flow.Child(EditUserAssignations)

    def get_display_name(self):
        name = self.display_name.get()
        if not name:
            tm = self.root().project().get_task_manager()
            name = tm.get_task_display_name(self.name())
        
        return name

    def get_icon(self, size=IconSize.MEDIUM):
        icon = self.get_sized_icon(size)
        if not icon:
            tm = self.root().project().get_task_manager()
            icon = tm.get_task_icon(self.name())
        
        return icon
    
    def get_code(self):
        code = self.code.get()
        if not code:
            tm = self.root().project().get_task_manager()
            code = tm.get_task_code(self.name())
        
        return code

    def is_assigned(self, user_name, subtask_name=None):
        assigned_users = self._get_assigned_users(subtask_name)
        assigned = user_name in assigned_users

        if subtask_name is None and not assigned:
            # If not explicitly assigned to the task, check if user is assigned to one of its subtasks
            st_assigned_users = self.subtask_assigned_users.get() or {}
            assigned |= user_name in set().union(*st_assigned_users.values())
        
        return assigned

    def assign_users(self, *user_names, subtask_name=None):
        names = set(self._get_assigned_users(subtask_name))
        names |= set(user_names)
        self._set_assigned_users(list(names), subtask_name)

    def unassign_users(self, *user_names, subtask_name=None):
        names = set(self._get_assigned_users(subtask_name))
        names -= set(user_names)
        self._set_assigned_users(list(names), subtask_name)
    
    def get_assigned_subtasks(self, user_name):
        assigned_users = self.subtask_assigned_users.get() or {}
        return [
            st for st, user_names in assigned_users.items()
            if user_name in user_names
        ]
    
    def get_color(self):
        color = self.color.get()
        if not color:
            tm = self.root().project().get_task_manager()
            color = tm.get_task_color(self.name()) or None
        
        return color
    
    def get_primary_file_names(self):
        names = super(ManagedTask, self).get_primary_file_names()

        if names is None:
            tm = self.root().project().get_task_manager()
            names = tm.get_task_primary_file_names(self.name())
        
        return names
    
    def _get_assigned_users(self, subtask_name=None):
        if subtask_name is None:
            names = self.assigned_users.get() or []
        else:
            assigned_users = self.subtask_assigned_users.get() or {}
            names = assigned_users.get(subtask_name, [])
        
        return names
    
    def _set_assigned_users(self, user_names, subtask_name=None):
        if subtask_name is None:
            self.assigned_users.set(user_names)
        else:
            assigned_users = self.subtask_assigned_users.get() or {}
            assigned_users[subtask_name] = user_names
            self.subtask_assigned_users.set(assigned_users)


class ManagedTaskCollection(TaskCollection):

    manage_tasks = flow.Child(ManageTasksAction).injectable().ui(
        label='Manage tasks'
    )

    @classmethod
    def mapped_type(cls):
        return flow.injection.injectable(ManagedTask)
    
    def mapped_names(self, page_num=0, page_size=None):
        names = super(ManagedTaskCollection, self).mapped_names(
            page_num, page_size
        )
        # Sort tasks by their positions configured in the project's default tasks
        default_tasks = {
            dt.name(): dt
            for dt in self.get_default_tasks()
        }
        names = sorted(
            names,
            key=lambda n: default_tasks[n].position.get()
        )
        return names
    
    def get_default_tasks(self):
        tm = self.root().project().get_task_manager()
        return tm.default_tasks.mapped_items()
    
    def _fill_row_cells(self, row, item):
        mgr = self.root().project().get_task_manager()
        row['Name'] = mgr.get_task_display_name(item.name())

    def _fill_row_style(self, style, item, row):
        mgr = self.root().project().get_task_manager()
        user_name = self.root().project().get_user_name()

        style['icon'] = mgr.get_task_icon(item.name())

        if (
            mgr.is_assignation_enabled(item.name())
            and not item.is_assigned(user_name)
        ):
            color = '#4e5255'
        else:
            color = item.get_color()
        
        style['foreground-color'] = color
