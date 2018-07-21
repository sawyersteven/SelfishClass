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


class TestScheduler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testclass = None

    def test_00_create_class(self):
        ''' Tests creation and instantiation of selfish class '''
        TestScheduler.testclass = TestClass(arg1, arg2, kwarg_str=kwarg_str, kwarg_int=kwarg_int, kwarg_list=kwarg_list)
        self.assertIsInstance(TestScheduler.testclass, TestClass)

    def test_01_selfish_kwargs(self):
        ''' Tests kwargs of selfish class '''
        self.assertEqual(TestScheduler.testclass.kwarg_str, kwarg_str)
        self.assertEqual(TestScheduler.testclass.kwarg_int, kwarg_int)
        self.assertEqual(TestScheduler.testclass.kwarg_list, kwarg_list)

    def test_02_selfish_init(self):
        ''' Tests that class's __init__ is called correctly '''
        self.assertEqual(TestScheduler.testclass.init_attribute, 21 + 12)

    def test_03_selfish_method(self):
        ''' Tests that the selfish class's methods are called correctly '''
        self.assertEqual(TestScheduler.testclass.test_method(), kwarg_list[0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
