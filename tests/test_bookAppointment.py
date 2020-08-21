from selenium.webdriver.support.select import Select

from pageObjects.BookingPage import BookingPage
from pageObjects.ConfPage import ConfPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Base import Base
from actions.Actions import Actions


class Test_BookAppointment(Base):

    def test_bookAppointment(self):

        hp = HomePage(self.driver)
        lp = LoginPage(self.driver)
        ba = BookingPage(self.driver)
        cp = ConfPage(self.driver)
        actions = Actions(self.driver)

        #hp.getMenu().click()
        actions.click(hp.getMenu())
        #hp.getLogin().click()
        actions.click(hp.getLogin())
        #lp.getUsername().send_keys("John Doe")
        actions.sendKeys(lp.getUsername(), "John Doe")
        #lp.getPassword().send_keys("ThisIsNotAPassword")
        actions.sendKeys(lp.getPassword(), "ThisIsNotAPassword")
        #lp.getLoginBtn().click()
        actions.click(lp.getLoginBtn())

        #ddelement = Select(ba.getFacilityDD())
        #ddelement.select_by_value('Hongkong CURA Healthcare Center')
        actions.selectFromDD(ba.getFacilityDD(), 'Hongkong CURA Healthcare Center')

        #ba.getReadmission().click()
        actions.click(ba.getReadmission())
        #ba.getVisitDate().send_keys("24/08/2021")
        actions.sendKeys(ba.getVisitDate(), "22/08/2021")
        #ba.getComment().send_keys("This is a test comment")
        actions.sendKeys(ba.getComment(), "This is a test comment !")
        #ba.getBookBtn().click()
        actions.click(ba.getBookBtn())

        assert cp.getTitle().is_displayed()