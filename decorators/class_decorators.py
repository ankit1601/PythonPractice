class Power(object):
    """Here function will go as an Argument
        Constructor will assign function to self instance
        final call method will be invoked and it will be invoked
        only once
        Arguments will be passed to Call method and then it will
        apply those to self._arg which is a function on which
        class decorator is applied.
        very important point to note that function will become instance of call
    """
    def __init__(self, arg):
        print("constructor", arg)
        self._arg = arg

    def __call__(self, a, b):
        retval = self._arg(a, b)
        return retval ** 2


@Power
def multiply_together(a, b):
    return a * b


print(isinstance(multiply_together, Power))
print(multiply_together(2, 2))
