![Logo](https://raw.githubusercontent.com/sawyersteven/SelfishClass/master/img/Logo_wide.png)

# SelfishClass
SelfishClass is a minimal (~1kb) alternative to dataclasses and the popular [attrs](https://github.com/python-attrs/attrs) package for python.

SelfishClass eliminates the need to assign variables as `self.varname` in a class's `__init__` method and provides a simple `__repr__` for the class instance.

##### Why not attrs?

Attrs does a lot of things very well. SelfishClass does a few things very well. Rarely do I need all of Attr's functionality. Attrs weighs in at ~100kb. SelfishClass is less than 1kb. In the words of the great philosopher Kevin Malone, `Me think, why waste time say lot word, when few word do trick.`

##### Why not dataclasses?
Dataclasses requires python 3.7, which may not be an option in some environments. Dataclasses require re-defining `__init__` methods as `__post_init__`, which can feel unintuitive and may require rewriting your classes. SelfishClass only requires that you insert the decorator.

### Installation
SelfishClass has been tested on Python 3.4.0 and 2.7.14 and is likely compatible with most other versions.

Install via pip with `pip install SelfishClass`

### Usage
SelfishClass provides a simple class decorator that requires minimal or no change to your existing class definition.

    from SelfishClass import selfish

    @selfish
    class Teacher(object):
        def __init__(self, name, id, department=None):
            pass

    stan = Teacher('Stan', 445, department='Math')

    print(stan)
    >> Teacher: department<str>: Math, id<int>: 445, name<str>: Stan

All vars are accessible in `__init__` as both instance variables and local variable. For instance, in `__init__` we can refer to `name` as both `name` and `self.name`.

You may specify certain arguments to ignore if you do not want them to be assigned as instance vars. This is accomplished by using the decorator as such:
    
    # All positional args will be ignored by selfish
    @selfish(args=False)
    class Teacher(object):
        def __init__(self, name, id, department=None):
            pass
            
    # All kwargs will be ignored by selfish
    @selfish(kwargs=False)
    class Teacher(object):
        def __init__(self, name, id, department=None):
            pass
            
    # Only id will be ignored by selfish
    @selfish(ignore=['id'])
    class Teacher(object):
        def __init__(self, name, id, department=None):
            pass