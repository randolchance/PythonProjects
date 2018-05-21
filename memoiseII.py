import inspect

class Memoise:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            if inspect.isgenerator(self.fn(*args)):
                result = [i for i in self.fn(*args)]
            else:
                result = self.fn(*args)
            self.memo[args] = result
        return self.memo[args]

"""
USE
@Memoise
def function(x)
    ...
"""
