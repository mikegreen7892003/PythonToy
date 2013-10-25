#coding=utf-8
"""
测试cached_property
"""
import unittest
from toys.cached_property import cached_property


class TestCachedProperty(unittest.TestCase):
    """测试cached_property类"""
    def setUp(self):

        class Foo(object):
            def __init__(self):
                self.cached_bar = False

            @cached_property
            def bar(self):
                self.cached_bar = not self.cached_bar
                return "bar"

        self.cachedFoo = Foo()

    def test_None(self):
        self.assertFalse(self.cachedFoo.cached_bar)
        self.assertEqual(self.cachedFoo.bar, "bar")
        self.assertTrue(self.cachedFoo.cached_bar)
        self.assertEqual(self.cachedFoo.bar, "bar")
        self.assertTrue(self.cachedFoo.cached_bar)
