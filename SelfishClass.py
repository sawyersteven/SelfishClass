def selfish(cls):

    class Wrap(cls):
        def __init__(self, *args, **kwargs):
            self.__class__.__name__ = cls.__name__

            for k, v in kwargs.items():
                setattr(self, k, v)

            super_init = super(Wrap, self).__init__

            for i, a in enumerate(args):
                setattr(self, super_init.__code__.co_varnames[i+1], a)

            super_init(*args, **kwargs)

        def __repr__(self):
            return '{}: {}'.format(self.__class__.__name__, ', '.join('{}<{}>: {}'.format(k, type(v).__name__, v) for k, v in self.__dict__.items()))

    return Wrap
