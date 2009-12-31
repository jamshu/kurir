'''
Created on Nov 9, 2009

@author: gumuz
'''
import os, urllib, pickle
from PyQt4 import QtGui, QtCore
from ui.kurir_main_window import Ui_MainWindow
from kurir_accounts import KurirAccountsDialog
from kurir_send import KurirSendDialog
from utils import convert_bytes, get_file_icon

MIME_FORMAT = 'text/uri-list'

class KurirMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.accounts = None
        self.current_account = None
        
        self.load_accounts()
        
        # slots/signals
        self.connect(self, QtCore.SIGNAL("file_list_changed"), self.update_file_status)
        
        
    def load_accounts(self):
        if self.accounts is None:
            try:
                self.accounts = pickle.load(open('accounts.db', 'r'))
            except IOError:
                self.accounts = [{"from_address":"kurir.account@gmail.com",
                                  "username":"kurir.account@gmail.com",
                                  "password":"kuriraccount",
                                  "hostname":"smtp.gmail.com",
                                  "port":587,
                                  "use_auth":True,
                                  "connection":"STARTTLS",
                                  "max_size":25,
                                  "max_size_type": "MB"
                                  }]
            
        self.ui.comboBoxFrom.clear()
        
        current_index = -1
        current_account = self.current_account
        for index, account in enumerate(self.accounts):
            self.ui.comboBoxFrom.addItem(account["from_address"])
        
            if current_account == account:
                current_index = index

        self.ui.comboBoxFrom.setCurrentIndex(current_index)
        
        
        
    def update_file_status(self):
        total_size = file_count = 0
        
        iter = QtGui.QTreeWidgetItemIterator(self.ui.treeWidgetFiles)
        while iter.value(): 
            file_count += 1
            total_size += iter.value().file_info['size']
            iter += 1
            
        self.ui.tabWidget.setTabText(1, "Files (%s)" % (file_count))
        self.ui.statusbar.showMessage("%s files loaded (%s)" % (file_count, convert_bytes(total_size)))
        
    
    def add_files(self, filenames):
        for filename in filenames:
            if not os.path.exists(filename) or not os.path.isfile(filename):
                # file not found, skip
                continue
            
            fstat = os.stat(unicode(filename))
            
            file_info = {'path' : filename,
                         'name': os.path.split(unicode(filename))[-1],
                         'size': fstat.st_size}
            
            twi = QtGui.QTreeWidgetItem()
            twi.file_info = file_info
            twi.setText(0, file_info['name'])
            twi.setToolTip(0, file_info['path'])
            twi.setText(1, convert_bytes(file_info['size']))
            twi.setToolTip(1, "%s bytes" % file_info['size'])
            
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/kurir/%s" % (get_file_icon(file_info['name']))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            twi.setIcon(0, icon)            
            
            self.ui.treeWidgetFiles.addTopLevelItem(twi)
            
        self.emit(QtCore.SIGNAL("file_list_changed"))
        
    # auto-slots
    #
    def closeEvent(self, event):
        """
            Save settings to file on closing.
        """
        btn = QtGui.QMessageBox.question(self, "Question", "Are you sure you want to exit?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if btn == QtGui.QMessageBox.Yes:
            pickle.dump(self.accounts, open("accounts.db", "w"))
            event.accept()
        else:
            event.ignore()
        
        
    def dragEnterEvent(self, event):
        """
            When files are dragged into the window we accept.
        """
        if event.mimeData().hasFormat(MIME_FORMAT):
                event.accept()
        else:
                event.ignore()
                
                
    def dropEvent(self, event):
        """
            When files are dropped into the window,
            add them to the list.
        """
        filenames = []
        for f in str(event.mimeData().data(MIME_FORMAT)).split():
            if f.startswith('file:///'): # strip this, to be sure
                f = f[8:]
            filenames.append(urllib.unquote(f))

        self.add_files(filenames)
        
        # set the current tab to files-tab, in case of drag'n'drop
        self.ui.tabWidget.setCurrentIndex(1)

        
    @QtCore.pyqtSlot(int)
    def on_comboBoxFrom_currentIndexChanged(self, index):
        self.current_account = self.accounts[index]
    
    @QtCore.pyqtSlot()
    def on_actionAccounts_triggered(self):
        ui = KurirAccountsDialog(self)
        self.connect(ui, QtCore.SIGNAL("accounts_changed"), self.load_accounts)
        ui.exec_() 
    
    @QtCore.pyqtSlot()
    def on_treeWidgetFiles_itemSelectionChanged(self):
        is_selected = len(self.ui.treeWidgetFiles.selectedItems()) > 0
        self.ui.toolButtonRemoveFiles.setEnabled(is_selected)
      
      
    @QtCore.pyqtSlot()
    def on_toolButtonRemoveFiles_clicked(self):
        btn = QtGui.QMessageBox.question(self, 
                                         "Question", 
                                         "Are you sure you want to remove the selected files?", 
                                         QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if btn == QtGui.QMessageBox.Yes:
            for twi in self.ui.treeWidgetFiles.selectedItems():
                self.ui.treeWidgetFiles.removeItemWidget(twi, 0)
            del twi # remove last reference
            self.emit(QtCore.SIGNAL("file_list_changed"))
          
                
    @QtCore.pyqtSlot()
    def on_toolButtonAddFiles_clicked(self):
        filenames = QtGui.QFileDialog.getOpenFileNames(self, 
                                                       'Open files', 
                                                       'c:\\')
        self.add_files(filenames)
            
            
    @QtCore.pyqtSlot()
    def on_toolButtonAddFolder_clicked(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self, 
                                                        'Open folder')
        if folder:
            filenames = [os.path.join(str(folder), filename) 
                         for filename in os.listdir(folder)]
            
            self.add_files(filenames)
    
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
            iter = QtGui.QTreeWidgetItemIterator(self.ui.treeWidgetFiles)
            while iter.value():
                file_info = iter.value().file_info
                if file_info["size"] > self.current_account["max_size_bytes"]:
                    QtGui.QMessageBox.critical(self, 
                                               "Error", 
                                               "'%s' larger than %s %s" % (file_info["name"], self.current_account["max_size"], self.current_account["max_size_type"]))
                    return False
                iter += 1
                
            return True
    
    @QtCore.pyqtSlot()
    def on_actionSend_triggered(self, checked=None):
        if self.validate():
            files = []
            
            iter = QtGui.QTreeWidgetItemIterator(self.ui.treeWidgetFiles)
            while iter.value():
                files.append(iter.value().file_info)
                iter += 1
                
            if not len(files):
                QtGui.QMessageBox.critical(self, "Error", "No files selected!")
                return
            
            to_address = str(self.ui.lineEditTo.text())
            subject = str(self.ui.lineEditSubject.text())
            body = str(self.ui.plainTextEditBody.toPlainText())
            
            ui = KurirSendDialog(self, self.current_account, to_address, subject, body, files)
            ui.exec_() 
    
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self, checked=None):
        self.close()
