#coding=utf-8
"""
Howto use exec
Reference:
http://hg.python.org/cpython/file/2.7/Lib/collections.py#l231
"""
import sys

_class_template = """\
class {classname}(object):
    def __init__(self):
        self.sys = sys
"""


def exec_class(classname):
    """use exec to define a new class which named by classname

    Usage:
    >>> from toys.exec_example import exec_class
    >>> hello = exec_class("hello")
    >>> hello
    <class 'toys.exec_example.hello'>
    >>> hello().sys
    <module 'sys' (built-in)>
    """
    class_definition = _class_template.format(classname=classname)
    namespace = {"sys": sys}
    try:
        exec class_definition in namespace
    except SyntaxError as e:
        raise SyntaxError(e.message + ":\n" + class_definition)
    result = namespace[classname]

    try:
        result.__module__ = sys._getframe(1).f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        pass

    return result


def doctests():
    import doctest
    return doctest.DocTestSuite()
