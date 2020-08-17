import pytest


def setup_module():
    print("这个方法是一个文件开始只执行一次")


def teardown_module():
    print("这个方法是一个文件结束只执行一次")


def setup_function():
    print("这个方法是每个不在类中的方法前执行一次")


def teardown_function():
    print("这个方法是每个不在类中的方法后执行一次")


def test_fuction_01():
    assert 1 == 1
    print("这是一个不在类中的测试方法1")


def test_fuction_02():
    assert 1 + 2 == 3
    print("这是一个不在类中的测试方法2")

class TestClassDemo():

    def setup_class(self):
        print("\n这个是在类前执行一次")

    def teardown_class(self):
        print("这是在类后执行一次")

    def setup_method(self):
        print("在每个类中方法前执行一次")

    def teardown_method(self):
        print("在每个类中方法后执行一次")

    def test_method_01(self):
        print("这 个是类中的 方法01")

    def test_method_02(self):
        print("\n这 个是类中的 方法02")

if __name__ == '__main__':
    pytest.main(['-s','test_pytest_framework.py'])
