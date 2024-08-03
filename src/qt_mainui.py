# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolButton, QTreeView,
    QTreeWidget, QTreeWidgetItem, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1399, 714)
        self.menuOpen = QAction(MainWindow)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuClose = QAction(MainWindow)
        self.menuClose.setObjectName(u"menuClose")
        self.menuExit = QAction(MainWindow)
        self.menuExit.setObjectName(u"menuExit")
        self.menuConnect = QAction(MainWindow)
        self.menuConnect.setObjectName(u"menuConnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.remoteFileTreeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(3, u"4");
        __qtreewidgetitem.setText(2, u"3");
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.remoteFileTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.remoteFileTreeWidget.setObjectName(u"remoteFileTreeWidget")
        self.remoteFileTreeWidget.setGeometry(QRect(790, 40, 591, 481))
        self.remoteFileTreeWidget.setColumnCount(4)
        self.remoteFileTreeWidget.header().setDefaultSectionSize(100)
        self.localPathEdit = QLineEdit(self.centralwidget)
        self.localPathEdit.setObjectName(u"localPathEdit")
        self.localPathEdit.setGeometry(QRect(60, 10, 521, 31))
        self.remotePathEdit = QLineEdit(self.centralwidget)
        self.remotePathEdit.setObjectName(u"remotePathEdit")
        self.remotePathEdit.setGeometry(QRect(790, 10, 591, 31))
        self.localFileTreeView = QTreeView(self.centralwidget)
        self.localFileTreeView.setObjectName(u"localFileTreeView")
        self.localFileTreeView.setGeometry(QRect(20, 40, 561, 481))
        self.logListWidget = QListWidget(self.centralwidget)
        self.logListWidget.setObjectName(u"logListWidget")
        self.logListWidget.setGeometry(QRect(20, 530, 1361, 131))
        self.fileOpenToolButton = QToolButton(self.centralwidget)
        self.fileOpenToolButton.setObjectName(u"fileOpenToolButton")
        self.fileOpenToolButton.setGeometry(QRect(20, 10, 41, 31))
        icon = QIcon()
        icon.addFile(u":/icons/dir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileOpenToolButton.setIcon(icon)
        self.fileOpenToolButton.setIconSize(QSize(32, 32))
        self.localToRemoteSendButton = QToolButton(self.centralwidget)
        self.localToRemoteSendButton.setObjectName(u"localToRemoteSendButton")
        self.localToRemoteSendButton.setGeometry(QRect(590, 190, 191, 51))
        icon1 = QIcon()
        icon1.addFile(u":/icons/rarr.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.localToRemoteSendButton.setIcon(icon1)
        self.localToRemoteSendButton.setIconSize(QSize(64, 64))
        self.remoteToLocalSendButton = QToolButton(self.centralwidget)
        self.remoteToLocalSendButton.setObjectName(u"remoteToLocalSendButton")
        self.remoteToLocalSendButton.setGeometry(QRect(590, 260, 191, 51))
        icon2 = QIcon()
        icon2.addFile(u":/icons/larr.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remoteToLocalSendButton.setIcon(icon2)
        self.remoteToLocalSendButton.setIconSize(QSize(64, 64))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1399, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menuConnect)
        self.menu.addAction(self.menuExit)
        self.menu.addAction(self.menuClose)

        self.retranslateUi(MainWindow)
        self.menuClose.triggered.connect(MainWindow.close)
        self.menuOpen.triggered.connect(MainWindow.fileOpen)
        self.remoteFileTreeWidget.itemDoubleClicked.connect(MainWindow.itemDoubleClicked)
        self.localFileTreeView.doubleClicked.connect(MainWindow.localFileItemDoubleClicked)
        self.remotePathEdit.returnPressed.connect(MainWindow.remoteEnterPressed)
        self.localPathEdit.returnPressed.connect(MainWindow.localPathEnterPressed)
        self.menuExit.triggered.connect(MainWindow.menuExit)
        self.fileOpenToolButton.clicked.connect(MainWindow.fileOpen)
        self.menuConnect.triggered.connect(MainWindow.menuConnect)
        self.localToRemoteSendButton.clicked.connect(MainWindow.localToRemoteButtonClicked)
        self.remoteToLocalSendButton.clicked.connect(MainWindow.remoteToLocalButtonClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CFT", None))
        self.menuOpen.setText(QCoreApplication.translate("MainWindow", u"\u958b\u304f", None))
        self.menuClose.setText(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b", None))
        self.menuExit.setText(QCoreApplication.translate("MainWindow", u"\u5207\u65ad", None))
        self.menuConnect.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u7d9a", None))
        self.fileOpenToolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.localToRemoteSendButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.remoteToLocalSendButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
    # retranslateUi

