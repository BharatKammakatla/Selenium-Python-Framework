from pageObjects.HomePage import HomePage
from utilities.Base import Base


class Test_Validate_Footer(Base):

    def test_validateFooter(self):
        hp = HomePage(self.driver)

        assert hp.getFooter().is_displayed()
