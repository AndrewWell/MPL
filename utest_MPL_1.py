import unittest
import MPL_1 as mpl


class Test(unittest.TestCase):

    def test_cycleFunc_except(self):
        self.assertRaises(mpl.ValueTooLargeError, mpl.cyclicFunc, 1, 2, 3, 4, 5, 6)
        self.assertRaises(mpl.ValueTooLargeError, mpl.cyclicFunc, 1.1, 3.3, 5, 2, 3, 5)

        self.assertRaises(mpl.ValueTooSmallError, mpl.cyclicFunc, 4, 2, 1, 7, 4, 9)
        self.assertRaises(mpl.ValueTooSmallError, mpl.cyclicFunc, 0.4, 0.2, 0.1, 0.2, 0.3, 0.7)

        self.assertRaises(mpl.DataTypeError, mpl.cyclicFunc, "one", 4, 1, 4, 5, 6)
        self.assertRaises(mpl.DataTypeError, mpl.cyclicFunc, 1, True, 1, 4, 5, 6)
        self.assertRaises(mpl.DataTypeError, mpl.cyclicFunc, 1, 4, False, 4, 5, 6)
        self.assertRaises(mpl.DataTypeError, mpl.cyclicFunc, "one", True, 1, False, 5, 6)

    def test_func_except(self):
        self.assertRaises(ZeroDivisionError, mpl.func, 5, 7, 3, 0)

    def test_func(self):
        self.assertEqual(mpl.func(0, 0, 0, 0), 0)
        self.assertEqual(mpl.func(-7, 3, 1, -7), 0)
        self.assertEqual(mpl.func(-2, 0, 3, -1), -1)


if __name__ == "__main__":
    unittest.main()
