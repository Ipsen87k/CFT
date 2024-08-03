# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tmain.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1399, 714)
        self.menuOpen = QAction(MainWindow)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menuClose = QAction(MainWindow)
        self.menuClose.setObjectName(u"menuClose")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setGeometry(QRect(10, 520, 771, 21))
        font = QFont()
        font.setPointSize(9)
        self.pathLabel.setFont(font)
        self.localPathEdit = QLineEdit(self.centralwidget)
        self.localPathEdit.setObjectName(u"localPathEdit")
        self.localPathEdit.setGeometry(QRect(20, 10, 561, 31))
        self.localRemoteView = QTreeView(self.centralwidget)
        self.localRemoteView.setObjectName(u"localRemoteView")
        self.localRemoteView.setGeometry(QRect(20, 40, 561, 481))
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
        self.menu.addAction(self.menuOpen)
        self.menu.addAction(self.menuClose)

        self.retranslateUi(MainWindow)
        self.menuClose.triggered.connect(MainWindow.close)
        self.menuOpen.triggered.connect(MainWindow.fileOpen)
        self.localPathEdit.returnPressed.connect(MainWindow.enterPressed)
        self.localRemoteView.doubleClicked.connect(MainWindow.localTreeViewClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CFT", None))
        self.menuOpen.setText(QCoreApplication.translate("MainWindow", u"\u958b\u304f", None))
        self.menuClose.setText(QCoreApplication.translate("MainWindow", u"\u9589\u3058\u308b", None))
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
    # retranslateUi

