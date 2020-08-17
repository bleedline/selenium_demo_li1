import pytest


@pytest.mark.parametrize("test_input,expected",[("3+5",8),
                                                ("13+5",18),
                                                ("3*5",8),
                                                ])
def test_jisuan(test_input,expected):
    assert eval(test_input)==expected


test_data={'username':'admin','password':'root12345'}
excepted_result={'code':200,'info':'ok'}
@pytest.mark.parametrize("test_datal,excepted_resultl",[(test_data,excepted_result)])
def test_interface_hrm(test_datal,excepted_resultl):
    print(test_datal)
    print(excepted_resultl)
