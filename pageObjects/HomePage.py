from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    menu = (By.CSS_SELECTOR, "a[id='menu-toggle']")
    login = (By.CSS_SELECTOR, "a[href*='login']")
    title = (By.CSS_SELECTOR, "h1")
    footer = (By.CSS_SELECTOR, "footer")

    def getMenu(self):
        return self.driver.find_element(*HomePage.menu)

    def getLogin(self):
        return self.driver.find_element(*HomePage.login)

    def getTitle(self):
        return self.driver.find_element(*HomePage.title)

    def getFooter(self):
        return self.driver.find_element(*HomePage.footer)
