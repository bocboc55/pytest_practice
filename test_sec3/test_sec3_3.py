# 前処理と後処理のメソッド

class Testexample():

    # 前処理
    # 最初に一度だけ実行される
    @classmethod
    def setup_class(cls):
        print("setup_class")

    # 後処理
    # クラスのメソッドが全て実行された後に実行される
    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def test_example1(self):
        print("hello world!")

    def test_example2(self):
        print("pytest!")

'''
$ pytest test_sec3_3.py -s
platform linux -- Python 3.12.3, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/b24a0185/private_repo/pytest_practice
collected 2 items                                                                                                                                    

test_sec3_3.py setup_class
hello world!
.pytest!
.teardown_class
'''