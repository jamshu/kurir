'''
Created on Oct 20, 2009

@author: gumuz
'''


import os
        
from PyQt4.QtCore import *

from kurir_smtp import KurirSMTP, CancelledException
import smtplib

from utils import divide_random, divide_greedy, split_seq
from random import shuffle

class SendThread(QThread):
    def __init__(self, parent, account, package):
        QThread.__init__(self, parent)
        
        self.account = account
        self.package = package

        self.cancelled = False
        
        
        self.connect(parent, SIGNAL("cancel"), self.cancel)
        
    def data_callback(self, timestamp, progress, total):
        self.emit(SIGNAL("transfer_progress"), timestamp, progress, total)
        return not self.cancelled
        
    def cancel(self):
        self.cancelled = True
        
    def status(self, msg):
        self.emit(SIGNAL("status"), msg)
        
    def run(self):
        try:
            self.status("Connecting to %s:%s..." % (self.account.host_name, self.account.port))
            server = KurirSMTP(self.account.host_name, 
                                    self.account.port)
            server.set_debuglevel(1)
            server.callback = self.data_callback
            server.ehlo()
            
            if self.account.security == "STARTTLS":
                self.status("STARTTLS...")
                server.starttls()
                server.ehlo()
            
            if self.account.use_auth:
                self.status("Authenticating %s..." % (self.account.username))
                server.login(self.account.username, self.account.password)
            
            for index, total, msg in self.package.get_messages():
                if self.cancelled:
                    break
                self.status("Sending email %s of %s..." % (index, total))
                server.sendmail(self.account.from_address, 
                                     msg['to'], 
                                     msg.as_string())
            
            self.status("Disconnecting...")
            server.quit()
            self.emit(SIGNAL("done"))
            
        except CancelledException:
            self.emit(SIGNAL("canceled"))
        except smtplib.SMTPAuthenticationError:
            self.emit(SIGNAL("fatal_error"), "Username and password not accepted!")
        except smtplib.SMTPServerDisconnected:
            self.emit(SIGNAL("fatal_error"), "Server got disconnected!")
        except smtplib.SMTPSenderRefused:
            self.emit(SIGNAL("fatal_error"), "Sender refused!")
        except smtplib.SMTPRecipientsRefused:
            self.emit(SIGNAL("fatal_error"), "Recipients refused!")
        except smtplib.SMTPDataError, e:
            self.emit(SIGNAL("fatal_error"), "SMTP data error!\r\n%s:%s" % (e.smtp_code, e.smtp_error))
        except smtplib.SMTPConnectError:
            self.emit(SIGNAL("fatal_error"), "Connect error!")
        except smtplib.SMTPHeloError:
            self.emit(SIGNAL("fatal_error"), "Helo error!")            
        except:
            self.emit(SIGNAL("fatal_error"), "Unknown error!")
            raise