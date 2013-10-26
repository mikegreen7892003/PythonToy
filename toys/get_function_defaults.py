#coding=utf-8
"""
Howto get function defaults dict
Reference:
http://stackoverflow.com/questions/12627118/get-a-function-arguments-default-value
"""
def get_func_defaults(func):
    """get func defaults dict

    Usage:
    >>> def foo(v1, v2="hello", *args, **kwargs):
    ...     pass
    ...
    >>> get_func_defaults(foo)
    {'v2': 'hello'}
    """
    import inspect
    argsspec = inspect.getargspec(func)
    return dict(zip(reversed(argsspec.args), reversed(argsspec.defaults)))


def doctests():
    import doctest
    return doctest.DocTestSuite()
