#coding=utf-8
import unittest
import test
doctests = [
    'toys.rewrite_module.doctests',
    'toys.exec_example.doctests',
]


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for case in unittest.TestLoader().discover("test"):
        suite.addTests(case)
    suite.addTests(unittest.TestLoader().loadTestsFromNames(doctests))
    unittest.TextTestRunner(verbosity=2).run(suite)
