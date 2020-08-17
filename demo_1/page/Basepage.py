

class Basepage(object):
    def __init__(self,driver):
        self.driver =driver

    def save_picture(self,filepath):
        self.driver.save_screenshot(filepath)
