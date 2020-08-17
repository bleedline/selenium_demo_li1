import unittest, sys
from selenium import webdriver
from demo_1.page.login_method import LoginPage
from demo_1.page.mian_method import Main
from demo_1.page.add_method import Add_page
from demo_1.page.Basepage import Basepage


class Login(unittest.TestCase):
    def setUp(self):
        # 需要就自己驱动(地址写工程地址)
        # sys.path.append('/Users/lindafang/PycharmProjects/SeleniumAutoDemo/')
        self.driver = webdriver.Chrome(executable_path=
                                       'F:\\python\\profile\\selenium_demo_li\\driver\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://81.70.24.116/"
        self.base_page = Basepage(self.driver)

    def test_login(self):
        driver = self.driver
        driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/recruitment/addJobVacancy")
        login_page = LoginPage(driver)
        login_page.enter_username("admin")
        login_page.enter_password("root1234")
        login_page.click_login()
        assert 'Admin' in login_page.result_login_sucess()
        # self.base_page.save_picture('1.png')

    def test_enter(self):
        driver = self.driver
        enter_page= Main(driver)
        enter_page.enter_recruitment()
        enter_page.enter_vacancy()

    def test_add(self):
        driver = self.driver
        add_page=Add_page(driver)
        add_page.click_add()
        add_page.addJobVacancy_jobTitle()
        add_page.addJobVacancy_name('hfgdgdgdf')
        add_page.addJobVacancy_hiringManager('crow w')
        add_page.click_save()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
