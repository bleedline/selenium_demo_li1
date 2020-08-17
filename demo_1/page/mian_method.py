from demo_1.page.vacancy import Vacancy
from demo_1.page.Basepage import Basepage
from selenium.webdriver.support.wait import WebDriverWait

class Main(Basepage):
    def enter_recruitment(self):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*Vacancy.recruitment))
        element = self.driver.find_element(*Vacancy.recruitment)
        element.click()

    def enter_vacancy(self):
        element_click = self.driver.find_element(*Vacancy.Vacancy)
        element_click.click()
