import unittest
from SelfishClass import selfish

''' Define args here for convenience '''
arg1 = 12
arg2 = 21
kwarg_str = 'Hello World'
kwarg_int = 8675309
kwarg_list = ['this', 'that', 'the other']


@selfish
class TestClass(object):
    def __init__(self, arg1, arg2, kwarg_str=None, kwarg_int=None, kwarg_list=None):
        ''' Test class for handling args, kwargs, and init
        arg1 (int): to be added to arg2 to make sure __init__ is called
        arg2 (int): to be added to arg1 to make sure __init__ is called
        kwarg_str (str): string to test as instnce property
        kwarg_int (int): string to test as instnce property
        kwarg_list (list): string to test as instnce property
        '''
        self.init_attribute = arg1 + arg2
        return

    def test_method(self):
        ''' Returns first item in self.kwarg '''
        return self.kwarg_list[0]


@selfish(ignore=['arg1', 'kwarg_str'])
class TestClassIgnoreSpecific(object):
    def __init__(self, arg1, arg2, kwarg_str=None, kwarg_int=None, kwarg_list=None):
        ''' Test class for handling args, kwargs, and init
        arg1 (int): to be added to arg2 to make sure __init__ is called
            Should be ignored in decorator per args
        arg2 (int): to be added to arg1 to make sure __init__ is called
        kwarg_str (str): string to test as instnce property
            Should be ignored in decorator per args
        kwarg_int (int): string to test as instnce property
        kwarg_list (list): string to test as instnce property
        '''
        self.init_attribute = arg1 + arg2
        return

    def test_method(self):
        ''' Returns first item in self.kwarg '''
        return self.kwarg_list[0]


@selfish(args=False)
class TestClassIgnoreArgs(object):
    def __init__(self, arg1, arg2, kwarg_str=None, kwarg_int=None, kwarg_list=None):
        ''' Test class for handling args, kwargs, and init
        arg1 (int): to be added to arg2 to make sure __init__ is called
            Should be ignored in decorator per args
        arg2 (int): to be added to arg1 to make sure __init__ is called
        kwarg_str (str): string to test as instnce property
            Should be ignored in decorator per args
        kwarg_int (int): string to test as instnce property
        kwarg_list (list): string to test as instnce property
        '''
        self.init_attribute = arg1 + arg2
        return

    def test_method(self):
        ''' Returns first item in self.kwarg '''
        return self.kwarg_list[0]


@selfish(kwargs=False)
class TestClassIgnoreKwargs(object):
    def __init__(self, arg1, arg2, kwarg_str=None, kwarg_int=None, kwarg_list=None):
        ''' Test class for handling args, kwargs, and init
        arg1 (int): to be added to arg2 to make sure __init__ is called
            Should be ignored in decorator per args
        arg2 (int): to be added to arg1 to make sure __init__ is called
        kwarg_str (str): string to test as instnce property
            Should be ignored in decorator per args
        kwarg_int (int): string to test as instnce property
        kwarg_list (list): string to test as instnce property
        '''
        self.init_attribute = arg1 + arg2
        return

    def test_method(self):
        ''' Returns first item in self.kwarg '''
        return self.kwarg_list[0]


class TestBase(unittest.TestCase):
    ''' Tests selfish using a plain decorator with no args '''
    target_class = TestClass

    @classmethod
    def setUpClass(cls):
        cls.testclass = cls.target_class(arg1, arg2, kwarg_str=kwarg_str, kwarg_int=kwarg_int, kwarg_list=kwarg_list)
        print("\n\t Testing Class: " + cls.__dict__['target_class'].__name__)

    def test_000_create_class(self):
        ''' Tests creation and instantiation of selfish class '''
        self.assertIsInstance(self.testclass, self.target_class)

    def test_001_selfish_instance_vars(self):
        ''' Tests instance args match passed args
        Compares against globals() to match document-level vars
        '''
        glb = globals()
        for k, v in self.testclass.__dict__.items():
            if k == 'init_attribute':
                continue
            else:
                self.assertEqual(glb[k], v)

    def test_002_selfish_init(self):
        ''' Tests that class's __init__ is called correctly '''
        self.assertEqual(self.testclass.init_attribute, 21 + 12)

    def test_003_selfish_method(self):
        ''' Tests that the selfish class's methods are called correctly '''
        self.assertEqual(self.testclass.test_method(), kwarg_list[0])


class TestIgnoreSpecific(TestBase):
    ''' Tests selfish with ignore args
    Runs same tests as TestNoArgs with additional tests for args
    '''
    target_class = TestClassIgnoreSpecific

    def test_01_selfish_ignore(self):
        ''' Tests that ignored args are not in instance '''
        self.assertFalse(hasattr(self.testclass, 'arg1'))
        self.assertFalse(hasattr(self.testclass, 'kwarg_str'))


class TestIgnoreArgs(TestBase):
    ''' Tests selfish with ignore args
    Runs same tests as TestNoArgs with additional tests for args
    '''
    target_class = TestClassIgnoreArgs

    def test_01_selfish_ignore(self):
        ''' Tests that ignored args are not in instance '''
        self.assertFalse(hasattr(self.testclass, 'arg1'))
        self.assertFalse(hasattr(self.testclass, 'arg2'))


class TestIgnoreKwargs(TestBase):
    ''' Tests selfish with ignore args
    Runs same tests as TestNoArgs with additional tests for args
    '''
    target_class = TestClassIgnoreKwargs

    def test_003_selfish_method(self):
        return

    def test_01_selfish_ignore(self):
        ''' Tests that ignored args are not in instance '''
        self.assertFalse(hasattr(self.testclass, 'kwarg_str'))
        self.assertFalse(hasattr(self.testclass, 'kwarg_int'))
        self.assertFalse(hasattr(self.testclass, 'kwarg_list'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
