# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Vacancy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='F:\\python\\profile\\selenium_demo_li\\driver\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://81.70.24.116"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_vacancy(self):
        driver = self.driver
        driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/recruitment/addJobVacancy")
        driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("root1234")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_xpath("//a[@id='menu_recruitment_viewRecruitmentModule']/b").click()
        driver.find_element_by_id("menu_recruitment_viewJobVacancy").click()
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("addJobVacancy_jobTitle").click()
        Select(driver.find_element_by_id("addJobVacancy_jobTitle")).select_by_visible_text("56dfflff")
        driver.find_element_by_id("addJobVacancy_jobTitle").click()
        driver.find_element_by_id("addJobVacancy_name").click()
        driver.find_element_by_id("addJobVacancy_name").clear()
        driver.find_element_by_id("addJobVacancy_name").send_keys("dfs553995")
        driver.find_element_by_id("addJobVacancy_name").click()
        driver.find_element_by_id("addJobVacancy_name").clear()
        driver.find_element_by_id("addJobVacancy_name").send_keys("dfs553995996")
        driver.find_element_by_id("addJobVacancy_hiringManager").click()
        driver.find_element_by_id("addJobVacancy_hiringManager").clear()
        driver.find_element_by_id("addJobVacancy_hiringManager").send_keys("c")
        driver.find_element_by_xpath("//div[4]/ul/li").click()
        driver.find_element_by_xpath("//form[@id='frmAddJobVacancy']/fieldset/ol").click()
        driver.find_element_by_id("btnSave").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
