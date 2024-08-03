# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_CFTConnectWindow(object):
    def setupUi(self, CFTConnectWindow):
        if not CFTConnectWindow.objectName():
            CFTConnectWindow.setObjectName(u"CFTConnectWindow")
        CFTConnectWindow.resize(675, 345)
        self.centralwidget = QWidget(CFTConnectWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.userLineEdit = QLineEdit(self.centralwidget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setGeometry(QRect(110, 50, 531, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 91, 31))
        font1 = QFont()
        font1.setPointSize(17)
        self.label_2.setFont(font1)
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(110, 90, 531, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 91, 31))
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)
        self.passwordRadioButton = QRadioButton(self.centralwidget)
        self.passwordRadioButton.setObjectName(u"passwordRadioButton")
        self.passwordRadioButton.setGeometry(QRect(10, 130, 121, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.passwordRadioButton.setFont(font2)
        self.passwordRadioButton.setChecked(True)
        self.privateKeyRadioButton = QRadioButton(self.centralwidget)
        self.privateKeyRadioButton.setObjectName(u"privateKeyRadioButton")
        self.privateKeyRadioButton.setGeometry(QRect(10, 170, 121, 41))
        self.privateKeyRadioButton.setFont(font2)
        self.privateKeyPathLineEdit = QLineEdit(self.centralwidget)
        self.privateKeyPathLineEdit.setObjectName(u"privateKeyPathLineEdit")
        self.privateKeyPathLineEdit.setEnabled(False)
        self.privateKeyPathLineEdit.setGeometry(QRect(100, 220, 501, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 220, 71, 16))
        self.label_4.setFont(font2)
        self.privateKeyButton = QPushButton(self.centralwidget)
        self.privateKeyButton.setObjectName(u"privateKeyButton")
        self.privateKeyButton.setEnabled(False)
        self.privateKeyButton.setGeometry(QRect(610, 220, 41, 21))
        self.hostLineEdit = QLineEdit(self.centralwidget)
        self.hostLineEdit.setObjectName(u"hostLineEdit")
        self.hostLineEdit.setGeometry(QRect(110, 10, 531, 31))
        self.conectButton = QPushButton(self.centralwidget)
        self.conectButton.setObjectName(u"conectButton")
        self.conectButton.setGeometry(QRect(530, 260, 61, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.conectButton.setFont(font3)
        self.finishButton = QPushButton(self.centralwidget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(600, 260, 61, 31))
        self.finishButton.setFont(font3)
        self.portLineEdit = QLineEdit(self.centralwidget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setGeometry(QRect(490, 180, 113, 31))
        self.portLabel = QLabel(self.centralwidget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setGeometry(QRect(490, 150, 121, 21))
        CFTConnectWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CFTConnectWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 675, 33))
        CFTConnectWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CFTConnectWindow)
        self.statusbar.setObjectName(u"statusbar")
        CFTConnectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CFTConnectWindow)
        self.passwordRadioButton.toggled.connect(CFTConnectWindow.radioButtonSelected)
        self.privateKeyRadioButton.toggled.connect(CFTConnectWindow.radioButtonSelected)
        self.privateKeyButton.clicked.connect(CFTConnectWindow.pravateKeyButtonClicked)
        self.conectButton.clicked.connect(CFTConnectWindow.connectButtonClicked)
        self.finishButton.clicked.connect(CFTConnectWindow.finishButtoncClicked)

        QMetaObject.connectSlotsByName(CFTConnectWindow)
    # setupUi

    def retranslateUi(self, CFTConnectWindow):
        CFTConnectWindow.setWindowTitle(QCoreApplication.translate("CFTConnectWindow", u"CFT-\u65b0\u3057\u3044\u63a5\u7d9a", None))
        self.label.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30db\u30b9\u30c8\u540d", None))
        self.label_2.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30e6\u30fc\u30b6\u30fc", None))
        self.label_3.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30d1\u30b9\u30ef\u30fc\u30c9", None))
        self.passwordRadioButton.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30d1\u30b9\u30ef\u30fc\u30c9\u8a8d\u8a3c", None))
        self.privateKeyRadioButton.setText(QCoreApplication.translate("CFTConnectWindow", u"\u79d8\u5bc6\u9375\u8a8d\u8a3c", None))
        self.label_4.setText(QCoreApplication.translate("CFTConnectWindow", u"\u79d8\u5bc6\u9375", None))
        self.privateKeyButton.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30fb\u30fb\u30fb", None))
        self.conectButton.setText(QCoreApplication.translate("CFTConnectWindow", u"\u63a5\u7d9a", None))
        self.finishButton.setText(QCoreApplication.translate("CFTConnectWindow", u"\u7d42\u4e86", None))
        self.portLineEdit.setText(QCoreApplication.translate("CFTConnectWindow", u"22", None))
        self.portLabel.setText(QCoreApplication.translate("CFTConnectWindow", u"\u30dd\u30fc\u30c8\u756a\u53f7", None))
    # retranslateUi

