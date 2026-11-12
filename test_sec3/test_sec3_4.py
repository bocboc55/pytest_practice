# モジュールに対する前処理と後処理

# 前処理
def setup_module(module):
    print("setup_module")

# 後処理
def teardown_module(module):
    print("teardown_module")

def test_hello_world():
    print("hello world!")

def test_pytest():
    print("pytest")

class Testexample():

    def test_hello_world(self):
        print("hello world!")

    def test_pytest(self):
        print("pytest")

'''
$ pytest test_sec3_4.py -s

platform linux -- Python 3.12.3, pytest-9.2.0, pluggy-1.7.0
rootdir: /home/b24a0185/private_repo/pytest_practice
collected 4 items                                                                                                                                    

test_sec3_4.py setup_module
hello world!
.pytest
.hello world!
.pytest
.teardown_module
'''