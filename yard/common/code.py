'''
Created on Aug 16, 2013

@author: hailiang
'''
# encode 
a = '\xe4\xbd\xa0\xe5\xa5\xbd'
print a 
b=unicode(a, "UTF-8")
print b

c="hello"

def foo(bar):
    print bar

if __name__ == "__main__":
    foo( \
        "yes")
