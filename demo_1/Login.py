# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='F:\\python\\profile\\selenium_demo_li\\driver\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "http://81.70.24.116"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/auth/login")
        driver.find_element_by_xpath("//div[@id='divUsername']/span").click()
        driver.find_element_by_id("txtUsername").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("root1234")
        driver.find_element_by_id("btnLogin").click()
        menu_admin_viewAdminModule = driver.find_element_by_id("menu_admin_viewAdminModule")
        menu_admin_Job = driver.find_element_by_id("menu_admin_Job")
        menu_admin_viewJobTitleList = driver.find_element_by_id("menu_admin_viewJobTitleList")
        ActionChains(driver).move_to_element(menu_admin_viewAdminModule).move_to_element(menu_admin_Job).click(menu_admin_viewJobTitleList).perform()
        # driver.find_element_by_xpath("//a[@id='menu_admin_viewJobTitleList']/font/font").click()
        driver.find_element_by_id("btnAdd").click()

        driver.find_element_by_id("jobTitle_jobTitle").click()
        driver.find_element_by_id("jobTitle_jobTitle").clear()
        driver.find_element_by_id("jobTitle_jobTitle").send_keys("56dfflff")
        driver.find_element_by_id("jobTitle_jobDescription").click()
        driver.find_element_by_id("jobTitle_jobDescription").clear()
        driver.find_element_by_id("jobTitle_jobDescription").send_keys("ffgdf56gfd6453")
        # driver.find_element_by_id("jobTitle_jobSpec").click()
        # driver.find_element_by_id("jobTitle_jobSpec").clear()
        driver.find_element_by_id("jobTitle_jobSpec").send_keys("F:\\python\\profile\\selenium_demo_li\\filter\\demo.txt")
        driver.find_element_by_id("btnSave").click()
        # driver.find_element_by_id("ohrmList_chkSelectRecord_144").click()
        # driver.find_element_by_id("btnDelete").click()
        # driver.find_element_by_id("dialogDeleteBtn").click()
        # driver.find_element_by_xpath("//table[@id='resultTable']/tbody/tr[8]/td[2]/a/font/font").click()
        # driver.find_element_by_id("btnSave").click()
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_xpath("//div[@id='welcome-menu']/ul/li[3]/a/font/font").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
