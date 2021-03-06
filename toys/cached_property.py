#coding=utf-8
"""
rewrite property, make the property can be cached
Reference:
http://docs.python.org/2/howto/descriptor.html#properties
"""
_missing = object()


class cached_property(property):
    """rewrite property, make the property can be cached"""
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
