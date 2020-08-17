import allure
import pytest


@allure.feature("购物车模块")
class TestShopping():

    @allure.story("添加购物车")
    def test_add_shopping(self):
        login('lijain','lijain567')
        with allure.step("第一步，浏览商品"):
            allure.attach('商品一','手柄')
            allure.attach('商品一', 'ps4')
        with allure.step("第二步，点击商品添加"):
            pass
        with allure.step("第三步，验证商品添加成功"):
            allure.attach('期望结果','手柄成功添加到购物车')
            allure.attach('商品一', 'ps4成功添加到购物车')
            assert 'success'!='failed'

    @allure.story("编辑购物车")
    def test_edit_shopping(self):
        allure.attach('商品已下架','无法进行编辑')
        assert False

    @pytest.mark.skip(reason='本次不执行')
    @allure.story("清空购物车")
    def test_delete_shopping(self):
        pass


@allure.step("用户先登录")
def login(user,pwd):
    print(user,pwd)

