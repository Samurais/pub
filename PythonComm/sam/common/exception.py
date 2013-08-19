'''
Created on Aug 15, 2013

@author: hailiang
'''
# class MyException(Exception):
#     """My documentation"""
class MyException(Exception):
    pass
# class MyException(Exception):
#     def _get_message(self): 
#         return self.args[0]
#     def _set_message(self, message): 
#         self._message = message
#     message = property(_get_message, _set_message)
# yes , there is a diff
try:
    raise MyException('description1', 'description2')
except MyException as my:
    print str(my)
    print unicode(my) 
    
try:
    raise MyException(u'description1', u'description2')
except MyException as my:
    print str(my)  
    print unicode(my)  
    
