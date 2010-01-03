'''
Created on Dec 29, 2009

@author: gumuz
'''
from PyQt4 import QtGui, QtCore
from ui.kurir_send_dialog import Ui_SendDialog
from send_thread import SendThread
from utils import convert_bytes
import os


class KurirSendDialog(QtGui.QDialog):
    def __init__(self, parent, account, package):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_SendDialog()
        self.ui.setupUi(self)
        
        self.send_thread = SendThread(self, account, package)
        self.history = []
        
        # slots/signals
        self.connect(self.send_thread, QtCore.SIGNAL("transfer_progress"), self.transfer_progress)
        self.connect(self.send_thread, QtCore.SIGNAL("fatal_error"), self.fatal_error)
        self.connect(self.send_thread, QtCore.SIGNAL("canceled"), self.canceled)
        self.connect(self.send_thread, QtCore.SIGNAL("status"), self.status)
        self.connect(self.send_thread, QtCore.SIGNAL("done"), self.finished)
        
        self.send_thread.start()
        
    def finished(self):
        self.send_thread.quit()
        self.send_thread.wait()
        self.ui.labelOverall.setText("Done!")
        self.ui.btnCancelFinish.setText('Close')
        
        
    def status(self, msg):
        self.ui.labelOverall.setText(msg) 
        
    def canceled(self):
        self.send_thread.quit()
        self.send_thread.wait()
        self.ui.labelOverall.setText("Canceled")
        self.ui.btnCancelFinish.setEnabled(True)
        self.ui.btnCancelFinish.setText("Close")
        
    def fatal_error(self, msg):
        QtGui.QMessageBox.critical(self, "Error", msg)   
        self.ui.labelOverall.setText("Sending failed...")
        self.send_thread.quit()
        self.send_thread.wait()
        self.ui.btnCancelFinish.setText("Close")
        
#    def overall_progress(self, filename, progress, total):
#        print "file progress", progress, total
#        
#        self.history = []
#        
#        if progress % 2:
#            norm_progress = (progress + 1)/2
#        else:
#            norm_progress = progress / 2
#        
#        self.ui.labelOverall.setText("Sending %s [%s of %s]" % (os.path.split(filename)[-1], norm_progress, total/2))
#        self.ui.progressOverall.setMaximum(total)
#        self.ui.progressOverall.setValue(progress)
#        
#        if progress == total:
#            self.send_thread.quit()
#            self.send_thread.wait()
#            self.ui.btnCancelFinish.setText('Close')
        
    
    
    def transfer_progress(self, timestamp, progress, total):
        print "send progress", timestamp, progress, total
        self.history.append((timestamp, progress))
        
        # calculate speed
        history = self.history[-500:]
        time_diff = history[-1][0] - history[0][0]
        progress_diff = history[-1][1] - history[0][1]
        if progress == total:
            self.history = []
        
        print "timediff", time_diff, progress_diff
        
        if time_diff:
            speed = progress_diff/time_diff
        else:
            speed = progress_diff
        
        
#        self.ui.labelTransfer.setText("Transferred %s of %s (%s/s)" % (convert_bytes(progress), convert_bytes(total), convert_bytes(speed)))
        self.ui.progressTransfer.setMaximum(total)
        self.ui.progressTransfer.setValue(progress)
        self.setWindowTitle("%s/s" % (convert_bytes(speed)))
        
    @QtCore.pyqtSlot()
    def on_btnCancelFinish_clicked(self):
        if self.ui.btnCancelFinish.text() == 'Close':
            self.accept()
        else:
            btn = QtGui.QMessageBox.question(self, 
                                             "Question", "Are you sure you want to cancel this transfer?", 
                                             QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            if btn == QtGui.QMessageBox.Yes:
                self.emit(QtCore.SIGNAL("cancel"))
                self.status("Cancelling...")
                self.ui.btnCancelFinish.setEnabled(False)     