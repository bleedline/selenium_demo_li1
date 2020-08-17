import allure
import pytest
import logging

@allure.step("测试步骤1：两个字符串相加：{0},{1}")
def str_add(str1,str2):
    print('hello',str1,str2)
    if not isinstance(str1,str):
        return  f"{str1}不是字符串"
    if not isinstance(str2,str):
        return  f"{str2,str}不是字符串"
    return str1 + str2

@allure.description("测试两个相加的各种情况")
@allure.severity("critical")
@allure.issue("http://81.70.24.116:8088/zentao/bug-view-26.html")
@allure.testcase("http://cn.bing.com")
@pytest.mark.parametrize("partone,parttwo",
                         [('linda','fang'),
                          (4,54),
                          ("我是linda","我是最厉害的"),
                          (888,'linda')
                          ],
                         ids=["letter",
                              "decimal",
                              "unicode",
                              "mix"
                              ])

def test_stradd_case(partone,parttwo):
    logging.info("我们要进行两个东西的相加，把相加可能遇到的情况都测试一遍")
    paras=vars()
    allure.attach(f"用例参数{paras}")
    res=str_add(partone,parttwo)
    allure.attach("返回结果","{0}".format(res))
    with allure.step(f"2、测试步骤：返回结果验证{res}=={partone+parttwo}"):
        allure.attach('<html><body>这是个网页，页面显示结果信息可能</body></html>',
                      '这是报错信息',allure.attachment_type.HTML)
        assert res==partone+parttwo
