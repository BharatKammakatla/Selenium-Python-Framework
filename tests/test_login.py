import pytest

from actions.Actions import Actions
from pageObjects.BookingPage import BookingPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Base import Base
from utilities.Data import Data


class Test_Login(Base):

    def test_login(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        bp = BookingPage(self.driver)
        actions = Actions(self.driver)

        actions.click(hp.getMenu())
        log.info("Clicked on Menu")
        actions.click(hp.getLogin())
        log.info("Clicked on Login")
        actions.sendKeys(lp.getUsername(), getData["Username"])
        log.info("Entered Username")
        actions.sendKeys(lp.getPassword(), getData["Password"])
        log.info("Entered Password")
        actions.click(lp.getLoginBtn())
        log.info("Clicked on login button")

        assert bp.getTitle().is_displayed()
        log.info("Login successful")

    @pytest.fixture(params=Data.getTestData("TC1"))
    def getData(self, request):
        return request.param
