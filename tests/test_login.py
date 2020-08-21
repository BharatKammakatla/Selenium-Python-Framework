from actions.Actions import Actions
from pageObjects.BookingPage import BookingPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Base import Base


class Test_Login(Base):

    def test_login(self):
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        bp = BookingPage(self.driver)
        actions = Actions(self.driver)

        # hp.getMenu().click()
        actions.click(hp.getMenu())
        # hp.getLogin().click()
        actions.click(hp.getLogin())
        # lp.getUsername().send_keys("John Doe")
        actions.sendKeys(lp.getUsername(), "John Doe")
        # lp.getPassword().send_keys("ThisIsNotAPassword")
        actions.sendKeys(lp.getPassword(), "ThisIsNotAPassword")
        # lp.getLoginBtn().click()
        actions.click(lp.getLoginBtn())

        assert bp.getTitle().is_displayed()
