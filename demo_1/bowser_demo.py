from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=
                          'F:\python\profile\selenium_demo_li\driver\chromedriver.exe')
# 进入某一个网页
driver.get("http://www.baidu.com")
driver.get("http://81.70.24.116/orangehrm/symfony/web/index.php/auth/login")
time.sleep(2)
# 回退
driver.back()
# 向前
driver.forward()
# 刷新
driver.refresh()
# 最大化窗口，为了找到元素。
driver.maximize_window()
# driver.minimize_window()
driver.set_window_position(500,500)
# 截屏
driver.save_screenshot("screeshoot_login.png")
time.sleep(2)

driver.close()
driver.quit()
