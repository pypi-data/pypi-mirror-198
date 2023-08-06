import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../..'))
from magicmethods import AttributeMethods
# from ..magicmethods import AttributeMethods

class MyClass(AttributeMethods):
    def __init__(self):
        super().__init__()
        self._start_init()
        self.attr1 = 1
        self._end_init()

    def _set_value(self, val):
        self.__dict__['value'] = val * 2

    def _set_attr2(self, val):
        self.__dict__['attr2'] = val * 3


c = MyClass()
c.value = 2
c.attr1 = 2
c.attr2 = 2
c.attr3 = 2
print({'value': {'check': hasattr(c, 'value'), 'val': c.value}})
print({'attr1': {'check': hasattr(c, 'attr1'), 'val': c.attr1}})
print({'attr2': {'check': hasattr(c, 'attr2'), 'val': c.attr2}})
print({'attr3': {'check': hasattr(c, 'attr3')}})

'''Response: 
{'value': {'check': True, 'val': 4}}
{'attr1': {'check': True, 'val': 2}}
{'attr2': {'check': True, 'val': 6}}
{'attr3': {'check': False}}
'''