#coding=utf-8
"""
实现带缓存功能的property，用法和系统自带的property一样
参考
http://docs.python.org/2/howto/descriptor.html#properties
"""
_missing = object()


class cached_property(property):
    """重写property，使其带缓存功能"""
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__.get("_{}".format(self.fget.__name__), _missing)
        if value is _missing:
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            value = self.fget(obj)
            obj.__dict__["_{}".format(self.fget.__name__)] = value
        return value
