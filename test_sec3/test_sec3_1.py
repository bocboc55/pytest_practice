# テストの前処理と後処理

# 前処理
# testの関数の前に実行される
def setup_function(function):
    print("setup_function")

# 後処理
# testの関数の後に実行される
def teardown_function(function):
    print("teardown_function")

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")

'''
実行結果

$ pytest test_sec3_1.py -s

platform linux -- Python 3.12.3, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/b24a0185/private_repo/pytest_practice
collected 2 items                                                                                                                                    

test_sec3_1.py setup_function
hello world!
.teardown_function
setup_function
pytest
.teardown_function

'''