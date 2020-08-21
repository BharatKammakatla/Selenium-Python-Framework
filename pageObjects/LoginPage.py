from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.CSS_SELECTOR, "input[name='username']")
    password = (By.CSS_SELECTOR, "input[name='password']")
    loginBtn = (By.CSS_SELECTOR, "button[id='btn-login']")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLoginBtn(self):
        return self.driver.find_element(*LoginPage.loginBtn)
