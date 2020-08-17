import pytest

test_user_data=[{'user':'linda','password':'root1234'},
                {'user':'lijian','password':'root1234'},
                {'user':'admin','password':''},
                ]

test_user_data2 = [{'q': 'selenium', 'count': 10, 'page': 1},
                   {'q': 'appium', 'count': 1, 'page': 1},
                   {'q': 'allure', 'count': 3, 'page': 1},
                   ]

@pytest.fixture(scope='module')
def login_r(request):
    user=request.param['user']
    password = request.param['password']
    print("这是要登陆的人名:",user)
    print("这是要登陆的密码:", password)
    return request.param
    # if password:
    #     return user
    # else:
    #     return False


@pytest.fixture(scope='module')
def query_param(request):
    return request.param


@pytest.mark.parametrize("query_param", test_user_data2, indirect=True)
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
def test_login(login_r,query_param):
    print("这个测试用例是要登陆的名字",login_r['user'],login_r['password'])
    print("这是测试用例中请求参数：", query_param)

