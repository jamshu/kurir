'''
Created on Dec 30, 2009

@author: gumuz
'''
from PyQt4 import QtGui
import re

email_re = re.compile(
            r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
            r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
            r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain


def is_email(value):
    if email_re.match(value.strip()):
        return True
    else:
        False

def is_required(value):
    if not str(value).strip():
        return False
    else:
        return True

def is_integer(value):
    try:
        int(value)
    except:
        return False
    
    return True
    
def int_min(value, minimum):
    try:
        assert(int(value) >= minimum)
    except:
        return False
    
    return True

def int_max(value, maximum):
    try:
        assert(int(value) <= maximum)
    except:
        return False
    
    return True

def get_value(obj):
    if isinstance(obj, QtGui.QLineEdit):
        return str(obj.text())
    if isinstance(obj, QtGui.QComboBox):
        return str(obj.currentText())
    
    return None

class Validator(object):
    def __init__(self, parent):
        self.objects = []
        
        for name in dir(parent):
            obj = getattr(parent, name)
            value = get_value(obj)
            if value is None:
                continue
            else:
                self.objects.append(obj)
                
        # sort up/down left/right
        self.objects.sort(cmp=lambda a,b: cmp((a.y(), a.x()), (b.y(), b.x())))
                
    def validate(self):
        errors = []
        for obj in self.objects:
            value = get_value(obj)
            
            # is required?
            prop = obj.property("is_required")
            if prop.isValid() and prop.toBool() is True:
                if not is_required(value):
                    errors.append((obj, "'%s' is required" % obj.toolTip()))
                    
            # is integer?
            prop = obj.property("is_integer")
            if prop.isValid() and prop.toBool() is True:
                if not is_integer(value):
                    errors.append((obj, "'%s' must be a number" % obj.toolTip()))
                    
            # is email?
            prop = obj.property("is_email")
            if prop.isValid() and prop.toBool() is True:
                if not is_email(value):
                    errors.append((obj, "'%s' must be a valid email address" % obj.toolTip()))
                    
        return errors
            
            