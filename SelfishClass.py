def selfish(cls):

    class Wrap(cls):
        def __init__(self, *args, **kwargs):
            self.__class__.__name__ = cls.__name__

            for k, v in kwargs.items():
                setattr(self, k, v)

            super(Wrap, self).__init__(*args, **kwargs)

        def __repr__(self):
            return '{}: {}'.format(self.__class__.__name__, ', '.join('{}<{}>: {}'.format(k, type(v).__name__, v) for k, v in self.__dict__.items()))

    return Wrap
