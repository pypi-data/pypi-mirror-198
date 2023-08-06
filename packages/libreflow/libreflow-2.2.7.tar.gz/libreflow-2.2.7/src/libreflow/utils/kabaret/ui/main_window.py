from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtCore
from kabaret.app.ui.gui.widgets.main_window import DockTitleBar, DockWidget, MainWindowManager


class DefaultDockTitleBar(DockTitleBar):

    def __init__(self, main_window_manager, dock, view):
        super(DockTitleBar, self).__init__(dock)
        self.mwm = main_window_manager
        self.dock = dock
        self.dock.topLevelChanged.connect(self.on_floating)
        self.view = view

        self.maximized = False
        self.installed = False
        self.btn_size = 25

        hlo = QtWidgets.QHBoxLayout()

        self.btn_view_menu = QtWidgets.QToolButton()
        self.btn_view_menu.setMaximumWidth(50)
        icon = self.btn_view_menu.style().standardIcon(QtWidgets.QStyle.SP_TitleBarUnshadeButton)
        self.btn_view_menu.setIcon(icon)
        self.btn_view_menu.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_view_menu.setFixedSize(QtCore.QSize(self.btn_size, self.btn_size))
        self.btn_view_menu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btn_view_menu.setToolTip('View Options')
        self.btn_view_menu.setStyleSheet('QToolButton::menu-indicator { image: none; }')

        self.title = QtWidgets.QLabel(self.view.view_title())
        self.title.setMinimumHeight(self.btn_size)
        self.title.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.btn_maximize = QtWidgets.QPushButton()
        icon = self.btn_maximize.style().standardIcon(QtWidgets.QStyle.SP_TitleBarMaxButton)
        self.btn_maximize.setIcon(icon)
        self.btn_maximize.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_maximize.setMaximumSize(QtCore.QSize(self.btn_size, self.btn_size))

        self.btn_duplicate = QtWidgets.QPushButton()
        icon = self.btn_duplicate.style().standardIcon(QtWidgets.QStyle.SP_TitleBarNormalButton)
        self.btn_duplicate.setIcon(icon)
        self.btn_duplicate.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_duplicate.setMaximumSize(QtCore.QSize(self.btn_size, self.btn_size))

        self.btn_close = QtWidgets.QPushButton()
        icon = self.btn_close.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton)
        self.btn_close.setIcon(icon)
        self.btn_close.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.btn_close.setMaximumSize(QtCore.QSize(self.btn_size, self.btn_size))

        hlo.addWidget(self.btn_view_menu, alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        hlo.addStretch(1)
        hlo.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)
        hlo.addStretch(1)
        hlo.addWidget(self.btn_maximize, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        hlo.addWidget(self.btn_duplicate, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        hlo.addWidget(self.btn_close, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        hlo.setSpacing(0)
        hlo.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hlo)

        self.btn_maximize.clicked.connect(lambda checked=False, self=self: self.mwm.toggle_maximized_dock(self))
        self.btn_duplicate.clicked.connect(lambda checked=False: self.view.create_view())
        self.btn_close.clicked.connect(lambda checked=False: self.hide_dock())

        try:
            self.view.set_on_view_title_change(self.on_view_title_change)
        except Exception as err:
            self.installed = False
            raise err
        else:
            try:
                self.install_tools()
            except Exception as err:
                self.installed = False
                raise err
            else:
                self.installed = True

    def sizeHint(self):
        return QtCore.QSize(5, self.btn_size)
    
    def install_tools(self):
        self.btn_view_menu.setMenu(self.view.view_menu)
        self.btn_view_menu.setToolTip(self.view.view_menu.title())
        self.installed = True
    
    def uninstall_tools(self):
        # FIXME: shouldn't a Hide be enough?
        self.btn_view_menu.setMenu(None)
    
    def on_view_title_change(self):
        self.title.setText(self.view.view_title())
    
    def on_floating(self, b):
        if b:
            self.dock.setTitleBarWidget(None)
            self.uninstall_tools()
        else:
            self.dock.setTitleBarWidget(self)
            self.install_tools()


class DefaultMainWindowManager(MainWindowManager):

    def create_docked_view_dock(self, view, hidden=False, area=None):
        dock = DockWidget(self.dock_closed, view.view_title(), self.main_window)
        tb = DefaultDockTitleBar(self, dock, view)
        if tb.installed:
            dock.setTitleBarWidget(tb)
        else:
            tb.deleteLater()

        dock.setWidget(view)

        dock.visibilityChanged.connect(
            lambda visible, dock=dock, view=view: self.dock_visibility_changed(visible, dock, view)
        )
        dock.setObjectName('Dock_%s_%i' % (view.view_title(), len(self._docks),))

        area = area or QtCore.Qt.LeftDockWidgetArea
        self.main_window.addDockWidget(area, dock)

        # Auto tabify views of matching type name:
        target_view = self.find_docked_view(view.view_type_name(), area=area)
        if target_view is not None:
            self.main_window.tabifyDockWidget(target_view.dock_widget(), dock)

        self._docks.append(dock)

        if len(self._docks) > 1:
            for d in self._docks:
                if d.titleBarWidget() and d.titleBarWidget().btn_maximize:
                    d.titleBarWidget().btn_maximize.setEnabled(True)
        else:
            for d in self._docks:
                if d.titleBarWidget() and d.titleBarWidget().btn_maximize:
                    d.titleBarWidget().btn_maximize.setEnabled(False)

        if hidden:
            dock.hide()

        return dock

    def toggle_maximized_dock(self, titlebar):
        button = titlebar.btn_maximize
        keeped = titlebar.dock

        if self._maximised_to_restore is None:
            button.setText('-')
            self._maximised_to_restore = self.main_window.saveState()
            for d in self._docks:
                if d is keeped:
                    continue
                d.hide()

        else:
            button.setText('+')

            self.main_window.restoreState(self._maximised_to_restore)
            self._maximised_to_restore = None
