# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\kurir_send.ui'
#
# Created: Thu Dec 31 01:26:55 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SendDialog(object):
    def setupUi(self, SendDialog):
        SendDialog.setObjectName("SendDialog")
        SendDialog.resize(481, 162)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/kurir/email_go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SendDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(SendDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelOverall = QtGui.QLabel(SendDialog)
        self.labelOverall.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOverall.setObjectName("labelOverall")
        self.verticalLayout.addWidget(self.labelOverall)
        self.progressOverall = QtGui.QProgressBar(SendDialog)
        self.progressOverall.setProperty("value", 0)
        self.progressOverall.setObjectName("progressOverall")
        self.verticalLayout.addWidget(self.progressOverall)
        self.labelTransfer = QtGui.QLabel(SendDialog)
        self.labelTransfer.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTransfer.setObjectName("labelTransfer")
        self.verticalLayout.addWidget(self.labelTransfer)
        self.progressTransfer = QtGui.QProgressBar(SendDialog)
        self.progressTransfer.setProperty("value", 0)
        self.progressTransfer.setObjectName("progressTransfer")
        self.verticalLayout.addWidget(self.progressTransfer)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnCancelFinish = QtGui.QPushButton(SendDialog)
        self.btnCancelFinish.setEnabled(True)
        self.btnCancelFinish.setObjectName("btnCancelFinish")
        self.horizontalLayout_2.addWidget(self.btnCancelFinish)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SendDialog)
        QtCore.QMetaObject.connectSlotsByName(SendDialog)

    def retranslateUi(self, SendDialog):
        SendDialog.setWindowTitle(QtGui.QApplication.translate("SendDialog", "Sending...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOverall.setText(QtGui.QApplication.translate("SendDialog", "Overall progress...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTransfer.setText(QtGui.QApplication.translate("SendDialog", "File transfer progress...", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancelFinish.setText(QtGui.QApplication.translate("SendDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import kurir_rc
