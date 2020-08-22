import pytest

from actions.Actions import Actions
from pageObjects.BookingPage import BookingPage
from pageObjects.ConfPage import ConfPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Base import Base
from utilities.Data import Data


class Test_BookAppointment(Base):

    def test_bookAppointment(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        ba = BookingPage(self.driver)
        cp = ConfPage(self.driver)
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

        actions.selectFromDD(ba.getFacilityDD(), getData["Facility"])
        log.info("Selected Facility option")

        actions.click(ba.getReadmission())
        log.info("Selected Readmission")
        actions.sendKeys(ba.getVisitDate(), getData["Visit Date"])
        log.info("Selected Date")
        actions.sendKeys(ba.getComment(), getData["Comment"])
        log.info("Entered comment")
        actions.click(ba.getBookBtn())
        log.info("Clicked on book button")

        assert cp.getTitle().is_displayed()
        log.info("Booking Successful")

    @pytest.fixture(params=Data.getTestData("TC2"))
    def getData(self, request):
        return request.param