from selenium.webdriver.support.select import Select
from demo_1.page.add import Add
from demo_1.page.Basepage import Basepage
from selenium.webdriver.support.wait import WebDriverWait

class Add_page(Basepage):
    def click_add(self):
        element = self.driver.find_element(*Add.btnAdd)
        element.click()

    def addJobVacancy_jobTitle(self):
        element= Select(self.driver.find_element(*Add.addJobVacancy_jobTitle)).select_by_index(4)
        element.click()


    def addJobVacancy_name(self, JobVacancy_name):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*Add.addJobVacancy_name))
        element = self.driver.find_element(*Add.addJobVacancy_name)
        element.click()
        element.clear()
        element.send_keys(JobVacancy_name)


    def addJobVacancy_hiringManager(self, hiringManager):
        WebDriverWait(self.driver, 10) \
            .until(lambda driver: driver.find_element(*Add.addJobVacancy_hiringManager))
        element = self.driver.find_element(*Add.addJobVacancy_hiringManager)
        element.click()
        element.clear()
        element.send_keys(hiringManager)


    def click_save(self):
        element_click = self.driver.find_element(*Add.btnSave)
        element_click.click()