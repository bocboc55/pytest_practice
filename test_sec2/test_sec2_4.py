# メソッドをテストする

# クラスの頭にTestをつける
class TestExsample1():
    # 関数にもtestをつける
    def test_example1(self):
        assert True

    # これは実行されない
    def example2(self):
        assert True

# どちらも実行されない
class  Example2():
    def test_example1(self):
        assert True

    def example2(self):
        assert True