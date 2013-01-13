#!/bin/env python
# coding=utf-8
""" test functions
"""

__author__ = 'yyaadet <yyaadet2002@gmail.com>'
__status__ = 'Product'  # can be 'Product', 'Development', 'Prototype'


import doctest
import unittest
from doctest import DocTestSuite


LIST_OF_DOCTESTS = [
    "base",
    "temperature",
    "wilson",
]

LIST_OF_UNITTESTS = [
]

def suite():
    suite = unittest.TestSuite()
    for t in LIST_OF_DOCTESTS:
        suite.addTest(DocTestSuite(
            __import__(t, globals(), locals(), fromlist=["*"])
        ))
    for t in LIST_OF_UNITTESTS:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(
            __import__(t, globals(), locals(), fromlist=["*"])
        ))
    return suite
        
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
            
