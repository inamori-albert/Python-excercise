import unittest

# unitテストのテスト用ファイル
#  python -m unittest test.py でテストできる
class MyTest(unittest.TestCase):

    # メソッド名のプレフィックスにtestをつける
    def test_do_somethig(self):
        # テストケースを書く
        one = 1
        self.assertEqual(one, 1, "one is 1")


if __name__ == "__main__":
    unittest.main()
    