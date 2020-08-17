from selenium.webdriver.support import expected_conditions as EC
from demo_1.page.Basepage import Basepage
from demo_1.page.login import Login
from demo_1.page.vacancy import Vacancy
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(Basepage):
    def enter_username(self,username):
        WebDriverWait(self.driver,100).\
        until(lambda driver:driver.find_element(*Login.txtUsername))
        element = self.driver.find_element(*Login.txtUsername)
        element.click()
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*Login.txtPassword))
        element = self.driver.find_element(*Login.txtPassword)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        element_click = self.driver.find_element(*Login.btnLogin)
        element_click.click()

    def result_login_sucess(self):
        WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located(Vacancy.welcome_link))
        return self.driver.find_element(*Vacancy.welcome_link).text

