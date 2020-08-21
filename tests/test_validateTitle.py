from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base


class Test_Validate_Title(Base):

    def test_validateTitle(self):
        hp = HomePage(self.driver)
        actions = Actions(self.driver)

        #actualTitle = hp.getTitle().text
        actualTitle = actions.getText(hp.getTitle())
        expectedTitle = "CURA Healthcare Service"

        assert actualTitle == expectedTitle
