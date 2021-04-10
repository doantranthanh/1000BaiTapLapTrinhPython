import bai2
import unittest


class Test_Bai_Hai(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(bai2.tinhTongBacHai(3), 14)


if __name__ == "__main__":
    unittest.main()
