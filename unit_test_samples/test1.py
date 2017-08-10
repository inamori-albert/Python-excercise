import unittest

# unitテストのテスト用ファイル
#  python -m unittest test.py でテストできる
class MyTest(unittest.TestCase):

    # 各テスト前に呼び出される
    # DBのセットアップやテストデータの準備を行う
    def setUp(self):
        print("SetUp is called.")

    # 各テスト後に呼び出される
    # テストの後処理(成果物の削除等)やDB処理の後処理などを行う
    def tearDown(self):
        print("tearDown is called.")

    # テストメソッド
    # メソッド名のプレフィックスにtestをつける
    def test_do_somethig1(self):
        # テストケースを書く
        one = 1
        self.assertEqual(one, 1, "one is 1")

    def test_do_somethig2(self):
        # テストケースを書く
        two = 2
        self.assertEqual(two, 2, "two is 2")


if __name__ == "__main__":
    unittest.main()
