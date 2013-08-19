"""
Created on Aug 15, 2013

@author: hailiang
"""

class Yeah():
    pass

def new_foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'

if __name__ == '__main__':
    new_foo(1, 2, 3, 4)
    new_foo(a=1, b=2, c=3)
    new_foo(1, 2, 3, 4, a=1, b=2, c=3)
    new_foo('a', 1, None, a=1, b='2', c=3)
