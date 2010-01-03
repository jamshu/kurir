'''
Created on Jan 2, 2010

@author: gumuz
'''


CONNECTION_TYPES = ["None", "STARTTLS"]
SIZES = {"KB":1024, "MB":1048576}
PRESETS = [{"domains":["gmail.com"],
            "host_name":"smtp.gmail.com",
           "port":587,
           "max_size":25,
           "max_size_type":"MB",
           "use_auth":True,
           "security":"STARTTLS"},
          {"domains":["hotmail.com", "live.com"],
           "host_name":"smtp.live.com",
           "port":587,
           "max_size":10,
           "max_size_type":"MB",
           "use_auth":True,
           "security":"STARTTLS"}, ]

class KurirAccount(object):
    def __init__(self):
        self.from_address = ""
        self.host_name, self.port = "", 25
        self.max_size, self.max_size_type = 2, "MB"
        self.use_auth, self.security = False, "None"
        self.username, self.password = "", ""

        
    def get_max_size_bytes(self):
        return self.max_size * SIZES[self.max_size_type]
    max_size_bytes = property(get_max_size_bytes)
