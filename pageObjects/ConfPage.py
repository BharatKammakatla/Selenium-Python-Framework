from selenium.webdriver.common.by import By


class ConfPage:

    def __init__(self, driver):
        self.driver = driver


    title = (By.CSS_SELECTOR, "h2")

    def getTitle(self):
        return self.driver.find_element(*ConfPage.title)