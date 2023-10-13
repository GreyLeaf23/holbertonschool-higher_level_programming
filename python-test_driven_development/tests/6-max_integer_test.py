#!/usr/bin/python3
"""unit from module max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):

    def testmaxinteger(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-10, -9, -7, -6]), -6)
        self.assertEqual(max_integer([99, 4, -7, -100]), 99)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertRaises(TypeError, max_integer(["hello"]))
        self.assertRaises(TypeError, max_integer())
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-10, 0, -11]), 0)



if __name__ == '__main__':
    unittest.main()
