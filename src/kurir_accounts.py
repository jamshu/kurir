'''
Created on Dec 29, 2009

@author: gumuz
'''
from PyQt4 import QtGui, QtCore
from ui.kurir_accounts_dialog import Ui_AccountsDialog
from account import KurirAccount, PRESETS
from form import Form
from fields import CharField, IntegerField, BooleanField

class AccountForm(Form):
    from_address = CharField()
    host_name = CharField()
    port = IntegerField()
    max_size = IntegerField()
    max_size_type = CharField()
    use_auth = BooleanField(required=False)
    username = CharField(required=False)
    password = CharField(required=False)
    security = CharField()


class KurirAccountsDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_AccountsDialog()
        self.ui.setupUi(self)
        
        self.accounts = parent.accounts
        
        self.load_accounts()
        
        
    def load_accounts(self):
        self.ui.treeWidgetAccounts.clear()
        for account in self.accounts:
            twi = QtGui.QTreeWidgetItem()
            twi.account = account
            twi.setText(0, account.from_address)
            twi.setText(1, account.host_name)
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/kurir/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            twi.setIcon(0, icon)            
            
            self.ui.treeWidgetAccounts.addTopLevelItem(twi)
            
        self.ui.stackedWidget.setCurrentIndex(0)
            
            
    def edit_account(self):
        form = AccountForm(initial_data=self.current_account or KurirAccount())
        form.display(target=self.ui)
        self.ui.checkBoxShowPw.setChecked(False)
        self.ui.from_address.setFocus()
        self.ui.from_address.selectAll()
        
        self.ui.stackedWidget.setCurrentIndex(1)

    
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
    def on_from_address_editingFinished(self):
        if self.current_account is None: 
            from_address = str(self.ui.from_address.text())
            for preset in PRESETS:
                for domain in preset["domains"]:
                    if from_address.endswith(domain):
                        btn = QtGui.QMessageBox.question(self, 
                                             "Question", 
                                             "Do you want to load the preset settings for %s %s?" % (domain, self.current_account), 
                                             QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            
                        if btn == QtGui.QMessageBox.Yes:
                            tmp = {"from_address":from_address,
                                   "username":from_address,
                                   "password":""}
                            tmp.update(preset)
                            form = AccountForm(initial_data=tmp)
                            form.display(self.ui)
                            
                        return
        
        
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
    def on_use_auth_toggled(self, checked):
        self.ui.username.setEnabled(checked)
        self.ui.password.setEnabled(checked)
        self.ui.labelUsername.setEnabled(checked)
        self.ui.labelPassword.setEnabled(checked)
        self.ui.checkBoxShowPw.setEnabled(checked)
        
        
    @QtCore.pyqtSlot(bool)
    def on_checkBoxShowPw_toggled(self, checked):
        if checked:
            self.ui.password.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QtGui.QLineEdit.Password)
        
    @QtCore.pyqtSlot()
    def on_toolButtonSave_clicked(self):
        form = AccountForm()
        form.load(target=self.ui)
        for name, msg in form.validate():
            QtGui.QMessageBox.critical(self, name, msg)
            try:
                attr = getattr(self.ui, name)
                attr.setFocus()
                attr.selectAll()
            except: pass
            return
        
        if not self.current_account:
            self.current_account = KurirAccount()
            self.accounts.append(self.current_account)

        for key, value in form.cleaned_data.items():
            if hasattr(self.current_account, key):
                setattr(self.current_account, key, value)
        
        self.load_accounts()
        
        self.emit(QtCore.SIGNAL("accounts_changed"))
        
    
    @QtCore.pyqtSlot()
    def on_toolButtonCancel_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    @QtCore.pyqtSlot(QtGui.QTreeWidgetItem, int)        
    def on_treeWidgetAccounts_itemDoubleClicked(self, twi, column):
        self.current_account = twi.account
        self.edit_account()