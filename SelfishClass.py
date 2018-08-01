def selfish(__cls=None, args=True, kwargs=True, ignore=[]):

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
