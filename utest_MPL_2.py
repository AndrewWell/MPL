import unittest
import MPL_2 as mpl


class Test(unittest.TestCase):

    def test_func(self):
        self.assertEqual(mpl.func(2, 0.32, 1.25, -4, 0.75, 2.2), -2.259)
        self.assertEqual(mpl.func(2, 0.32, 1.25, -4, 0, 2.2), -2.714)
        self.assertEqual(mpl.func(-2, 0.32, -1.25, 4, 0.75, 2.2), 0.002)
        self.assertEqual(mpl.func(0, 0, 0, 0, 0, 0), -3.384)


    def test_func_except(self):
        self.assertRaises(mpl.DataTypeError, mpl.func, 1, 2, 3, 4, 5, True)
        self.assertRaises(mpl.DataTypeError, mpl.func, "one", 2, 3, 4, 5, 6)
        self.assertRaises(mpl.DataTypeError, mpl.func, 1, 2, False, 4, 5, 6)
        self.assertRaises(mpl.DataTypeError, mpl.func, "one", 2, False, 4, 5, True)


if __name__ == "__main__":
    unittest.main()
