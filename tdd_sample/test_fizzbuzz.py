import unittest
from fizzbuzz import FizzBuzz #テスト対象


class TestFizzBuzz(unittest.TestCase):


    def setUp(self):
        # 初期化処理
        pass


    def tearDown(self):
        # 終了処理
        pass


    def testNewClass(self):
        # テストを書いていく
        self.assertNotEqual(FizzBuzz(10), None)


class TestRandom(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
