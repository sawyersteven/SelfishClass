def selfish(__cls=None, args=True, kwargs=True, ignore=[]):
    ''' Class decorator to automatically assign instance vars for all values
        passed to __init__

    __cls (class): Decorated class. Passed by decorator call if no args are
        passed (ie @selfish, not @selfish(ignore=[])). Never pass this value.
    args (bool): Set False to ignore all args
    kwargs (bool): Set False to ignore all kwargs
    ignore (list): Strings of each var name to be excluded from the instance


    Decorators with the option to take arguments or to be used plain are a
        bit complicated.

    If no args are passed, ie @selfish, cls is passed by the interpreter
        and we need to return the class Wrap. This is inside the decorator()
        function so that it is compatible with args as well.

    If args are passed to the decorator, ie @selfish(ignore=['user_name']), we
        need to return a function that accepts cls in the way that a plain
        @selfish call accepts cls as the first arg. Because of this we return
        the decorator method.

    It is best to think of selfish as a wrapper for the decorator, which is
        actuall the decorator function.

    The reason Wrap must be defined inside the decorator method is that cls
        will be None if selfish is called with args and cls *must* be a class
        when Wrap is defined or an exception will be raised.


    '''

    def decorator(cls):
        class Wrap(cls):
            def __init__(self, *_args, **_kwargs):
                self.__class__.__name__ = cls.__name__
                super_init = super(Wrap, self).__init__

                if kwargs:
                    for k, v in _kwargs.items():
                        if k not in ignore:
                            setattr(self, k, v)

                if args:
                    for i, a in enumerate(_args):
                        name = super_init.__code__.co_varnames[i + 1]
                        if name not in ignore:
                            setattr(self, name, a)

                super_init(*_args, **_kwargs)

            def __repr__(self):
                return '{}: {}'.format(self.__class__.__name__, ', '.join('{}<{}>: {}'.format(k, type(v).__name__, v) for k, v in self.__dict__.items()))

        return Wrap

    if __cls is not None:
        return decorator(__cls)
    else:
        return decorator
