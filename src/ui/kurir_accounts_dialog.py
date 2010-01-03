# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\kurir_accounts.ui'
#
# Created: Sun Jan 03 19:35:46 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AccountsDialog(object):
    def setupUi(self, AccountsDialog):
        AccountsDialog.setObjectName("AccountsDialog")
        AccountsDialog.resize(344, 286)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/kurir/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AccountsDialog.setWindowIcon(icon)
        self.horizontalLayout = QtGui.QHBoxLayout(AccountsDialog)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtGui.QStackedWidget(AccountsDialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButtonAddAccount = QtGui.QToolButton(self.page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/kurir/user_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonAddAccount.setIcon(icon1)
        self.toolButtonAddAccount.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButtonAddAccount.setAutoRaise(True)
        self.toolButtonAddAccount.setObjectName("toolButtonAddAccount")
        self.horizontalLayout_2.addWidget(self.toolButtonAddAccount)
        self.toolButtonEditAccount = QtGui.QToolButton(self.page)
        self.toolButtonEditAccount.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/kurir/user_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonEditAccount.setIcon(icon2)
        self.toolButtonEditAccount.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButtonEditAccount.setAutoRaise(True)
        self.toolButtonEditAccount.setObjectName("toolButtonEditAccount")
        self.horizontalLayout_2.addWidget(self.toolButtonEditAccount)
        self.toolButtonDeleteAccount = QtGui.QToolButton(self.page)
        self.toolButtonDeleteAccount.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/kurir/user_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonDeleteAccount.setIcon(icon3)
        self.toolButtonDeleteAccount.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButtonDeleteAccount.setAutoRaise(True)
        self.toolButtonDeleteAccount.setObjectName("toolButtonDeleteAccount")
        self.horizontalLayout_2.addWidget(self.toolButtonDeleteAccount)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeWidgetAccounts = QtGui.QTreeWidget(self.page)
        self.treeWidgetAccounts.setRootIsDecorated(False)
        self.treeWidgetAccounts.setObjectName("treeWidgetAccounts")
        self.treeWidgetAccounts.header().setDefaultSectionSize(80)
        self.verticalLayout.addWidget(self.treeWidgetAccounts)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(self.page_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 2)
        self.from_address = QtGui.QLineEdit(self.groupBox)
        self.from_address.setProperty("is_required", True)
        self.from_address.setProperty("is_email", True)
        self.from_address.setObjectName("from_address")
        self.gridLayout.addWidget(self.from_address, 0, 2, 1, 5)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 2)
        self.max_size = QtGui.QLineEdit(self.groupBox)
        self.max_size.setProperty("is_required", True)
        self.max_size.setProperty("is_integer", True)
        self.max_size.setObjectName("max_size")
        self.gridLayout.addWidget(self.max_size, 3, 2, 1, 2)
        self.port = QtGui.QLineEdit(self.groupBox)
        self.port.setProperty("is_required", True)
        self.port.setProperty("is_integer", True)
        self.port.setProperty("min_int", 1)
        self.port.setProperty("max_int", 1000000)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 6, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 2)
        self.password = QtGui.QLineEdit(self.groupBox)
        self.password.setEnabled(False)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 7, 2, 1, 5)
        self.security = QtGui.QComboBox(self.groupBox)
        self.security.setObjectName("security")
        self.security.addItem("")
        self.security.addItem("")
        self.gridLayout.addWidget(self.security, 9, 2, 1, 2)
        self.use_auth = QtGui.QCheckBox(self.groupBox)
        self.use_auth.setObjectName("use_auth")
        self.gridLayout.addWidget(self.use_auth, 5, 0, 1, 3)
        self.labelUsername = QtGui.QLabel(self.groupBox)
        self.labelUsername.setEnabled(False)
        self.labelUsername.setObjectName("labelUsername")
        self.gridLayout.addWidget(self.labelUsername, 6, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.labelPassword = QtGui.QLabel(self.groupBox)
        self.labelPassword.setEnabled(False)
        self.labelPassword.setObjectName("labelPassword")
        self.gridLayout.addWidget(self.labelPassword, 7, 1, 1, 1)
        self.username = QtGui.QLineEdit(self.groupBox)
        self.username.setEnabled(False)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 6, 2, 1, 5)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)
        self.max_size_type = QtGui.QComboBox(self.groupBox)
        self.max_size_type.setObjectName("max_size_type")
        self.max_size_type.addItem("")
        self.max_size_type.addItem("")
        self.gridLayout.addWidget(self.max_size_type, 3, 4, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 6, 1, 1)
        self.checkBoxShowPw = QtGui.QCheckBox(self.groupBox)
        self.checkBoxShowPw.setEnabled(False)
        self.checkBoxShowPw.setObjectName("checkBoxShowPw")
        self.gridLayout.addWidget(self.checkBoxShowPw, 8, 2, 1, 3)
        self.host_name = QtGui.QLineEdit(self.groupBox)
        self.host_name.setObjectName("host_name")
        self.gridLayout.addWidget(self.host_name, 1, 2, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.toolButtonSave = QtGui.QToolButton(self.page_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/kurir/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonSave.setIcon(icon4)
        self.toolButtonSave.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButtonSave.setAutoRaise(True)
        self.toolButtonSave.setObjectName("toolButtonSave")
        self.horizontalLayout_3.addWidget(self.toolButtonSave)
        self.toolButtonCancel = QtGui.QToolButton(self.page_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/kurir/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonCancel.setIcon(icon5)
        self.toolButtonCancel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButtonCancel.setAutoRaise(True)
        self.toolButtonCancel.setObjectName("toolButtonCancel")
        self.horizontalLayout_3.addWidget(self.toolButtonCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.label_6.setBuddy(self.from_address)
        self.label_8.setBuddy(self.max_size)
        self.label_9.setBuddy(self.security)
        self.labelUsername.setBuddy(self.username)
        self.labelPassword.setBuddy(self.password)
        self.label_7.setBuddy(self.port)

        self.retranslateUi(AccountsDialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AccountsDialog)
        AccountsDialog.setTabOrder(self.from_address, self.port)
        AccountsDialog.setTabOrder(self.port, self.max_size)
        AccountsDialog.setTabOrder(self.max_size, self.max_size_type)
        AccountsDialog.setTabOrder(self.max_size_type, self.use_auth)
        AccountsDialog.setTabOrder(self.use_auth, self.username)
        AccountsDialog.setTabOrder(self.username, self.password)
        AccountsDialog.setTabOrder(self.password, self.checkBoxShowPw)
        AccountsDialog.setTabOrder(self.checkBoxShowPw, self.security)
        AccountsDialog.setTabOrder(self.security, self.toolButtonSave)
        AccountsDialog.setTabOrder(self.toolButtonSave, self.toolButtonCancel)
        AccountsDialog.setTabOrder(self.toolButtonCancel, self.toolButtonDeleteAccount)
        AccountsDialog.setTabOrder(self.toolButtonDeleteAccount, self.toolButtonAddAccount)
        AccountsDialog.setTabOrder(self.toolButtonAddAccount, self.toolButtonEditAccount)
        AccountsDialog.setTabOrder(self.toolButtonEditAccount, self.treeWidgetAccounts)

    def retranslateUi(self, AccountsDialog):
        AccountsDialog.setWindowTitle(QtGui.QApplication.translate("AccountsDialog", "Accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonAddAccount.setText(QtGui.QApplication.translate("AccountsDialog", "Add account", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonEditAccount.setText(QtGui.QApplication.translate("AccountsDialog", "Edit account", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonDeleteAccount.setText(QtGui.QApplication.translate("AccountsDialog", "Delete account", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetAccounts.headerItem().setText(0, QtGui.QApplication.translate("AccountsDialog", "From", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetAccounts.headerItem().setText(1, QtGui.QApplication.translate("AccountsDialog", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AccountsDialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AccountsDialog", "From address:", None, QtGui.QApplication.UnicodeUTF8))
        self.from_address.setToolTip(QtGui.QApplication.translate("AccountsDialog", "From address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AccountsDialog", "Hostname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AccountsDialog", "Max size:", None, QtGui.QApplication.UnicodeUTF8))
        self.max_size.setToolTip(QtGui.QApplication.translate("AccountsDialog", "Maximum size", None, QtGui.QApplication.UnicodeUTF8))
        self.port.setToolTip(QtGui.QApplication.translate("AccountsDialog", "Port number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("AccountsDialog", "Security:", None, QtGui.QApplication.UnicodeUTF8))
        self.security.setItemText(0, QtGui.QApplication.translate("AccountsDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.security.setItemText(1, QtGui.QApplication.translate("AccountsDialog", "STARTTLS", None, QtGui.QApplication.UnicodeUTF8))
        self.use_auth.setText(QtGui.QApplication.translate("AccountsDialog", "Use name & password", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUsername.setText(QtGui.QApplication.translate("AccountsDialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPassword.setText(QtGui.QApplication.translate("AccountsDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AccountsDialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.max_size_type.setItemText(0, QtGui.QApplication.translate("AccountsDialog", "KB", None, QtGui.QApplication.UnicodeUTF8))
        self.max_size_type.setItemText(1, QtGui.QApplication.translate("AccountsDialog", "MB", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowPw.setText(QtGui.QApplication.translate("AccountsDialog", "Show password", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonSave.setText(QtGui.QApplication.translate("AccountsDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonCancel.setText(QtGui.QApplication.translate("AccountsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import kurir_rc