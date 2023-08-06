import os
import re
import datetime
import pprint
import time
import webbrowser
import functools
from kabaret.app.ui.gui.widgets.flow.flow_view import (
    CustomPageWidget,
    QtWidgets,
    QtCore,
    QtGui,
)
from kabaret.app.ui.gui.widgets.flow.flow_field import ObjectActionMenuManager
from kabaret.app.ui.gui.widgets.popup_menu import PopupMenu
from kabaret.app import resources
from kabaret.app.ui.gui.icons import flow as _

from libreflow.baseflow.runners import CHOICES_ICONS

from ...resources.icons import gui as _


class LabelIcon(QtWidgets.QLabel):

    def __init__(self, icon=None):
        QtWidgets.QLabel.__init__(self, '')
        if icon:
            self.setIcon(icon)
    
    def setIcon(self, icon):
        icon = QtGui.QIcon(resources.get_icon(icon))
        pixmap = icon.pixmap(QtCore.QSize(16, 16))
        self.setPixmap(pixmap)
        self.setAlignment(QtCore.Qt.AlignVCenter)


class TaskStatusItem(QtWidgets.QWidget):

    def __init__(self, combobox, text, preset=None):
        super().__init__()
        self.combobox = combobox
        self.text = text
        self.preset = preset
        
        self.presetData = []
        self.checked = False

        self.build()

    def build(self):
        layout = QtWidgets.QHBoxLayout(self)
        layout.setMargin(0)
        layout.setSpacing(0)

        if self.text == '-':
            separator = QtWidgets.QFrame()
            separator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        
            layout.addWidget(separator, QtCore.Qt.AlignVCenter)
            return

        name = QtWidgets.QLabel(self.text)

        self.checkbox = QtWidgets.QToolButton(self)
        self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check-box-empty'))))
        self.checkbox.setFixedSize(20,20)
        self.checkbox.setIconSize(QtCore.QSize(10,10))
        self.checkbox.clicked.connect(self._on_checkbox_clicked)
        
        layout.addWidget(self.checkbox)
        layout.addWidget(name, QtCore.Qt.AlignVCenter)
        layout.addStretch()
    
    def setChecked(self, state, disablePreset=None):
        if state:
            self.checked = True
            self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check'))))
        else:
            self.checked = False
            self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check-box-empty'))))
        
        if self.preset and disablePreset is None:
            self.combobox.setChecked(self.presetData, self.checked, presetMode=True)
        
        if disablePreset is None:
            self.combobox.checkPreset()
        self.combobox.setTopText()
        
    def _on_checkbox_clicked(self):
        if self.checked:
            self.setChecked(False)
        else:
            self.setChecked(True)


class FilterStatusComboBox(QtWidgets.QComboBox):

    def __init__(self, *args):
        super(FilterStatusComboBox, self).__init__(*args)
        self.listw = QtWidgets.QListWidget(self)
        self.setModel(self.listw.model())
        self.setView(self.listw)
        self.activated.connect(self.setTopText)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        # Style
        self.setMinimumWidth(92)
        qss = '''QListView {
                    border: 0px;
                }
                QListView::item:selected {
                    background: transparent;
                }
                QListView::item:hover {
                    background-color: #273541;
                }'''
        self.setStyleSheet(qss)
        self.view().window().setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.view().window().setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

        # Disable right-click
        self.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        # For save user choices
        self.previousData = []

    def addItem(self, text, preset=None):
        item = QtWidgets.QListWidgetItem(self.listw)
        itemWidget = TaskStatusItem(self, text, preset)
        item.setSizeHint(itemWidget.sizeHint())
        self.listw.addItem(item)
        self.listw.setItemWidget(item, itemWidget)
        self.setTopText()
    
    def addItems(self, texts):
        for text in texts:
            exist = False
            for i in range(self.listw.count()):
                item = self.listw.item(i)
                widget = self.listw.itemWidget(item)
                if widget.text == text:
                    exist = True
                    break
            if not exist:
                self.addItem(text)

    def setDefaultPreset(self):
        preset = []
        defaultPresetItem = None
        for i in range(self.listw.count()):
            item = self.listw.item(i)
            widget = self.listw.itemWidget(item)
            if widget.preset and widget.text == 'Default':
                defaultPresetItem = widget
                continue
            if widget.preset or widget.text == 'DONE' or widget.text == '-':
                continue
            preset.append(widget.text)

        defaultPresetItem.presetData = preset
        return preset

    def setChecked(self, texts, state, presetMode=None):
        for i, text in enumerate(texts):
            for i in range(self.listw.count()):
                item = self.listw.item(i)
                widget = self.listw.itemWidget(item)
                if widget.text == text:
                    if state == True:
                        widget.setChecked(True)
                    else:
                        widget.setChecked(False)
                if presetMode:
                    if not widget.preset and widget.text not in texts:
                        if widget.checked:
                            widget.setChecked(False)

    def setTopText(self):
        list_text = self.fetchNames()
        text = ", ".join(list_text)
        
        metrics = QtGui.QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, QtCore.Qt.ElideRight, self.lineEdit().width())
        if '…' in elidedText:
            elidedText = 'Status (' + str(len(list_text)) + ')'
        self.setEditText(elidedText)

    def checkPreset(self):
        currentData = self.fetchNames()
        for i in range(self.listw.count()):
            item = self.listw.item(i)
            widget = self.listw.itemWidget(item)
            if widget.preset:
                if widget.presetData == currentData:
                    widget.setChecked(True, disablePreset=True)
                else:
                    widget.setChecked(False, disablePreset=True)

    def fetchNames(self):
        return [
            self.listw.itemWidget(self.listw.item(i)).text
            for i in range(self.listw.count())
            if self.listw.itemWidget(self.listw.item(i)).preset is None
            if self.listw.itemWidget(self.listw.item(i)).checked
        ]

    def fetchItems(self):
        return [
            self.listw.itemWidget(self.listw.item(i))
            for i in range(self.listw.count())
            if self.listw.itemWidget(self.listw.item(i)).preset is None
            if self.listw.itemWidget(self.listw.item(i)).checked
        ]

    def count(self):
        return len([
            self.listw.itemWidget(self.listw.item(i))
            for i in range(self.listw.count())
            if self.listw.itemWidget(self.listw.item(i)).preset is None
        ])

    # Methods for make combobox less buggy
    def eventFilter(self, object, event):
        if object == self.lineEdit():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                if event.button() == QtCore.Qt.LeftButton:
                    if self.closeOnLineEditClick:
                        self.hidePopup()
                    else:
                        self.showPopup()
                    return True

        if object == self.view().viewport():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.setTopText()
        # Check if there are any changes
        newRes = self.fetchNames()
        if self.previousData != newRes:
            self.previousData = newRes
            self.parent().page_widget.update_presets(filter_data=self.previousData)
            self.parent().page_widget.list.refresh(force_update=True)

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False


