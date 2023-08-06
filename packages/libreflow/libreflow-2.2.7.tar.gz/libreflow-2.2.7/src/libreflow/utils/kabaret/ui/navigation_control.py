import six
import qtpy
import functools

from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtGui, QtCore
from kabaret.app.ui.gui.widgets.flow_layout import FlowLayout
from kabaret.app.ui.gui.widgets.popup_menu import PopupMenu
from kabaret.app import resources


class Separator(QtWidgets.QToolButton):
    def __init__(self, related_navigation_button):
        super(Separator, self).__init__(related_navigation_button)
        self.setProperty("class", "nav_separator")
        self.related_navigation_button = related_navigation_button
        self.setIcon(resources.get_icon(
            ('icons.flow', 'collapsed'),
            disabled_ref=('icons.flow', 'collapsed')
        ))
    
    def mousePressEvent(self, e):
        self.related_navigation_button._show_navigables_menu(self.related_navigation_button.nav_widget.current_oid())
        super(Separator, self).mousePressEvent(e)

    def sizeHint(self):
        return QtCore.QSize(18, 24)

class NavigationButton(QtWidgets.QToolButton):

    def __init__(self, name, oid, nav_widget, is_last=False):
        super(NavigationButton, self).__init__(nav_widget)
        self.name = name
        self.oid = oid
        self.nav_widget = nav_widget
        self._last_click_pos = QtCore.QPoint()

        self.setFont(self.nav_widget.bt_font)
        self.setProperty('tight_layout', True)
        self.setProperty('hide_arrow', True)
        self.setProperty('no_border', True)
        self.setProperty('square', True)
        self.setArrowType(QtCore.Qt.NoArrow)
        self.setProperty('last', is_last)

        # Removed the map name before the ":"
        # Not changing it 
        self.setText('%s' % (self.name.split(":")[-1],))

        self.clicked.connect(self._goto)

        self._menu = PopupMenu(self)

    def _goto_oid(self, oid):
        self.nav_widget._goto(oid)

    def _goto(self, b=None):
        self.nav_widget._goto(self.oid)

    def _show_navigables_menu(self, full_oid):
        self._menu.clear()

        m = self._menu

        m.addAction('Loading...')
        # self.setMenu(m)
        # self.showMenu()

        session = self.nav_widget._navigator.session
        try:
            navigatable_entries = session.cmds.Flow.get_navigable_oids(
                self.oid, full_oid
            )
        except Exception as err:
            m.clear()
            m.addAction('ERROR: ' + str(err))
            raise
        print (navigatable_entries)
        print(session.cmds.Flow.get_navigable_oids(
                self.oid, "/MyHomeRoot"
            ))
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
            self._show_navigables_menu(self.nav_widget.current_oid())
        else:
            self._last_click_pos = e.pos()
        super(NavigationButton, self).mousePressEvent(e)

    def mouseMoveEvent(self, e):
        super(NavigationButton, self).mouseMoveEvent(e)

        if self._last_click_pos.isNull():
            return
        drag_distance = (e.pos() - self._last_click_pos).manhattanLength()
        if drag_distance < QtWidgets.QApplication.startDragDistance():
            return

        oids = [self.oid]
        mime_data = QtCore.QMimeData()
        md = self.nav_widget._navigator.session.cmds.Flow.to_mime_data(oids)
        for data_type, data in six.iteritems(md):
            mime_data.setData(data_type, data)

        pixmap = QtGui.QPixmap(self.size())
        self.render(pixmap)

        # below makes the pixmap half transparent
        painter = QtGui.QPainter(pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(pixmap.rect(), QtGui.QColor(0, 0, 0, 127))
        painter.end()

        # make a QDrag
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        drag.setPixmap(pixmap)

        # shift the Pixmap so that it coincides with the cursor position
        drag.setHotSpot(self._last_click_pos)

        # start the drag operation
        # exec_ will return the accepted action from dropEvent
        drag_result = drag.exec_(QtCore.Qt.CopyAction)

    def mouseReleaseEvent(self, e):
        self._last_click_pos = QtCore.QPoint()
        super(NavigationButton, self).mouseReleaseEvent(e)


class NavigationOIDControls(QtWidgets.QWidget):

    def __init__(self, parent, navigator):
        super(NavigationOIDControls, self).__init__(parent)

        self._navigator = navigator

        self.nav_oid_bar = parent
        self.bt_font = self.font()
        self.bt_font.setPointSize(self.bt_font.pointSize() * 1.3)

        self._flow_lo = FlowLayout()
        self.setLayout(self._flow_lo)
        self._flow_lo.setContentsMargins(2, 0, 2, 0)
        self._flow_lo.setSpacing(0)

    def update_controls(self):
        self._flow_lo.clear()

        label_to_oid = self._navigator.split_current_oid()
        i = 1
        
        for label, goto_oid in label_to_oid:
            if i>1 :
                self._flow_lo.addWidget(Separator(tb))
            tb = NavigationButton(label, goto_oid, self, i == len(label_to_oid))
            tb.adjustSize()
            self._flow_lo.addWidget(tb)
            i += 1
        if not self.isVisible():
            self.show()

    def _goto_home(self):
        self._navigator.goto_root()

    def _goto(self, oid):
        in_new_view = (
            QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier
        )
        self._navigator.goto(oid, in_new_view)

    def current_oid(self):
        return self._navigator.current_oid()


class NavigationOIDField(QtWidgets.QLineEdit):
    def __init__(self, parent, navigator):
        super(NavigationOIDField, self).__init__(parent)
        self._navigator = navigator
        self.session = navigator.session
        self.nav_oid_bar = parent
        field_font = self.font()
        field_font.setPointSize(field_font.pointSize() * 1.3)

        self.setFont(field_font)

        self.textEdited.connect(self.update_completion)
        self.completion_current_oid = ""  
        self.completer = QtWidgets.QCompleter([], self)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompleter(self.completer)

    def get_completion_current_oid(self, text):
        if not text:
            return "/"
        if text.endswith("/"):
            return text
        if text.startswith("/"):
            return text.rpartition("/")[0] + "/"
        else:
            return "/"

    def update_completion(self, text):
        current_oid = self.get_completion_current_oid(text)
        if current_oid == self.completion_current_oid:
            return
        self.completion_current_oid = current_oid

        if not current_oid or current_oid == "/":
            _target_oid = True
        else:
            try:
                _target_oid = self.session.cmds.Flow.exists(current_oid)
            except:
                _target_oid = False
                # TODO : RAISE ERROR ?
                print("INVALID PROJECT OID ? : ", current_oid)
                self.setProperty('error', True)

        if _target_oid:
            if not current_oid or current_oid == "/":
                # Get list of project
                projects = self.session.get_actor("Flow").get_projects_info()
                completion_oid_list = list(map(lambda p: "/" + p[0], projects))
                # Add the Home Oid to the autocompletion list
                completion_oid_list.append(self.session.get_actor("Flow").home_root().Home.oid())
            else:
                # get list of children of current oid
                navigatable_entries =  self.session.cmds.Flow.get_navigable_oids(
                    current_oid.rpartition("/")[0], current_oid.rpartition("/")[0]
                )
                completion_oid_list = map(lambda navigatable_entry: navigatable_entry[1] ,navigatable_entries[navigatable_entries.index(None)+1:])
            self.completer.model().setStringList(completion_oid_list)
            

        else:
            # TODO : RAISE ERROR ?
            print("INVALID OID : ", current_oid)
            self.setProperty('error', True)

    def reset(self):
        self.setText(self._navigator.current_oid())
        self.setProperty('edited', False)

    def edit(self):
        self.reset()
        self.show()
        self.selectAll()
        self.setFocus()
        self.nav_oid_bar.nav_oid.hide()

    def accept(self):
        oid = self.text().strip()
        # HACK to remove a final '/' as user might forget it in manual editing of OIDs
        if oid[-1] == "/":
            oid = oid[:-1]
        try:
            exists = self._navigator.session.cmds.Flow.exists(oid)
        except:
            exists = False
        if not exists:
            # TODO : RAISE ERROR ?
            self.session.logger.error("INVALID OID ? : {}".format(oid))
            self.setProperty("error", True)
            return
        self.end_edit()
        in_new_view = (
            QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ControlModifier
        )
        self._navigator.goto(oid, in_new_view)

    def reject(self):
        self.reset()
        self.end_edit()

    def end_edit(self):
        self.hide()
        self.nav_oid_bar.nav_oid.show()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.reject()  # if focus lost, hide automatically
    
    def keyPressEvent(self, e):
        if e.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.accept()
        if e.key() == QtCore.Qt.Key_Escape:
            self.reject()
        else:
            self.setProperty('error', False)
            self.setProperty('edited', True)
        self.style().polish(self)
        return super().keyPressEvent(e)


class NavigationOIDBar(QtWidgets.QWidget):
    def __init__(self, parent, navigator):
        super(NavigationOIDBar, self).__init__(parent)

        self._navigator = navigator

        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setMinimumHeight(32)
        layout = QtWidgets.QHBoxLayout(self)

        self.nav_oid_field = NavigationOIDField(self, navigator)
        self.nav_oid = NavigationOIDControls(self, navigator)
        
        self.nav_oid_field.hide()
        layout.addWidget(self.nav_oid, 100, alignment=QtCore.Qt.AlignVCenter)
        layout.addWidget(self.nav_oid_field, 100, alignment=QtCore.Qt.AlignVCenter)

        layout.setMargin(0)
        self.setLayout(layout)

    def setFocusOnOidField(self):
        self.nav_oid_field.edit()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.setFocusOnOidField()
        super(NavigationOIDBar, self).mousePressEvent(e)


class NavigationHistoryControls(QtWidgets.QWidget):

    def __init__(self, parent, navigator):
        super(NavigationHistoryControls, self).__init__(parent)

        self._navigator = navigator

        self.prev_bt = QtWidgets.QToolButton(self)
        self.prev_bt.setProperty('no_border', True)
        self.prev_bt.setProperty('class', ["nav_bt", "prev_bt"])
        self.prev_bt.setText('<')
        self.prev_bt.setIcon(resources.get_icon(
            ('icons.gui', 'chevron-sign-left'),
            disabled_ref=('icons.gui', 'chevron-sign-left-disabled')
        ))
        self.prev_bt.clicked.connect(self._on_prev_bt)

        self.up_bt = QtWidgets.QToolButton(self)
        self.up_bt.setProperty('no_border', True)
        self.up_bt.setProperty('class', ["nav_bt", "up_bt"])
        self.up_bt.setText('/\\')
        self.up_bt.setIcon(resources.get_icon(
            ('icons.gui', 'chevron-sign-up'),
            disabled_ref=('icons.gui', 'chevron-sign-up-disabled')
        ))
        self.up_bt.clicked.connect(self._on_up_bt)

        self.next_bt = QtWidgets.QToolButton(self)
        self.next_bt.setProperty('no_border', True)
        self.next_bt.setProperty('class', ["nav_bt", "next_bt"])
        self.next_bt.setText('>')
        self.next_bt.setIcon(resources.get_icon(
            ('icons.gui', 'chevron-sign-to-right'),
            disabled_ref=('icons.gui', 'chevron-sign-to-right-disabled')
        ))
        self.next_bt.clicked.connect(self._on_next_bt)

        self.home_bt = QtWidgets.QToolButton(self)
        self.home_bt.setProperty('no_border', True)
        self.home_bt.setProperty('class', ["nav_bt", "home_bt"])
        self.home_bt.setText('/')
        self.home_bt.setIcon(resources.get_icon(
            ('icons.gui', 'home'),
            disabled_ref=('icons.gui', 'home-outline')
        ))
        self.home_bt.clicked.connect(self._goto_home)

        self.refresh_bt = QtWidgets.QToolButton(self)
        self.refresh_bt.setProperty('no_border', True)
        self.refresh_bt.setProperty('class', ["nav_bt", "refresh_bt"])
        self.refresh_bt.setText('/')
        self.refresh_bt.setIcon(resources.get_icon(
            ('icons.gui', 'refresh'),
            disabled_ref=('icons.gui', 'refresh')
        ))
        self.refresh_bt.clicked.connect(self._refresh)

        bt_lo = QtWidgets.QHBoxLayout()
        bt_lo.setContentsMargins(12, 0, 12, 0)
        bt_lo.setSpacing(0)
        bt_lo.addWidget(self.prev_bt)
        bt_lo.addWidget(self.up_bt)
        bt_lo.addWidget(self.next_bt)
        bt_lo.addWidget(self.home_bt)
        bt_lo.addWidget(self.refresh_bt)

        self.setLayout(bt_lo)

    def _refresh(self):
        self._navigator.refresh()

    def _goto_home(self):
        self._navigator.goto_root()

    def _on_prev_bt(self):
        # TODO: handle optional new view
        self._navigator.goto_prev()

    def _on_up_bt(self):
        # TODO: handle optional new view
        self._navigator.goto_parent()

    def _on_next_bt(self):
        # TODO: handle optional new view
        self._navigator.goto_next()

    def update_controls(self):
        self.prev_bt.setEnabled(self._navigator.has_prev())
        self.up_bt.setEnabled(self._navigator.has_parent())
        self.next_bt.setEnabled(self._navigator.has_next())
        self.home_bt.setEnabled(self._navigator.current_oid is not None and self._navigator.current_oid() != '/Home')


class NavigationBar(QtWidgets.QWidget):

    def __init__(self, parent, navigator):
        super(NavigationBar, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout(self)
        self._navigator = navigator
        self.nav_ctrl = NavigationHistoryControls(self, navigator)
        self.nav_oid_bar = NavigationOIDBar(self, navigator)
        layout.addWidget(self.nav_ctrl, 10, alignment=QtCore.Qt.AlignVCenter)
        layout.addWidget(self.nav_oid_bar, 90, alignment=QtCore.Qt.AlignVCenter)
        self.setLayout(layout)
        self.setAcceptDrops(True)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

    def dragEnterEvent(self, event):
        source = event.source()
        if source is not None:
            children = self.findChildren(type(source), source.objectName())
            if children and source in children:  # the drop come from one of its children
                return

        if event.mimeData().hasFormat("text/plain"):
            oid = event.mimeData().text()
            try:
                self._navigator.session.cmds.Flow.resolve_path(oid)
            except:
                pass
            else:
                event.acceptProposedAction()

    def dropEvent(self, event):
        oid = event.mimeData().text()
        oid = self._navigator.session.cmds.Flow.resolve_path(oid)
        self._navigator.goto(oid)
        event.acceptProposedAction()
