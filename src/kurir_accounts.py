'''
Created on Dec 29, 2009

@author: gumuz
'''
from PyQt4 import QtGui, QtCore
from ui.kurir_accounts_dialog import Ui_AccountsDialog

MULTIPLIERS = {"MB":1048576, "KB":1024}
CONNECTIONS = ["None", "STARTTLS"]
SIZES = ["KB", "MB"]
PRESETS = [{"hostname":"smtp.gmail.com",
           "port":587,
           "max_size":25,
           "max_size_type":"MB",
           "use_auth":True,
           "connection":"STARTTLS"},
          {"hostname":"smtp.live.com",
           "port":587,
           "max_size":10,
           "max_size_type":"MB",
           "use_auth":True,
           "connection":"STARTTLS"},]

class KurirAccountsDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AccountsDialog()
        self.ui.setupUi(self)
        
        self.accounts = parent.accounts
        
        for conn in CONNECTIONS:
            self.ui.comboBoxConnection.addItem(conn)
            
        for size in SIZES:
            self.ui.comboBoxMaxSizeType.addItem(size)
            
        for preset in PRESETS:
            self.ui.comboBoxHostname.addItem(preset["hostname"])
        self.ui.comboBoxHostname.setCurrentIndex(-1)
        
        self.load_accounts()
        
        
    def load_accounts(self):
        self.ui.treeWidgetAccounts.clear()
        for account in self.accounts:
            twi = QtGui.QTreeWidgetItem()
            twi.account = account
            twi.setText(0, account['from_address'])
            twi.setText(1, account['hostname'])
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/kurir/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            twi.setIcon(0, icon)            
            
            self.ui.treeWidgetAccounts.addTopLevelItem(twi)
            
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def validate(self):
        from validator import Validator
        
        v = Validator(self.ui)
        errors = v.validate()
        
        if errors:
            obj, msg = errors[0]
            QtGui.QMessageBox.critical(self, "Error", msg)
            try:
                obj.setFocus()
                obj.selectAll()
            except: pass
            return False
        else:
            return True
            
            
    def edit_account(self):
        if self.current_account:
            self.ui.lineEditFromAddress.setText(self.current_account["from_address"])
            self.ui.comboBoxHostname.setEditText(self.current_account["hostname"])
            self.ui.lineEditPort.setText(str(self.current_account["port"]))
            self.ui.lineEditMaxSize.setText(str(self.current_account["max_size"]))
            self.ui.comboBoxMaxSizeType.setCurrentIndex(SIZES.index(self.current_account["max_size_type"]))
            self.ui.checkBoxUsernamePw.setChecked(self.current_account["use_auth"])
            self.ui.comboBoxConnection.setCurrentIndex(CONNECTIONS.index(self.current_account["connection"]))
            self.ui.lineEditUsername.setText(self.current_account["username"])
            self.ui.lineEditPassword.setText(self.current_account["password"])
        else:
            self.ui.lineEditFromAddress.setText("")
            self.ui.comboBoxHostname.setEditText("")
            self.ui.lineEditPort.setText("")
            self.ui.lineEditMaxSize.setText("")
            self.ui.comboBoxMaxSizeType.setCurrentIndex(0)
            self.ui.checkBoxUsernamePw.setChecked(False)
            self.ui.comboBoxConnection.setCurrentIndex(0)
            self.ui.lineEditUsername.setText("")
            self.ui.lineEditPassword.setText("")
            
        self.ui.checkBoxShowPw.setChecked(False)
        self.ui.lineEditFromAddress.setFocus()
        self.ui.lineEditFromAddress.selectAll()
        
        self.ui.stackedWidget.setCurrentIndex(1)

    
    @QtCore.pyqtSlot(str)
    def on_comboBoxHostname_currentIndexChanged(self, text):
        for preset in PRESETS:
            if preset["hostname"] == text:
                self.ui.lineEditPort.setText(str(preset["port"]))
                self.ui.lineEditMaxSize.setText(str(preset["max_size"]))
                self.ui.comboBoxMaxSizeType.setCurrentIndex(SIZES.index(preset["max_size_type"]))
                self.ui.checkBoxUsernamePw.setChecked(preset["use_auth"])
                self.ui.comboBoxConnection.setCurrentIndex(CONNECTIONS.index(preset["connection"]))
                
                break
    
    @QtCore.pyqtSlot()
    def on_treeWidgetAccounts_itemSelectionChanged(self):
        is_selected = len(self.ui.treeWidgetAccounts.selectedItems()) > 0
        self.ui.toolButtonEditAccount.setEnabled(is_selected)
        self.ui.toolButtonDeleteAccount.setEnabled(is_selected)
    
    @QtCore.pyqtSlot()
    def on_toolButtonAddAccount_clicked(self):
        self.current_account = None
        self.edit_account()
        
    
    @QtCore.pyqtSlot()
    def on_toolButtonEditAccount_clicked(self):
        twi = self.ui.treeWidgetAccounts.selectedItems()[0]
        self.current_account = twi.account
        self.edit_account()
        
        
    @QtCore.pyqtSlot()
    def on_toolButtonDeleteAccount_clicked(self):
        btn = QtGui.QMessageBox.question(self, 
                                         "Question", 
                                         "Are you sure you want to delete the selected account?", 
                                         QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        
        if btn == QtGui.QMessageBox.Yes:
            twi = self.ui.treeWidgetAccounts.selectedItems()[0]
            for index, account in enumerate(self.accounts):
                if account == twi.account:
                    del self.accounts[index]
                    break
            
            self.load_accounts()
            
            self.emit(QtCore.SIGNAL("accounts_changed"))
        
        
    @QtCore.pyqtSlot(bool)
    def on_checkBoxUsernamePw_toggled(self, checked):
        self.ui.labelUsername.setEnabled(checked)
        self.ui.labelPassword.setEnabled(checked)
        self.ui.lineEditUsername.setEnabled(checked)
        self.ui.lineEditPassword.setEnabled(checked)
        self.ui.checkBoxShowPw.setEnabled(checked)
        
        
    @QtCore.pyqtSlot(bool)
    def on_checkBoxShowPw_toggled(self, checked):
        if checked:
            self.ui.lineEditPassword.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.ui.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        
    @QtCore.pyqtSlot()
    def on_toolButtonSave_clicked(self):
        if self.validate():
            if not self.current_account:
                self.current_account = {}
                self.accounts.append(self.current_account)
                
            self.current_account["from_address"] = str(self.ui.lineEditFromAddress.text())
            self.current_account["hostname"] = str(self.ui.comboBoxHostname.currentText())
            self.current_account["port"] = int(self.ui.lineEditPort.text())
            self.current_account["use_auth"] = self.ui.checkBoxUsernamePw.isChecked()
            self.current_account["connection"] = CONNECTIONS[self.ui.comboBoxConnection.currentIndex()]
            self.current_account["username"] = str(self.ui.lineEditUsername.text())
            self.current_account["password"] = str(self.ui.lineEditPassword.text())
            self.current_account["max_size"] = int(self.ui.lineEditMaxSize.text())
            self.current_account["max_size_type"] = SIZES[self.ui.comboBoxMaxSizeType.currentIndex()]
            self.current_account["max_size_bytes"] =  self.current_account["max_size"] \
                                                      * MULTIPLIERS[self.current_account["max_size_type"]]
    
            self.load_accounts()
            
            self.emit(QtCore.SIGNAL("accounts_changed"))
        
    
    @QtCore.pyqtSlot()
    def on_toolButtonCancel_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    @QtCore.pyqtSlot(QtGui.QTreeWidgetItem, int)        
    def on_treeWidgetAccounts_itemDoubleClicked(self, twi, column):
        self.current_account = twi.account
        self.edit_account()