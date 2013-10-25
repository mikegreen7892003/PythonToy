#coding=utf-8
"""
Howto rewrite the module itself
Reference:
https://github.com/amoffat/sh/blob/master/sh.py
>>> from toys.rewrite_module import hello
>>> hello
'hello'
"""
import os
import sys
from types import ModuleType


class Environment(object):
    def __init__(self, globs):
        self.globs = globs

    def __setitem__(self, k, v):
        self.globs[k] = v

    def __getitem__(self, k):
        try:
            return self.globs[k]
        except KeyError:
            pass

        if k == "__all__":
            raise ImportError("Cannot import * from rewrite_module.")

        if k.startswith("__") and k.endswith("__"):
            raise AttributeError

        try:
            return os.environ[k]
        except KeyError:
            pass

        return k


class ModuleWrapper(ModuleType):
    def __init__(self, original_modules):
        for attr in ["__builtins__", "__doc__", "__name__", "__package__"]:
            setattr(self, attr, getattr(original_modules, attr, None))
        self.__path__ = []
        self.original_modules = original_modules
        self.env = Environment(globals())

    def __setattr__(self, name, value):
        if hasattr(self, "env"):
            self.env[name] = value
        ModuleType.__setattr__(self, name, value)

    def __getattr__(self, name):
        if name == "env":
            raise AttributeError
        return self.env[name]

    def __call__(self, **kwargs):
        return ModuleWrapper(self.self_module, kwargs)


def doctests():
    import doctest
    return doctest.DocTestSuite()


if __name__ == "__main__":
    raise ValueError("This file can't be run as the main file")
else:
    this_module = sys.modules[__name__]
    sys.modules[__name__] = ModuleWrapper(this_module)
