'''
Created on Dec 31, 2009

@author: gumuz
'''
from PyQt4 import QtGui
def _(msg): return msg

EMPTY_VALUES = (None, "")

class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg


def set_value(attr, value):
    if isinstance(attr, QtGui.QLineEdit):
        attr.setText(str(value))
    if isinstance(attr, QtGui.QComboBox):
        index = attr.findText(str(value))
        attr.setCurrentIndex(index)
    if isinstance(attr, QtGui.QCheckBox):
        attr.setChecked(bool(value))
        
def get_value(attr):
    if isinstance(attr, QtGui.QLineEdit):
        return str(attr.text())
    if isinstance(attr, QtGui.QComboBox):
        return str(attr.currentText())
    if isinstance(attr, QtGui.QCheckBox):
        return attr.isChecked()

class BaseField(object):
    creation_counter = 0
    default_error_messages = {
        'required': _(u'This field is required.'),
        'invalid': _(u'Enter a valid value.'),
    }
    def __init__(self, alt_name=None, label=None, required=True, error_messages=None):
        # instance vars
        self.alt_name, self.required, self.label = alt_name, required, label
        
        # Increase the creation counter, and save our local copy.
        self.creation_counter = BaseField.creation_counter
        BaseField.creation_counter += 1

        def set_class_error_messages(messages, klass):
            for base_class in klass.__bases__:
                set_class_error_messages(messages, base_class)
            messages.update(getattr(klass, 'default_error_messages', {}))

        messages = {}
        set_class_error_messages(messages, self.__class__)
        messages.update(error_messages or {})
        self.error_messages = messages
        
    def clean(self, value):
        if self.required and value in EMPTY_VALUES:
            raise ValidationError(self.error_messages['required'])
        return value

        
class CharField(BaseField):
    default_error_messages = {
        'max_length': _(u'Ensure this value has at most %(max)d characters (it has %(length)d).'),
        'min_length': _(u'Ensure this value has at least %(min)d characters (it has %(length)d).'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        self.max_length, self.min_length = max_length, min_length
        super(CharField, self).__init__(*args, **kwargs)

    def clean(self, value):
        "Validates max_length and min_length. Returns a Unicode object."
        super(CharField, self).clean(value)
        if value in EMPTY_VALUES:
            return u''
#        value = smart_unicode(value)
        value_length = len(value)
        if self.max_length is not None and value_length > self.max_length:
            raise ValidationError(self.error_messages['max_length'] % {'max': self.max_length, 'length': value_length})
        if self.min_length is not None and value_length < self.min_length:
            raise ValidationError(self.error_messages['min_length'] % {'min': self.min_length, 'length': value_length})
        return value
    
class BooleanField(BaseField):
    def clean(self, value):
        """Returns a Python boolean object."""
        # Explicitly check for the string 'False', which is what a hidden field
        # will submit for False. Also check for '0', since this is what
        # RadioSelect will provide. Because bool("True") == bool('1') == True,
        # we don't need to handle that explicitly.
        if value in ('False', '0'):
            value = False
        else:
            value = bool(value)
        super(BooleanField, self).clean(value)
        if not value and self.required:
            raise ValidationError(self.error_messages['required'])
        return value


class IntegerField(BaseField):
    default_error_messages = {
        'invalid': _(u'Enter a whole number.'),
        'max_value': _(u'Ensure this value is less than or equal to %s.'),
        'min_value': _(u'Ensure this value is greater than or equal to %s.'),
    }

    def __init__(self, max_value=None, min_value=None, *args, **kwargs):
        self.max_value, self.min_value = max_value, min_value
        super(IntegerField, self).__init__(*args, **kwargs)

    def clean(self, value):
        """
        Validates that int() can be called on the input. Returns the result
        of int(). Returns None for empty values.
        """
        super(IntegerField, self).clean(value)
        if value in EMPTY_VALUES:
            return None
        try:
            value = int(str(value))
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'])
        if self.max_value is not None and value > self.max_value:
            raise ValidationError(self.error_messages['max_value'] % self.max_value)
        if self.min_value is not None and value < self.min_value:
            raise ValidationError(self.error_messages['min_value'] % self.min_value)
        return value