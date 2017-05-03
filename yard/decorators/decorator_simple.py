class Test(object):
    def __call__( self, f):
        def wrapper(self, *args, **kwargs):
            # anything in the old Test.__call__ goes here.
            kwargs['foo'] = "bar2"
            return f(self, *args, **kwargs)
        return wrapper

class TestController():
    @Test()
    def index(self, foo = "foo"):
        print foo


t = TestController()
t.index(foo = "bar")