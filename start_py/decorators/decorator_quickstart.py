'''
Created on Aug 21, 2013

@author: hailiang
'''
class myDecorator(object):
    
    def __init__(self, f):
        print "1:inside myDecorator.__init__()"
        self.f = f  # Prove that function definition has completed
 
    def __call__(self, args=None):
        print "3:inside myDecorator.__call__()"
        self.f(args)
 
@myDecorator
def aFunction(args=None):
    print "4:inside aFunction()"
    print args
 
print "2:Finished decorating aFunction()"
aFunction()
print "another call"
aFunction(args="value")
