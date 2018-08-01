    
`selfish(__cls=None, args=True, kwargs=True, ignore=[])`
Class decorator to automatically assign instance vars for all values
    passed to __init__


    
    __cls (class): Decorated class. Passed by decorator call if no args are
        passed (ie @selfish, not @selfish(ignore=[])). Never pass this value.
    args (bool): Set False to ignore all args
    kwargs (bool): Set False to ignore all kwargs
    ignore (list): Strings of each var name to be excluded from the instance
    
    
Decorators with the option to take arguments or to be used plain are a bit complicated.

If no args are passed, ie @selfish, cls is passed by the interpreter and we need to return the class Wrap. This is inside the decorator() function so that it is compatible with args as well.

If args are passed to the decorator, ie @selfish(ignore=['user_name']), we need to return a function that accepts cls in the way that a plain @selfish call accepts cls as the first arg. Because of this we return the decorator method.

It is best to think of selfish as a wrapper for the decorator, which is actual the decorator function.

The reason Wrap must be defined inside the decorator method is that cls will be None if selfish is called with args and cls *must* be a class when Wrap is defined or a TypeError exception will be raised.
