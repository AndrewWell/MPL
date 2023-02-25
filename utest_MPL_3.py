import unittest
import MPL_3 as mpl


class Test(unittest.TestCase):

    def test_findUselessNum(self):
        list = [1, 2, 3, 4, 5, 3, 2]
        self.assertEqual(mpl.findUselessNum(list), max(list) / len(list))
        list = [1.2, 22.4, 3, 4.5, 5, 3, 2.7]
        self.assertEqual(mpl.findUselessNum(list), max(list) / len(list))

    def test_findUselessNum_negativeNum(self):
        list = [-1, 2, 3, -4, 5, -3, 2]
        self.assertEqual(mpl.findUselessNum(list), max(list) / len(list))
        list = [-1.2, -22.4, 3, 4.5, -5, 3, -2.7]
        self.assertEqual(mpl.findUselessNum(list), max(list) / len(list))

    def test_findUselessNum_except(self):
        self.assertRaises(mpl.DataTypeError, mpl.findUselessNum, ["one", 2, 3, 4, 5])
        self.assertRaises(mpl.DataTypeError, mpl.findUselessNum, [1, False, 3, 4, 5])
        self.assertRaises(mpl.DataTypeError, mpl.findUselessNum, [1, 2, True, 4, 5])


if __name__ == "__main":
    unittest.main()
