# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Loader(object):
    def setupUi(self, Loader):
        Loader.setObjectName("Loader")
        Loader.resize(340, 219)
        self.frame_login = QtWidgets.QFrame(Loader)
        self.frame_login.setGeometry(QtCore.QRect(10, 30, 321, 141))
        self.frame_login.setStyleSheet("QFrame {\n"
"background: rgb(40, 40, 40);\n"
"color:  rgb(255, 255, 255)\n"
"}")
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")
        self.lineEdit_username = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_username.setGeometry(QtCore.QRect(10, 30, 301, 20))
        self.lineEdit_username.setStyleSheet("QLineEdit {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_username = QtWidgets.QLabel(self.frame_login)
        self.label_username.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label_username.setObjectName("label_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_password.setGeometry(QtCore.QRect(10, 70, 301, 20))
        self.lineEdit_password.setAutoFillBackground(False)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setDragEnabled(False)
        self.lineEdit_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_password = QtWidgets.QLabel(self.frame_login)
        self.label_password.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_password.setObjectName("label_password")
        self.button_login = QtWidgets.QPushButton(self.frame_login)
        self.button_login.setGeometry(QtCore.QRect(230, 100, 71, 23))
        self.button_login.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_login.setObjectName("button_login")
        self.button_registration_menu = QtWidgets.QPushButton(self.frame_login)
        self.button_registration_menu.setGeometry(QtCore.QRect(140, 100, 81, 23))
        self.button_registration_menu.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_registration_menu.setFlat(True)
        self.button_registration_menu.setObjectName("button_registration_menu")
        self.frame_topbar = QtWidgets.QFrame(Loader)
        self.frame_topbar.setGeometry(QtCore.QRect(10, 10, 321, 21))
        self.frame_topbar.setStyleSheet("QFrame {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.frame_topbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_topbar.setObjectName("frame_topbar")
        self.label_programm_name = QtWidgets.QLabel(self.frame_topbar)
        self.label_programm_name.setGeometry(QtCore.QRect(6, 1, 151, 21))
        self.label_programm_name.setObjectName("label_programm_name")
        self.button_close = QtWidgets.QPushButton(self.frame_topbar)
        self.button_close.setGeometry(QtCore.QRect(289, 0, 31, 23))
        self.button_close.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_close.setFlat(True)
        self.button_close.setObjectName("button_close")
        self.button_hide = QtWidgets.QPushButton(self.frame_topbar)
        self.button_hide.setGeometry(QtCore.QRect(259, 0, 31, 21))
        self.button_hide.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_hide.setFlat(True)
        self.button_hide.setObjectName("button_hide")
        self.frame_register = QtWidgets.QFrame(Loader)
        self.frame_register.setEnabled(True)
        self.frame_register.setGeometry(QtCore.QRect(10, 30, 321, 181))
        self.frame_register.setStyleSheet("QFrame {\n"
"background: rgb(40,40,40);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.frame_register.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_register.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_register.setObjectName("frame_register")
        self.lineEdit_reg_username = QtWidgets.QLineEdit(self.frame_register)
        self.lineEdit_reg_username.setGeometry(QtCore.QRect(10, 30, 301, 20))
        self.lineEdit_reg_username.setStyleSheet("QLineEdit {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.lineEdit_reg_username.setText("")
        self.lineEdit_reg_username.setObjectName("lineEdit_reg_username")
        self.lineEdit_reg_password = QtWidgets.QLineEdit(self.frame_register)
        self.lineEdit_reg_password.setGeometry(QtCore.QRect(10, 70, 301, 20))
        self.lineEdit_reg_password.setAutoFillBackground(False)
        self.lineEdit_reg_password.setStyleSheet("QLineEdit {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.lineEdit_reg_password.setInputMask("")
        self.lineEdit_reg_password.setText("")
        self.lineEdit_reg_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_reg_password.setDragEnabled(False)
        self.lineEdit_reg_password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_reg_password.setObjectName("lineEdit_reg_password")
        self.label_username_2 = QtWidgets.QLabel(self.frame_register)
        self.label_username_2.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label_username_2.setObjectName("label_username_2")
        self.label_password_2 = QtWidgets.QLabel(self.frame_register)
        self.label_password_2.setGeometry(QtCore.QRect(10, 50, 151, 16))
        self.label_password_2.setObjectName("label_password_2")
        self.lineEdit_reg_key = QtWidgets.QLineEdit(self.frame_register)
        self.lineEdit_reg_key.setGeometry(QtCore.QRect(10, 110, 251, 20))
        self.lineEdit_reg_key.setAutoFillBackground(False)
        self.lineEdit_reg_key.setStyleSheet("QLineEdit {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.lineEdit_reg_key.setInputMask("")
        self.lineEdit_reg_key.setText("")
        self.lineEdit_reg_key.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_reg_key.setDragEnabled(False)
        self.lineEdit_reg_key.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_reg_key.setObjectName("lineEdit_reg_key")
        self.label_key = QtWidgets.QLabel(self.frame_register)
        self.label_key.setGeometry(QtCore.QRect(10, 90, 151, 16))
        self.label_key.setObjectName("label_key")
        self.button_registration = QtWidgets.QPushButton(self.frame_register)
        self.button_registration.setGeometry(QtCore.QRect(220, 140, 81, 23))
        self.button_registration.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_registration.setObjectName("button_registration")
        self.button_back = QtWidgets.QPushButton(self.frame_register)
        self.button_back.setGeometry(QtCore.QRect(10, 140, 51, 23))
        self.button_back.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.button_getkey = QtWidgets.QPushButton(self.frame_register)
        self.button_getkey.setGeometry(QtCore.QRect(270, 110, 41, 21))
        self.button_getkey.setStyleSheet("QPushButton {\n"
"background: rgb(60, 60, 60);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.button_getkey.setFlat(True)
        self.button_getkey.setObjectName("button_getkey")

        self.retranslateUi(Loader)
        QtCore.QMetaObject.connectSlotsByName(Loader)

    def retranslateUi(self, Loader):
        _translate = QtCore.QCoreApplication.translate
        Loader.setWindowTitle(_translate("Loader", "Form"))
        self.label_username.setText(_translate("Loader", "Username"))
        self.label_password.setText(_translate("Loader", "Password"))
        self.button_login.setText(_translate("Loader", "Login"))
        self.button_registration_menu.setText(_translate("Loader", "Registration"))
        self.label_programm_name.setText(_translate("Loader", "Simple PyLoader @firocore"))
        self.button_close.setText(_translate("Loader", "x"))
        self.button_hide.setText(_translate("Loader", "_"))
        self.label_username_2.setText(_translate("Loader", "Username"))
        self.label_password_2.setText(_translate("Loader", "Password"))
        self.label_key.setText(_translate("Loader", "Key"))
        self.button_registration.setText(_translate("Loader", "Registration"))
        self.button_back.setText(_translate("Loader", "<- Back"))
        self.button_getkey.setText(_translate("Loader", "Get"))
