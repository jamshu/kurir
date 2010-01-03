'''
Created on Dec 31, 2009

@author: gumuz
'''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders


class KurirPackage(object):
    def __init__(self, from_address, to_address, subject, body, max_size, 
                 add_summary=True, attachments=[]):
        """
            Msg
        """
        self.from_address, self.to_address = from_address, to_address
        self.subject, self.body = subject, body
        self.max_size, self.add_summary =  max_size, add_summary
        self.attachments = attachments
        
    def get_messages(self, group=False):
        file_groups = []
        if group:
            pass
        else:
            for attachment in self.attachments:
                file_groups.append((attachment,))
                
        if self.add_summary:
            summary = ["--"*30]
            for group_index, file_group in enumerate(file_groups):
                summary += ["(%s/%s) - %s files\r\n" % (group_index+1, len(file_groups), len(file_group))]
                for file_index, file_info in enumerate(file_group):
                    summary += ["%s. %s (%s)" % (file_index+1, attachment.name, attachment.size)]
                summary += ["\r\n"]
            self.body += "\r\n\r\n%s" % ("\r\n".join(summary))
                
        for group_index, file_group in enumerate(file_groups):
            msg = MIMEMultipart()
            msg['subject'] = "[Kurir] %s [%s/%s]" % (self.subject, group_index+1, len(file_groups))
            msg['to'] = self.to_address
#                
            msg.attach(MIMEText(self.body))
            
            for file_index, attachment in enumerate(file_group):
                    filepart = MIMEBase('application', "octet-stream")
                    filepart.set_payload(open(attachment.path,"rb").read())
                    Encoders.encode_base64(filepart)
                    filepart.add_header('Content-Disposition', 'attachment; filename="%s"' % attachment.name.encode("utf-8"))
                    msg.attach(filepart)
                    

            yield group_index+1, len(file_groups), msg
        
        
        