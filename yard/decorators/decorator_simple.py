class Test(object):
    def __call__( self, f):
        def wrapper(self, *args, **kwargs):
            # anything in the old Test.__call__ goes here.
            return f(self, *args, **kwargs)
        return wrapper

class TestController(BaseController):
    @Test()
    def index(self):
        return 'hello world'