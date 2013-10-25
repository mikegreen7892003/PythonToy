#coding=utf-8
import unittest
import test


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for case in unittest.TestLoader().discover("test"):
        suite.addTests(case)
    unittest.TextTestRunner(verbosity=2).run(suite)