class FileUploadItem(QtWidgets.QWidget):
    """A single item in listWidget."""
    removed = QtCore.Signal(QtWidgets.QListWidgetItem)

    def __init__(self, combobox, text, path, listwidgetItem, primary_file):
        super().__init__()
        self.combobox = combobox
        self.text = text
        self.path = path
        self.listwidgetItem = listwidgetItem
        self.primary_file = primary_file
        self.checked = True

        self.build()

    def build(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(5,0,0,0)

        name, ext = os.path.splitext(self.text)
        if ext:
            file_icon = CHOICES_ICONS.get(
                ext[1:], ('icons.gui', 'text-file-1')
            )
        else:
            file_icon = ('icons.gui', 'folder-white-shape')

        label_icon = QtWidgets.QLabel('')
        icon = QtGui.QIcon(resources.get_icon(file_icon))
        pixmap = icon.pixmap(QtCore.QSize(13,13))
        label_icon.setPixmap(pixmap)

        file_name = QtWidgets.QLabel(self.text)

        self.horizontalLayout.addWidget(label_icon)
        self.horizontalLayout.addWidget(file_name)
        self.horizontalLayout.addStretch()

        if self.primary_file:
            self.checked = False
            self.checkbox = QtWidgets.QToolButton(self)
            self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check-box-empty'))))
            self.checkbox.setFixedSize(20,20)
            self.checkbox.setIconSize(QtCore.QSize(10,10))
            self.checkbox.clicked.connect(self._on_checkbox_clicked)
            self.horizontalLayout.addWidget(self.checkbox)
        else:
            self.delete = QtWidgets.QToolButton(self)
            self.delete.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'remove-symbol'))))
            self.delete.setFixedSize(20,20)
            self.delete.setIconSize(QtCore.QSize(10,10))
            self.delete.setToolTip("Delete")
            self.delete.clicked.connect(lambda: self.removed.emit(self.listwidgetItem))
            self.horizontalLayout.addWidget(self.delete)
    
    def setChecked(self, state):
        if state:
            self.checked = True
            self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check'))))
            self.combobox.setTopText()
        else:
            self.checked = False
            self.checkbox.setIcon(QtGui.QIcon(resources.get_icon(('icons.gui', 'check-box-empty'))))
            self.combobox.setTopText()
        
    def _on_checkbox_clicked(self):
        if self.checked:
            self.setChecked(False)
        else:
            self.setChecked(True)


class FilesUploadComboBox(QtWidgets.QComboBox):

    def __init__(self, *args):
        super(FilesUploadComboBox, self).__init__(*args)
        self.listw = QtWidgets.QListWidget(self)
        self.setModel(self.listw.model())
        self.setView(self.listw)
        self.activated.connect(self.setTopText)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

        qss = '''QListView {
                    border: 0px;
                }
                QListView::item:selected {
                    background: transparent;
                }
                QListView::item:hover {
                    background-color: #273541;
                }'''
        self.setStyleSheet(qss)
        self.view().window().setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.view().window().setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setAcceptDrops(True)
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        self.view().viewport().installEventFilter(self)
        self.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.addPrimaryFiles()

    def addItem(self, text, path, primary_file=None):
        item = QtWidgets.QListWidgetItem(self.listw)
        itemWidget = FileUploadItem(self, text, path, item, primary_file)
        itemWidget.removed.connect(self.removeItem)
        item.setSizeHint(itemWidget.sizeHint())
        self.listw.addItem(item)
        self.listw.setItemWidget(item, itemWidget)
        self.setTopText()
    
    def addFiles(self, paths):
        for path in paths:
            exist = False
            for i in range(self.listw.count()):
                item = self.listw.item(i)
                widget = self.listw.itemWidget(item)
                if widget.path == path:
                    exist = True
                    break
            if not exist:
                filename = os.path.split(path)[1]
                self.addItem(filename, path)

    def addPrimaryFiles(self):
        files_list = self.parent().task_item.files_list
        for i in range(files_list.topLevelItemCount()):
            f = files_list.topLevelItem(i)
            check = self.parent().page_widget.is_uploadable(f.file_name)
            if check:
                r = self.parent().page_widget.session.cmds.Flow.call(
                    f.file_oid, 'get_head_revision', ['Available'], {}
                )
                self.addItem(f.file_name, r.get_path(), True)

    def removeItem(self, item):
        view = self.view()
        index = view.indexFromItem(item)
        view.takeItem(index.row())
        self.setTopText()

    def clear(self):
        for i in reversed(range(self.listw.count())):
            item = self.listw.item(i)
            widget = self.listw.itemWidget(item)
            if widget.primary_file:
                widget.setChecked(False)
            else:
                self.removeItem(item)
        self.setTopText()

    def setTopText(self):
        list_text = self.fetchFilesNames()
        text = ", ".join(list_text)
        if not text:
            count = 0
            for i in range(self.listw.count()):
                if self.listw.itemWidget(self.listw.item(i)).primary_file:
                    count = count + 1
            if count > 1:
                return self.setEditText(str(count) + ' Primary files available')
        
        metrics = QtGui.QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, QtCore.Qt.ElideRight, self.lineEdit().width())
        if '…' in elidedText:
            elidedText = str(len(list_text)) + ' Files'
        self.setEditText(elidedText)

    def fetchFilesNames(self):
        return [
            self.listw.itemWidget(self.listw.item(i)).text
            for i in range(self.listw.count())
            if self.listw.itemWidget(self.listw.item(i)).checked
        ]

    def fetchItems(self):
        return [
            self.listw.itemWidget(self.listw.item(i))
            for i in range(self.listw.count())
            if self.listw.itemWidget(self.listw.item(i)).checked
        ]

    def count(self):
        return self.view().count()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.addFiles([url.toLocalFile() for url in event.mimeData().urls()])

    # Methods for make combobox less buggy
    def eventFilter(self, object, event):
        if object == self.lineEdit():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                if event.button() == QtCore.Qt.LeftButton:
                    if self.closeOnLineEditClick:
                        self.hidePopup()
                    else:
                        self.showPopup()
                    return True

        if object == self.view().viewport():
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False


