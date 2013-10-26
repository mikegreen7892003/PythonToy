#coding=utf-8
"""
Show the magic of super
Reference:
http://stackoverflow.com/questions/19608134/why-is-python-3-xs-super-magic
http://www.python.org/dev/peps/pep-3135/
>>> super_ = super
>>> class A(object):
...     def x(self):
...         pass
...
>>> class B(A):
...     def x(self):
...         import sys
...         if sys.version_info > (3, ):
...             super().x()
...             super_().x()
>>> B().x()
"""
def doctests():
    import doctest
    return doctest.DocTestSuite()
