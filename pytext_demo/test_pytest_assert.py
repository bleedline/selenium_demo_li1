import pytest
import sys


@pytest.mark.skipif(sys.platform=='win32',reason='windows系统下不运行')
@pytest.mark.skipif(sys.version_info<(3,6),reason="3.6版本以下不执行，你需求更高版本")
def test_assert_demo():
    assert {'name': 'linda', 'age': 18} == {'name': 'linda', 'age': 108}


def f():
    return 3

@pytest.mark.skip
def test_assert_1():
    assert f() == 4

environment="android"
@pytest.mark.skipif('environment=="android"',reason='android平台没有这个功能')
def test_assert_2():
    list1 = [1, 2, 3] * 50
    list2 = [1, 2, 3] * 100
    assert list1 == list2

def broken_fixture():
    print("开发这个模块没修改好")
    raise Exception("中断异常")

@pytest.mark.xfail
def test_boken_xfail():
    broken_fixture()