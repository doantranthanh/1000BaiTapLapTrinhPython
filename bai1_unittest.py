import bai1
import unittest


class Test_Bai_Mot(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(bai1.findSum(3), 6)

    def test_case_one(self):
        self.assertEqual(bai1.findSum(5), 15)


if __name__ == '__main__':
    unittest.main()
