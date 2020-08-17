import pytest
@pytest.fixture(scope='module',autouse=True)

def open_browser():
    print("打开浏览器，输入人力登录页")
    yield
    print("退出，关闭浏览器")

@pytest.fixture(autouse=True)
def open_first(open_browser):
    print("这是首页")

@pytest.mark.usefixtures("login")
def test_add_jobtitle():
    print("这个添加功能，需要登录")

def test_search_goods():
    print("这个搜索功能不需要登录")

def test_cart_pay(login):
    print("支付，登录")