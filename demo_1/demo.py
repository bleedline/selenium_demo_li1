from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='F:\python\profile\selenium_demo_li\driver\chromedriver.exe')
driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/auth/login")

driver.find_element_by_id("txtUsername").send_keys('admin')
driver.find_element_by_id("txtPassword").send_keys('root1234')
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
assert 'Welcome Admin' == driver.find_element_by_id('welcome').text
assert 'Admin' in driver.find_element_by_id('welcome').text
driver.close()