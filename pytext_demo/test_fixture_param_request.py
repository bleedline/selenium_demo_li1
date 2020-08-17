import pytest


@pytest.fixture(params=[1,2,3,'lijian'])
def t_data(request):
    print('这个是提供数据的方法')
    return request.param


def test_one(t_data):
    print(f'test_data is {t_data}')