#!/user/bin/env python
# -*-coding:utf-8 -*-

import unittest
from math import *

class testmathfunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,sqrt(9))



if __name__ == '__main__':
    unittest.main(verbosity=2)