class NavigationSeparator(QtWidgets.QToolButton):

    def __init__(self, related_navigation_button, custom_widget):
        super(NavigationSeparator, self).__init__(related_navigation_button)
        self.related_navigation_button = related_navigation_button
        self.custom_widget = custom_widget

        self.setIcon(resources.get_icon(
            ('icons.flow', 'collapsed'),
            disabled_ref=('icons.flow', 'collapsed')
        ))
    
    def mousePressEvent(self, e):
        self.related_navigation_button._show_navigables_menu(self.custom_widget.task_oid)
        super(NavigationSeparator, self).mousePressEvent(e)

    def sizeHint(self):
        return QtCore.QSize(18, 24)


class NavigationButton(QtWidgets.QToolButton):

    def __init__(self, name, oid, custom_widget):
        super(NavigationButton, self).__init__()
        if ':' in name:
            self.name = name.split(':')[1]
        else:
            self.name = name
        self.oid = oid
        self.custom_widget = custom_widget
        self.page_widget = custom_widget.page_widget
        self._last_click_pos = QtCore.QPoint()

        self.setText(self.name)

        self.clicked.connect(self._goto)

        self._menu = PopupMenu(self)

    def _goto_oid(self, oid):
        self.parent().tasks_list.page_widget.page.goto(oid)

    def _goto(self, b=None):
        self.parent().tasks_list.page_widget.page.goto(self.oid)

    def _show_navigables_menu(self, full_oid):
        self._menu.clear()

        m = self._menu

        m.addAction('Loading...')

        session = self.page_widget.session
        try:
            navigatable_entries = session.cmds.Flow.get_navigable_oids(
                self.oid, full_oid
            )
        except Exception as err:
            m.clear()
            m.addAction('ERROR: ' + str(err))
            raise

        m.clear()
        root = m
        for i, entry in enumerate(navigatable_entries, 1):
            if entry is None:
                m.addMenu()
            else:
                label, oid = entry
                if oid == self.oid:
                    item = m.addItem(
                        '> %s <' % label
                    )
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                else:
                    m.addAction(label, callback=functools.partial(self._goto_oid, oid))

        root.addMenu()
        root.addAction("Copy", icon=resources.get_icon(('icons.gui', 'copy-document')),
                       callback=lambda: QtWidgets.QApplication.clipboard().setText(self.oid))
        root.addAction("Paste", icon=resources.get_icon(('icons.gui', 'paste-from-clipboard')),
                       callback=lambda: self._goto_oid(QtWidgets.QApplication.clipboard().text()))
        m.popup(QtGui.QCursor.pos())

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.RightButton:
            self._show_navigables_menu(self.custom_widget.task_oid)
        else:
            self._last_click_pos = e.pos()
        super(NavigationButton, self).mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self._last_click_pos = QtCore.QPoint()
        super(NavigationButton, self).mouseReleaseEvent(e)


class WarningFrame(QtWidgets.QWidget):

    def __init__(self, custom_widget, text):
        super(WarningFrame, self).__init__()
        self.custom_widget = custom_widget

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.frame = QtWidgets.QFrame()
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet('''
            background-color: palette(base);
            border: 1px solid palette(dark);
            border-radius: 2px;
        ''')

        self.asset = QtWidgets.QWidget()
        asset_lo = QtWidgets.QVBoxLayout()
        icon = QtGui.QIcon(resources.get_icon(('icons.gui', 'exclamation-sign')))
        pixmap = icon.pixmap(QtCore.QSize(128, 128))
        self.icon_lbl = QtWidgets.QLabel('')
        self.icon_lbl.setPixmap(pixmap)
        self.label = QtWidgets.QLabel(text)

        asset_lo.addWidget(self.icon_lbl, 0, QtCore.Qt.AlignCenter)
        asset_lo.addWidget(self.label, 1, QtCore.Qt.AlignCenter)
        self.asset.setLayout(asset_lo)
        
        glo = QtWidgets.QGridLayout()
        glo.setContentsMargins(0,0,0,0)
        glo.addWidget(self.frame, 0, 0, 3, 0)
        glo.addWidget(self.asset, 1, 0, QtCore.Qt.AlignCenter)
        self.setLayout(glo)


# class KitsuUser(QtWidgets.QWidget):

    #     def __init__(self, parent, full_name, color):
    #         super(KitsuUser, self).__init__()
    #         self.parent = parent
    #         self.full_name = full_name
    #         self.color = color

    #         self.build()

    #     def build(self):
    #         lo = QtWidgets.QHBoxLayout()
    #         lo.setMargin(0)

    #         self.user_icon = QtWidgets.QLabel()
    #         pm = resources.get_pixmap('icons.libreflow', 'circular-shape-silhouette')
    #         painter = QtGui.QPainter(pm)
    #         painter.save()
    #         font = QtGui.QFont()
    #         font.setPointSize(12)
    #         font.setWeight(QtGui.QFont.Bold)
    #         painter.setFont(font)
    #         painter.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
    #         painter.fillRect(pm.rect(), QtGui.QColor(self.color))
    #         painter.setPen(QtCore.Qt.white)
    #         painter.drawText(pm.rect(), QtCore.Qt.AlignCenter, ''.join([s[0] for s in self.full_name.split()]))
    #         painter.restore()
    #         self.user_icon.setPixmap(pm.scaled(23, 23, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
    #         self.user_icon.setAlignment(QtCore.Qt.AlignCenter)
            
    #         self.user_name = QtWidgets.QLabel(self.full_name)
    #         self.user_name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

    #         lo.addWidget(self.user_icon)
    #         lo.addWidget(self.user_name)
    #         self.setLayout(lo)


class MyTasksFooter(QtWidgets.QWidget):

    def __init__(self, page_widget):
        super(MyTasksFooter, self).__init__(page_widget)
        self.page_widget = page_widget
        self.build()

    def build(self):
        self.left_text = QtWidgets.QLabel()
        self.left_text.setText(str(self.page_widget.list.get_count())+' Tasks')
        self.page_widget.list.get_count()
        self.shift_label = QtWidgets.QLabel('Press SHIFT to display entity description')

        hlo = QtWidgets.QHBoxLayout()
        hlo.addWidget(self.left_text)
        hlo.addStretch()
        hlo.addWidget(self.shift_label)
        hlo.setContentsMargins(0,10,0,5)
        self.setLayout(hlo)

    def refresh_count(self):
        self.left_text.setText(str(self.page_widget.list.get_count())+' Tasks')
        self.left_text.setStyleSheet('')


