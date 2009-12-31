'''
Created on Oct 20, 2009

@author: gumuz
'''

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import os
        
from PyQt4.QtCore import *

from kurir_smtp import KurirSMTP, CancelledException
import smtplib

from utils import divide_random, divide_greedy, split_seq
from random import shuffle

class SendThread(QThread):
    def __init__(self, parent, account, to_address, subject, body, files):
        QThread.__init__(self, parent)
        
        self.account = account
        self.to_addres = to_address
        self.subject = subject
        self.body = body

        self.cancelled = False
        self.files = files
        
        
        self.connect(parent, SIGNAL("cancel"), self.cancel)
        
    def data_callback(self, timestamp, progress, total):
        self.emit(SIGNAL("transfer_progress"), timestamp, progress, total)
        return not self.cancelled
        
    def cancel(self):
        self.cancelled = True
        
    def status_update(self, msg):
        self.emit(SIGNAL("status_update"), msg)
        
    def run(self):
        try:
            self.status_update("Connecting to smtp.gmail.com...")
            self.server = KurirSMTP(self.account["hostname"], 
                                    self.account["port"])
            self.server.set_debuglevel(1)
            self.server.callback = self.data_callback
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            
            self.status_update("Authenticating...")
            self.server.login(self.account["username"], self.account["password"])
            
            self.status_update("Caluculating email size...")
            try1 = divide_random(self.files)
            try2 = divide_greedy(self.files)
            
            if len(try1) < len(try2):
                self.parts = try1
            else:
                self.parts = try2
            
            for mail_index, part in enumerate(self.parts):
                self.emit(SIGNAL("overall_progress"), "", (mail_index*2)+1, len(self.parts)*2)    
                
                msg = MIMEMultipart()
                msg['subject'] = "[Kurir] %s [%s/%s]" % (self.subject, mail_index+1, len(self.parts))
                msg['to'] = self.to_addres
                
                msg.attach(MIMEText("These files are sent to you using Kurir!"))
                
                for file_index, file_info in enumerate(part):
                    self.status_update("Encoding %s [%s/%s]..." % (file_info['name'], file_index+1, len(part)))
                    attachment = MIMEBase('application', "octet-stream")
                    attachment.set_payload( open(file_info['path'],"rb").read() )
                    Encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % file_info['name'].encode("utf-8"))
                    msg.attach(attachment)
                print
                
                self.status_update("Sending email [%s/%s]..." % (mail_index+1, len(self.parts)))
                self.server.sendmail(self.account["from_address"], self.to_addres.split(','), msg.as_string())
                
                self.emit(SIGNAL("overall_progress"), "", (mail_index*2)+2, len(self.parts)*2)
                
            self.status_update("Disconnecting from smtp.gmail.com...")
            self.server.quit()            
            self.status_update("Done!")
        
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