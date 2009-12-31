'''
Created on Oct 20, 2009

@author: gumuz
'''

from smtplib import SMTP, quotedata, CRLF
from sys import stderr
from time import time

class CancelledException(Exception): pass

class KurirSMTP(SMTP):        
    def data(self,msg):
        """SMTP 'DATA' command -- sends message data to server.

        Automatically quotes lines beginning with a period per rfc821.
        Raises SMTPDataError if there is an unexpected reply to the
        DATA command; the return value from this method is the final
        response code received when the all data is sent.
        """
        self.putcmd("data")
        (code,repl)=self.getreply()
        if self.debuglevel >0 : print>>stderr, "data:", (code,repl)
        if code != 354:
            raise SMTPDataError(code,repl)
        else:
            q = quotedata(msg)
            if q[-2:] != CRLF:
                q = q + CRLF
            q = q + "." + CRLF
            
            # begin chunked sent code
            chunk_size = 2048
            bytes_sent = 0
            
            while bytes_sent != len(q):
                chunk = q[bytes_sent:bytes_sent+chunk_size]
                self.send(chunk)
                bytes_sent += len(chunk)
                if hasattr(self, "callback"):
                    if not self.callback(time(), bytes_sent, len(q)):
                        raise CancelledException
            
            # end chunked sent code
            
            (code,msg)=self.getreply()
            if self.debuglevel >0 : print>>stderr, "data:", (code,msg)
            return (code,msg)