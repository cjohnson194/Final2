# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(1200, 800)
        Welcome.setMinimumSize(QtCore.QSize(1200, 800))
        Welcome.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(Welcome)
        self.centralwidget.setObjectName("centralwidget")
        self.label_top = QtWidgets.QLabel(self.centralwidget)
        self.label_top.setGeometry(QtCore.QRect(230, 100, 911, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_top.setFont(font)
        self.label_top.setObjectName("label_top")
        self.welcomeButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.welcomeButton_login.setGeometry(QtCore.QRect(390, 290, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcomeButton_login.setFont(font)
        self.welcomeButton_login.setObjectName("welcomeButton_login")
        self.welcomeButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.welcomeButton_register.setGeometry(QtCore.QRect(390, 430, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.welcomeButton_register.setFont(font)
        self.welcomeButton_register.setObjectName("welcomeButton_register")
        Welcome.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Welcome)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        Welcome.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Welcome)
        self.statusbar.setObjectName("statusbar")
        Welcome.setStatusBar(self.statusbar)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Welcome"))
        self.label_top.setText(_translate("Welcome", "Sign in or register a new account"))
        self.welcomeButton_login.setText(_translate("Welcome", "Login"))
        self.welcomeButton_register.setText(_translate("Welcome", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome = QtWidgets.QMainWindow()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())