class EditStatusDialog(QtWidgets.QDialog):

    def __init__(self, task_item):
        super(EditStatusDialog, self).__init__(task_item)
        self.task_item = task_item
        self.page_widget = task_item.page_widget
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setStyleSheet('font-size: 11px;')
        self.setMaximumSize(600, 300)

        self.build()
    
    def build(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(20,20,20,20)

        palette = self.palette()
        palette.setColor(QtGui.QPalette.Base, palette.color(QtGui.QPalette.Window))
        self.setPalette(palette)

        self.content_layout = QtWidgets.QGridLayout()
        self.content_layout.setAlignment(QtCore.Qt.AlignTop)
      
        self.content_layout.addWidget(LabelIcon(('icons.flow', 'input')), 0, 0, QtCore.Qt.AlignVCenter)
        self.content_layout.addWidget(QtWidgets.QLabel('Target Status'), 0, 1, QtCore.Qt.AlignVCenter)
        self.target_status = QtWidgets.QComboBox()
        self.target_status.addItems(sorted(self.page_widget.get_task_statutes(False)))
        self.target_status.setCurrentText('Work In Progress')
        self.content_layout.addWidget(self.target_status, 0, 2, 1, 3, QtCore.Qt.AlignVCenter)

        self.content_layout.addWidget(LabelIcon(('icons.flow', 'input')), 1, 0, QtCore.Qt.AlignVCenter)
        self.content_layout.addWidget(QtWidgets.QLabel('Comment'), 1, 1, QtCore.Qt.AlignVCenter)
        self.comment = QtWidgets.QTextEdit('')
        self.content_layout.addWidget(self.comment, 1, 2, 1, 3, QtCore.Qt.AlignVCenter)

        self.content_layout.addWidget(LabelIcon(('icons.flow', 'input')), 2, 0, QtCore.Qt.AlignVCenter)
        self.content_layout.addWidget(QtWidgets.QLabel('Files'), 2, 1, QtCore.Qt.AlignVCenter)
        self.files = FilesUploadComboBox(self)
        self.content_layout.addWidget(self.files, 2, 2, QtCore.Qt.AlignVCenter)

        self.files_buttons = QtWidgets.QWidget()
        self.files_buttons_lo = QtWidgets.QHBoxLayout()
        self.files_buttons_lo.setContentsMargins(0,0,0,0)
        self.files_buttons_lo.setSpacing(0)
        self.files_buttons.setLayout(self.files_buttons_lo)

        self.button_add = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.gui', 'add-file'))), '')
        self.button_add.setIconSize(QtCore.QSize(13,13))
        self.button_add.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_add.clicked.connect(self._on_add_files_button_clicked)
        self.files_buttons_lo.addWidget(self.button_add)
        self.button_clear = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.libreflow', 'delete'))), '')
        self.button_clear.setIconSize(QtCore.QSize(13,13))
        self.button_clear.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_clear.clicked.connect(self._on_clear_button_clicked)
        self.files_buttons_lo.addWidget(self.button_clear)

        self.content_layout.addWidget(self.files_buttons, 2, 3, QtCore.Qt.AlignVCenter)
        self.content_layout.setColumnStretch(2, 1)

        # Buttons
        self.button_layout = QtWidgets.QHBoxLayout()

        self.button_post = QtWidgets.QPushButton('Post')
        self.button_cancel = QtWidgets.QPushButton('Cancel')

        self.button_post.clicked.connect(self._on_post_button_clicked)
        self.button_cancel.clicked.connect(self._on_cancel_button_clicked)

        self.button_post.setAutoDefault(False)
        self.button_cancel.setAutoDefault(False)

        self.button_layout.addStretch()
        self.button_layout.addWidget(self.button_post)
        self.button_layout.addWidget(self.button_cancel)

        self.layout.addLayout(self.content_layout)
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def sizeHint(self):
        return QtCore.QSize(530, 275)

    def _on_add_files_button_clicked(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)

        if dialog.exec_():
            paths = dialog.selectedFiles()
            self.files.addFiles(paths)

    def _on_clear_button_clicked(self):
        self.files.clear()

    def _on_post_button_clicked(self):
        items = self.files.fetchItems()
        if len(items) == 1:
            if items[0].primary_file:
                self.page_widget.upload_preview(
                    self.page_widget.session.cmds.Flow.get_value(self.task_item.oid+'/entity_id'),
                    self.task_item.task_type,
                    self.target_status.currentText(),
                    items[0].path,
                    self.comment.toPlainText()
                )
                return self.page_widget.list.refresh(True)
        
        paths = [item.path for item in items]
        self.page_widget.set_task_status(
            self.task_item.task_id,
            self.target_status.currentText(),
            self.comment.toPlainText(),
            paths
        )
        self.page_widget.list.refresh(True)

    def _on_cancel_button_clicked(self):
        self.close()


class TaskFile(QtWidgets.QTreeWidgetItem):

    def __init__(self, tree, file_oid):
        super(TaskFile, self).__init__(tree)
        self.tree = tree
        self.file_oid = file_oid
        self.page_widget = tree.page_widget

        self.refresh()
    
    def refresh(self):
        self.file_name = self.page_widget.session.cmds.Flow.get_value(self.file_oid+'/display_name')
        name, ext = os.path.splitext(self.file_name)
        if ext:
            icon = CHOICES_ICONS.get(
                ext[1:], ('icons.gui', 'text-file-1')
            )
        else:
            icon = ('icons.gui', 'folder-white-shape')

        self.setIcon(0, self.get_icon(icon))
        self.setText(0, self.file_name)

        self.setExpanded(True)
    
    @staticmethod
    def get_icon(icon_ref):
        return QtGui.QIcon(resources.get_icon(icon_ref))


class TaskFiles(QtWidgets.QTreeWidget):

    def __init__(self, task_item):
        super(TaskFiles, self).__init__(task_item)
        self.task_item = task_item
        self.page_widget = task_item.page_widget

        self.action_manager = ObjectActionMenuManager(
            self.page_widget.session, self.page_widget.page.show_action_dialog, 'Flow.map'
        )

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('''
        QTreeView::item {
            height: 25px;
        }
        QTreeView::item:selected {
            background-color: #223e55;
            color: white;
        }'''
        )
        self.setRootIsDecorated(False)

        self.setHeaderLabel('Files')
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.refresh()

        self.header().setStretchLastSection(True)

        self.itemDoubleClicked.connect(self._on_item_double_clicked)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._on_context_menu)

    def refresh(self):
        self.blockSignals(True)
        self.clear()

        primary_files = sorted(self.page_widget.session.cmds.Flow.get_value(
            self.task_item.oid+'/primary_files'
        ))

        for oid in primary_files:
            TaskFile(self, oid)

        self.blockSignals(False)
    
    def _on_item_double_clicked(self, item):
        self.page_widget.page.show_action_dialog(self.page_widget.session.cmds.Flow.call(
            item.file_oid, 'activate_oid', [], {}
        ))

    def _on_context_menu(self, pos):
        item = self.itemAt(pos)

        if item is None:
            return

        self.action_menu = QtWidgets.QMenu()

        has_actions = self.action_manager.update_oid_menu(
            item.file_oid, self.action_menu, with_submenus=True
        )

        if has_actions:
            self.action_menu.exec_(self.viewport().mapToGlobal(pos))


