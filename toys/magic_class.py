#coding=utf-8
"""
Show the magic of class definition
Reference:
http://stackoverflow.com/questions/19622550/how-to-use-class-name-in-class-scope-in-python
http://docs.python.org/2/reference/compound_stmts.html#class-definitions
>>> import inspect
>>> class Foo(object):
...     something = "hello, world"
...     class Bar(object):
...         another = inspect.currentframe().f_back.f_locals['something']
...
>>> Foo.Bar.another
'hello, world'
"""
def doctests():
    import doctest
    return doctest.DocTestSuite()
