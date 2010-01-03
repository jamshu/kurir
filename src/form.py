'''
Created on Dec 31, 2009

@author: gumuz
'''

from fields import ValidationError, get_value, set_value, BaseField, IntegerField

class Form(object):
    def __init__(self, initial_data=None):
        self.data = {}
        self.cleaned_data = {}
        
        if initial_data:
            if isinstance(initial_data, dict):
                    self.data.update(initial_data)
            for name, attr in self.get_fields():
                if hasattr(initial_data, name):
                    self.data[name] = getattr(initial_data, name)
                    
    def validate(self):
        errors = []
        for name, attr in self.get_fields():
            try:
                value = attr.clean(self.data.get(name, None))
                self.cleaned_data[name] = value
            except ValidationError, e:
                errors.append((name, e.msg))
                
        return errors
                
        
        
    def display(self, target):
        for name, attr in self.get_fields():
            if hasattr(target, name):
                target_attr = getattr(target, name)
                set_value(target_attr, self.data.get(name, None))
        
    def load(self, target):
        for name, attr in self.get_fields():
            if hasattr(target, name):
                target_attr = getattr(target, name)
                self.data[name] = get_value(target_attr)            
    
    def get_fields(self):
        attrs = []
        for name in dir(self):
            attr = getattr(self, name)
            if isinstance(attr, BaseField):
                attrs.append((name, attr))
                
        attrs.sort(cmp=lambda a,b:cmp(a[1].creation_counter, b[1].creation_counter))
        return attrs
        
        
if __name__ == "__main__":
    from fields import CharField
    
    class TestForm(Form):
        first_name  = CharField(50, 3)
        last_name = CharField(50, 2)
        age = IntegerField()
        
    f = TestForm()
    print f.get_fields()