from pageObjects.HomePage import HomePage
from utilities.Base import Base


class Test_Validate_Footer(Base):

    def test_validateFooter(self):
        log = self.getLogger()
        hp = HomePage(self.driver)

        assert hp.getFooter().is_displayed()
        log.info("Footer validation successful")