class TaskItem(QtWidgets.QWidget):

    def __init__(self, tasks_list, oid):
        super(TaskItem, self).__init__()
        self.setObjectName('TaskItem')
        self.tasks_list = tasks_list
        self.page_widget = tasks_list.page_widget
        self.oid = oid

        self.task_id = self.page_widget.session.cmds.Flow.get_value(self.oid+'/task_id')
        self.task_type = self.page_widget.session.cmds.Flow.get_value(self.oid+'/task_type')
        self.task_oid = self.page_widget.session.cmds.Flow.get_value(self.oid+'/task_oid')
        self.dft_task_name = self.page_widget.session.cmds.Flow.get_value(self.oid+'/dft_task_name')
        
        self.op = QtWidgets.QGraphicsOpacityEffect(self)
        self.op.setOpacity(1.00)
        self.setGraphicsEffect(self.op)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            '''
            QWidget {
                font-size: 12px;
            }
            #TaskItem {
                background-color: palette(window);
                border: palette(dark);
                border-radius: 5px;
            }
            '''
        )
        self.setMaximumHeight(200)

        self.expanded = False

        self.build()
        self.refresh()

    def build(self):
        container = QtWidgets.QGridLayout()
        container.setMargin(10)

        # Left Layout
        left_lo = QtWidgets.QVBoxLayout()
        self.oid_lo = QtWidgets.QHBoxLayout()
        self.oid_lo.setSpacing(0)
        left_lo.addLayout(self.oid_lo)

        self.expand_button = QtWidgets.QToolButton()
        self.expand_button.setFixedSize(20, 20)
        self.expand_button.setIconSize(QtCore.QSize(10, 10))
        self.expand_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.expand_button.clicked.connect(self._on_expand_button_clicked)
        self.oid_lo.addWidget(self.expand_button)

        if self.dft_task_name is None:
            task_warning = WarningFrame(self, f'Cannot find {self.task_type} task')
            left_lo.addWidget(task_warning)
        else:
            self.files_list = TaskFiles(self)
            left_lo.addWidget(self.files_list)

        # Right Layout
        ## Kitsu
        self.right_kitsu = QtWidgets.QWidget()
        self.kitsu_lo = QtWidgets.QVBoxLayout()
        self.kitsu_lo.setContentsMargins(0,0,0,0)
        kitsu_header = QtWidgets.QHBoxLayout()
        kitsu_header.setSpacing(0)

        self.type_label = QtWidgets.QLabel('')
        self.status_label = QtWidgets.QLabel('')
        self.redirect_task = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.libreflow', 'kitsu'))), '')
        self.redirect_task.setIconSize(QtCore.QSize(13,13))
        self.redirect_task.setStyleSheet('padding: 2;')
        self.edit_status = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.libreflow', 'edit-blank'))), '')
        self.edit_status.setIconSize(QtCore.QSize(13,13))
        self.edit_status.setStyleSheet('padding: 2;')
        self.edit_status.clicked.connect(self._on_edit_status_button_clicked)
        kitsu_header.addStretch()
        kitsu_header.addWidget(self.type_label)
        kitsu_header.addWidget(self.status_label)
        kitsu_header.addWidget(self.edit_status)
        kitsu_header.addWidget(self.redirect_task)

        self.kitsu_lo.addLayout(kitsu_header)

        self.kitsu_comments = QtWidgets.QTextBrowser()
        self.kitsu_comments.setOpenExternalLinks(True)
        self.kitsu_comments.setReadOnly(True)
        self.kitsu_comments.setPlaceholderText('No comment for this task.')

        self.kitsu_lo.addWidget(self.kitsu_comments)
        self.right_kitsu.setLayout(self.kitsu_lo)

        ## Entity Data
        self.right_entity = QtWidgets.QWidget()
        entity_lo = QtWidgets.QGridLayout()
        entity_lo.setContentsMargins(0,0,0,0)

        self.header_spacer = QtWidgets.QWidget()
        header_spacer_lo = QtWidgets.QVBoxLayout()
        header_spacer_lo.setContentsMargins(0,0,0,0)
        self.header_spacer.setLayout(header_spacer_lo)
        self.spacer = QtWidgets.QSpacerItem(0, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        header_spacer_lo.addItem(self.spacer)

        if self.task_id is None:
            self.task_warning = WarningFrame(
                self, f'Cannot find {self.dft_task_name} task on Kitsu'
            )
            entity_lo.addWidget(self.header_spacer, 0, 0, QtCore.Qt.AlignTop)
            entity_lo.addWidget(self.task_warning, 1, 0)
            self.right_entity.setLayout(entity_lo)
            self.right_kitsu.hide()
        else:
            self.shot_header = QtWidgets.QWidget()
            shot_header_lo = QtWidgets.QHBoxLayout()
            shot_header_lo.setContentsMargins(0,0,0,0)
            self.shot_header.setLayout(shot_header_lo)

            self.shot_icon = QtWidgets.QLabel()
            pm = resources.get_pixmap('icons.gui', 'film-strip-with-two-photograms')
            self.shot_icon.setPixmap(pm.scaled(23, 23, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            self.shot_icon.setAlignment(QtCore.Qt.AlignCenter)
            self.shot_frames = QtWidgets.QLabel('Frames duration')
            self.shot_frames.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

            shot_header_lo.addWidget(self.shot_icon)
            shot_header_lo.addWidget(self.shot_frames)
            shot_header_lo.addStretch()
            entity_lo.addWidget(self.shot_header, 0, 0, QtCore.Qt.AlignTop)
            entity_lo.addWidget(self.header_spacer, 0, 0, QtCore.Qt.AlignTop)

            self.entity_description = QtWidgets.QTextEdit('')
            self.entity_description.setPlaceholderText('No description')
            self.entity_description.setReadOnly(True)
            # Set line spacing
            descBlockFmt = QtGui.QTextBlockFormat()
            descBlockFmt.setLineHeight(120, QtGui.QTextBlockFormat.ProportionalHeight)
            descTextCursor = self.entity_description.textCursor()
            descTextCursor.clearSelection()
            descTextCursor.select(QtGui.QTextCursor.Document)
            descTextCursor.mergeBlockFormat(descBlockFmt)

            entity_lo.addWidget(self.entity_description, 1, 0, QtCore.Qt.AlignTop)
            self.right_entity.setLayout(entity_lo)
            self.right_entity.hide()

        container.addLayout(left_lo, 0, 0)
        container.addWidget(self.right_kitsu, 0, 1)
        container.addWidget(self.right_entity, 0, 1)
        container.setColumnStretch(0, 3)
        container.setColumnStretch(1, 2)
        self.setLayout(container)

    def refresh(self):
        entity_type = self.page_widget.session.cmds.Flow.get_value(self.oid+'/entity_type')

        # Navigation buttons
        project_oid = self.page_widget.get_project_oid()

        label_to_oid = self.page_widget.session.cmds.Flow.split_oid(self.task_oid, True, project_oid)
        for i, (label, goto_oid) in enumerate(label_to_oid):
            nav_button = NavigationButton(label, goto_oid, self)
            self.oid_lo.addWidget(nav_button)
            if i != len(label_to_oid)-1:
                self.oid_lo.addWidget(NavigationSeparator(nav_button, self))

        # Bookmark
        if self.page_widget.session.cmds.Flow.get_value(self.oid+'/is_bookmarked'):
            self.bookmark_button = QtWidgets.QToolButton()
            self.bookmark_button.setFixedSize(22, 22)
            self.bookmark_button.setIconSize(QtCore.QSize(14, 14))
            self.bookmark_button.setIcon(resources.get_icon(('icons.gui', 'star')))
            self.bookmark_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.bookmark_button.clicked.connect(self._on_bookmark_button_clicked)
            self.oid_lo.addWidget(self.bookmark_button)
        self.oid_lo.addStretch()

        if self.task_id:
            # Task Status
            status = self.page_widget.session.cmds.Flow.get_value(self.oid+'/task_status')
            self.type_label.setText(f'{self.task_type} -')
            self.status_label.setText(f'{status.upper()}')

            # Redirect Task
            task_link = self.create_task_link(entity_type)
            self.redirect_task.clicked.connect(lambda: self._on_redirect_task_button_clicked(task_link))

            # Comments
            comments = self.page_widget.get_task_comments(self.task_id)

            if comments:
                comment_html = '''
                <style>
                    a:link {
                        color: #00BFFF;
                        background-color: transparent;
                        text-decoration: none;
                    }
                    .separator {
                        border-bottom: 1px solid white;
                        border-collapse: collapse;
                    }
                    .spacer {
                        margin-bottom: 10px;
                    }
                </style>
                '''

                for i, c in enumerate(comments):
                    date_object = datetime.datetime.strptime(c['created_at'], "%Y-%m-%dT%H:%M:%S")

                    comment_html = comment_html + '''
                    <table cellspacing=0 width=100%>
                    <tr>
                        <td><span style='color: {color}; font-weight: bold;'>{status}</span> - {name}</td>
                        <td align=right>{date}</td>
                    </tr>
                    </table>
                    '''.format(
                        color=c['task_status']['color'],
                        status=c['task_status']['short_name'].upper(),
                        name=c['person']['first_name'] + ' ' + c['person']['last_name'],
                        date=date_object.strftime('%d/%m'),
                    )

                    if c['text'] != '':
                        if '\n' in c['text']:
                            comment_lines = c['text'].split('\n')
                            for line in comment_lines:
                                comment_html = comment_html + '''<p>{text}</p>'''.format(text=line)
                        else:
                            comment_html = comment_html + '''<p>{text}</p>'''.format(text=c['text'])

                    if c['previews'] != []:
                        revision_link = self.create_revision_link(entity_type, c['previews'][0]['id'])
                        comment_html = comment_html + '''<p><a href='{link}'>Revision</a></p>'''.format(link=revision_link)
                    
                    if i == 0:
                        self.status_label.setStyleSheet(f'color: {c["task_status"]["color"]}; font-weight: 700; padding-right: 1;')

                    if i == len(comments)-1:
                        continue
                    comment_html = comment_html + '''<table cellspacing=0 class="spacer" width=100%><tr><td class="separator"/></tr></table>'''

                self.kitsu_comments.setHtml(comment_html)

            if self.status_label.styleSheet() == '':
                status_data = self.page_widget.get_task_status(status)
                self.status_label.setStyleSheet(f'color: {status_data["color"]}; font-weight: 700; padding-right: 1;')

            if self.page_widget.session.cmds.Flow.get_value(self.oid+'/shot_frames'):
                self.header_spacer.hide()
                frames = self.page_widget.session.cmds.Flow.get_value(self.oid+'/shot_frames')
                project_fps = int(self.page_widget.get_project_fps())
                timecode = self.frames_to_timecode(frames, project_fps)
                self.shot_frames.setText(str(frames)+' frames ('+timecode+')')
            else:
                self.shot_header.hide()
            self.entity_description.setText(self.page_widget.session.cmds.Flow.get_value(self.oid+'/entity_description'))

        # Expand
        if self.task_id in self.tasks_list.tasks_expanded:
            if self.tasks_list.tasks_expanded[self.task_id]:
                self.expanded = True
        elif self.page_widget.get_auto_expand():
            self.expanded = True
        self.expand()

    def frames_to_timecode(self, frames, fps):
        h = int(frames / 86400) 
        m = int(frames / 1440) % 60
        s = int((frames % 1440)/fps)
        f = frames % 1440 % fps
        return ( "%02d:%02d:%02d:%02d" % ( h, m, s, f))

    def create_task_link(self, entity_type):
        return '{server}/productions/{project}/{entity}/tasks/{task}'.format(
            server=self.page_widget.get_server_url(),
            project=self.page_widget.get_project_id(),
            entity=entity_type.lower(),
            task=self.task_id
        )

    def create_revision_link(self, entity_type, preview_id):
        return '{server}/productions/{project}/{entity}/tasks/{task}/previews/{preview}'.format(
            server=self.page_widget.get_server_url(),
            project=self.page_widget.get_project_id(),
            entity=entity_type.lower(),
            task=self.task_id,
            preview=preview_id
        )
    
    def expand(self):
        if self.expanded:
            self.expand_button.setIcon(resources.get_icon(('icons.gui', 'arrow-down')))
            self.setMinimumHeight(165)
            if self.dft_task_name is not None:
                self.files_list.show()
            if self.task_id is not None:
                self.kitsu_comments.show()
                self.entity_description.show()
            else:
                self.task_warning.show()
        else:
            self.expand_button.setIcon(resources.get_icon(('icons.gui', 'arrow-right')))
            self.setMinimumHeight(0)
            if self.dft_task_name is not None:
                self.files_list.hide()
            if self.task_id is not None:
                self.kitsu_comments.hide()
                self.entity_description.hide()
            else:
                self.task_warning.hide()

    def _on_expand_button_clicked(self):
        if self.expanded:
            self.expanded = False
        else:
            self.expanded = True
        self.expand()
        
        self.tasks_list.tasks_expanded[self.task_id] = self.expanded
        self.page_widget.update_presets(expand_data=self.tasks_list.tasks_expanded)

    def _on_bookmark_button_clicked(self):
        is_bookmarked = self.page_widget.toggle_bookmark(self.task_oid)
        if is_bookmarked:
            self.bookmark_button.setIcon(resources.get_icon(('icons.gui', 'star')))
        else:
            self.bookmark_button.setIcon(resources.get_icon(('icons.gui', 'star-1')))

    def _on_redirect_task_button_clicked(self, link):
        webbrowser.open(link)
    
    def _on_edit_status_button_clicked(self):
        dialog = EditStatusDialog(self)
        dialog.exec()


class MyTasksList(QtWidgets.QScrollArea):

    def __init__(self, page_widget):
        super(MyTasksList, self).__init__()
        self.page_widget = page_widget
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.tasks_expanded = {}

        self.setStyleSheet(
            '''
            QScrollArea {
                border: palette(dark); border-radius: 5px;
            }
            '''
        )

        self.refresh()
        self.page_widget.header.search.textChanged.connect(self.refresh_search)

    def refresh(self, force_update=False):
        if force_update:
            self.page_widget.footer.left_text.setText('Updating...')
            self.page_widget.footer.left_text.setStyleSheet('color: red; font-weight: 700;')
            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                if widget is not None:
                    widget.op.setOpacity(0.50)

            QtWidgets.QApplication.processEvents()
            QtWidgets.QApplication.processEvents()

        self.page_widget.header.search.setText('')

        tasks = self.page_widget.session.cmds.Flow.call(
            self.page_widget.oid, 'get_tasks', {force_update}, {}
        )
        self.tasks_expanded = self.page_widget.get_user_expanded()

        container = QtWidgets.QWidget()
        container.setObjectName('ScrollAreaContainer')
        container.setStyleSheet(
            '''
            #ScrollAreaContainer {
                background-color: palette(base);
                border: palette(dark);
                border-radius: 5px;
            }
            '''
        )
        self.layout = QtWidgets.QVBoxLayout(container)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setSpacing(10)
        
        for task in tasks:
            item = TaskItem(self, task.oid())
            self.layout.addWidget(item)

        for task_id, value in list(self.tasks_expanded.items()):
            has_key = False
            for task in tasks:
                if task_id == task.task_id.get():
                    has_key = True
                    break
            if not has_key:
                self.tasks_expanded.pop(task_id)
        
        self.layout.addStretch(1)
        self.layout.setMargin(10)
        self.setWidget(container)

        self.page_widget.update_presets(expand_data=self.tasks_expanded)

        if force_update:
            self.page_widget.footer.refresh_count()

    def refresh_search(self, query_filter):
        count = 0
        keywords = query_filter.split()
        query_filter = '.*'+'.*'.join(keywords)
        for i in reversed(range(self.layout.count())):
            task = self.layout.itemAt(i).widget()
            if task is not None:
                if re.match(query_filter, task.task_oid):
                    task.show()
                    count = count + 1
                else:
                    task.hide()
        self.page_widget.footer.left_text.setText(str(count)+' Tasks')

    def get_count(self):
        return self.layout.count() - 1

    def toggle_entity_data(self):
        for i in reversed(range(self.layout.count())):
            task = self.layout.itemAt(i).widget()
            if task is not None:
                if task.task_id:
                    if task.right_kitsu.isVisible():
                        task.right_kitsu.hide()
                        task.right_entity.show()
                    else:
                        task.right_entity.hide()
                        task.right_kitsu.show()


class MyTasksSearch(QtWidgets.QLineEdit):

    def __init__(self, header):
        super(MyTasksSearch, self).__init__()
        self.header = header
        self.page_widget = header.page_widget
        self.setPlaceholderText('Search...')
   
    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape) or (event.key() == QtCore.Qt.Key_Return):
            self.clearFocus()
        else:
            super(MyTasksSearch, self).keyPressEvent(event)


class MyTasksHeader(QtWidgets.QWidget):

    def __init__(self, page_widget):
        super(MyTasksHeader, self).__init__(page_widget)
        self.page_widget = page_widget
        self.build_completed = False
        self.build()

    def build(self):
        self.refresh_icon = QtGui.QIcon(resources.get_icon(('icons.gui', 'refresh')))
        self.refresh_button = QtWidgets.QPushButton(self.refresh_icon, '')
        self.refresh_button.clicked.connect(self._on_refresh_button_clicked)
        self.refresh_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.filter_label = QtWidgets.QLabel('Filter by')
        self.filter_combobox = FilterStatusComboBox()
        self.filter_combobox.addItem('Default', preset=True)
        self.filter_combobox.addItem('-')
        self.filter_combobox.addItems(sorted([task.upper() for task in self.page_widget.get_task_statutes(True)]))
        self.filter_combobox.setDefaultPreset()
        filter_value = self.page_widget.get_user_filter()
        if filter_value == []:
            self.filter_combobox.setChecked(['Default'], True)
        else:
            for statues in filter_value:
                self.filter_combobox.setChecked([statues], True)
        self.filter_combobox.previousData = self.filter_combobox.fetchNames()
        self.page_widget.update_presets(filter_data=self.filter_combobox.previousData)
        
        self.sort_label = QtWidgets.QLabel('Sort by')
        self.sort_combobox = QtWidgets.QComboBox()
        self.sort_combobox.addItems(['Entity name', 'Status', 'Latest update'])
        self.sort_combobox.currentTextChanged.connect(self._on_sort_combobox_changed)
        self.sort_combobox.setView(QtWidgets.QListView())
        self.sort_combobox.setStyleSheet(
            '''QComboBox QAbstractItemView::item {
                min-height: 20px;
            }'''
        )
        sort_value = self.page_widget.get_user_sorted()
        if sort_value == None:
            self.page_widget.update_presets(sort_data='Entity name')
        else:
            self.sort_combobox.setCurrentText(sort_value)

        self.search = MyTasksSearch(self)

        self.kitsu_tasks = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.libreflow', 'kitsu'))), 'My Tasks')
        self.kitsu_tasks.clicked.connect(self._on_kitsu_tasks_button_clicked)
        self.kitsu_tasks.setIconSize(QtCore.QSize(13,13))
        self.kitsu_tasks.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.fdt_button = QtWidgets.QPushButton('FDT')
        self.fdt_button.clicked.connect(self._on_fdt_button_clicked)
        self.fdt_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        hlo = QtWidgets.QHBoxLayout()
        hlo.addWidget(self.refresh_button)
        hlo.addWidget(self.filter_label)
        hlo.addWidget(self.filter_combobox)
        hlo.addWidget(self.sort_label)
        hlo.addWidget(self.sort_combobox)
        hlo.addWidget(self.search)
        hlo.addStretch()
        hlo.addWidget(self.kitsu_tasks)
        hlo.addWidget(self.fdt_button)
        hlo.setContentsMargins(0,0,0,5)
        self.setLayout(hlo)
        self.build_completed = True

    def _on_sort_combobox_changed(self, value):
        if self.build_completed == False:
            return
        self.page_widget.update_presets(sort_data=value)
        self.page_widget.list.refresh(force_update=True)

    def _on_refresh_button_clicked(self):
        self.page_widget.list.refresh(force_update=True)

    def _on_kitsu_tasks_button_clicked(self):
        webbrowser.open(self.page_widget.get_server_url() + '/todos')

    def _on_fdt_button_clicked(self):
        webbrowser.open('https://fdt.lesfees.net/')


class MyTasksPageWidget(CustomPageWidget):

    def build(self):
        self.setStyleSheet('outline: 0;')

        self.header = MyTasksHeader(self)
        self.list = MyTasksList(self)
        self.footer = MyTasksFooter(self)

        vlo = QtWidgets.QVBoxLayout()
        vlo.addWidget(self.header)
        vlo.addWidget(self.list)
        vlo.addWidget(self.footer)
        vlo.setSpacing(0)
        vlo.setMargin(0)
        self.setLayout(vlo)

        self.key_press_start_time = -1
    
    def sizeHint(self):
        return QtCore.QSize(2000, 2000)

    def keyPressEvent(self, event):
        super(MyTasksPageWidget, self).keyPressEvent(event)

        if event.key() == QtCore.Qt.Key_Shift:
            self.list.toggle_entity_data()
            self.key_press_start_time =  time.time()

    def keyReleaseEvent(self, event):
        super(MyTasksPageWidget, self).keyReleaseEvent(event)
        key_press_time = time.time() - self.key_press_start_time

        if event.key() == QtCore.Qt.Key_Shift and key_press_time > 0.5:
            self.list.toggle_entity_data()

    def get_project_oid(self):
        return self.session.cmds.Flow.call(
            self.oid, 'get_project_oid', {}, {}
        )

    def get_project_id(self):
        return self.session.cmds.Flow.call(
            self.oid, 'get_project_id', {}, {}
        )

    def get_project_fps(self):
        return self.session.cmds.Flow.call(
            self.oid, 'get_project_fps', {}, {}
        )

    def get_user_filter(self):
        return self.session.cmds.Flow.get_value(self.oid+'/settings/task_statues_filter')

    def get_user_sorted(self):
        return self.session.cmds.Flow.get_value(self.oid+'/settings/task_sorted')
    
    def get_user_expanded(self):
        return self.session.cmds.Flow.get_value(self.oid+'/settings/tasks_expanded')

    def get_auto_expand(self):
        return self.session.cmds.Flow.get_value(self.oid+'/settings/auto_expand')

    def get_task_comments(self, task_id):
        return self.session.cmds.Flow.call(
            self.oid, 'get_task_comments', {task_id}, {}
        )

    def get_server_url(self):
        return self.session.cmds.Flow.call(
            self.oid, 'get_server_url', {}, {}
        )

    def is_uploadable(self, file_name):
        return self.session.cmds.Flow.call(
            self.oid, 'is_uploadable', [file_name], {}
        )

    def get_task_statutes(self, short_name):
        return self.session.cmds.Flow.call(
            self.oid, 'get_task_statutes', [short_name], {}
        )

    def get_task_status(self, task_status_name):
        return self.session.cmds.Flow.call(
            self.oid, 'get_task_status', [task_status_name], {}
        )

    def set_task_status(self, task_id, task_status_name, comment, files):
        return self.session.cmds.Flow.call(
            self.oid, 'set_task_status', [task_id, task_status_name, comment, files], {}
        )

    def upload_preview(self, entity_id, task_name, task_status_name, file_path, comment):
        return self.session.cmds.Flow.call(
            self.oid, 'upload_preview', [entity_id, task_name, task_status_name, file_path, comment], {}
        )

    def toggle_bookmark(self, oid):
        return self.session.cmds.Flow.call(
            self.oid, 'toggle_bookmark', [oid], {}
        )

    def update_presets(self, filter_data=None, sort_data=None, expand_data=None):
        if filter_data:
            self.session.cmds.Flow.set_value(self.oid+'/settings/task_statues_filter', filter_data)
        if sort_data:
            self.session.cmds.Flow.set_value(self.oid+'/settings/task_sorted', sort_data)
        if expand_data:
            self.session.cmds.Flow.set_value(self.oid+'/settings/tasks_expanded', expand_data)
        return self.session.cmds.Flow.call(
            self.oid+'/settings', 'update_presets', {}, {}
        )
