#coding=utf-8
"""
Test cached_property
"""
import unittest
from toys.cached_property import cached_property


class TestCachedProperty(unittest.TestCase):
    """A testcase for cached_property"""
    def setUp(self):

        class Foo(object):
            def __init__(self):
                self.cached_bar = False
                self.cached_dog = False

            @cached_property
            def bar(self):
                self.cached_bar = not self.cached_bar
                return "bar"

            @cached_property
            def dog(self):
                self.cached_dog = not self.cached_dog
                return None

        self.cachedFoo = Foo()

    def test_sample(self):
        self.assertFalse(self.cachedFoo.cached_bar)
        self.assertEqual(self.cachedFoo.bar, "bar")
        self.assertTrue(self.cachedFoo.cached_bar)
        self.assertEqual(self.cachedFoo.bar, "bar")
        self.assertTrue(self.cachedFoo.cached_bar)

    def test_None(self):
        self.assertFalse(self.cachedFoo.cached_dog)
        self.assertEqual(self.cachedFoo.dog, None)
        self.assertTrue(self.cachedFoo.cached_dog)
        self.assertEqual(self.cachedFoo.dog, None)
        self.assertTrue(self.cachedFoo.cached_dog)
