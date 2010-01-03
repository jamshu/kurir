'''
Created on Jan 3, 2010

@author: gumuz
'''
import os


class KurirAttachment(object):
    def __init__(self, path):
        fstat = os.stat(path)
        
        self.path = path
        self.name = os.path.split(path)[-1]
        self.size = fstat.st_size
        