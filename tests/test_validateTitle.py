import pytest

from actions.Actions import Actions
from pageObjects.HomePage import HomePage
from utilities.Base import Base
from utilities.Data import Data


class Test_Validate_Title(Base):

    def test_validateTitle(self, getData):
        log = self.getLogger()
        hp = HomePage(self.driver)
        actions = Actions(self.driver)

        actualTitle = actions.getText(hp.getTitle())
        expectedTitle = getData["Title"]

        assert actualTitle == expectedTitle
        log.info("Title validation successful")

    @pytest.fixture(params=Data.getTestData("TC3"))
    def getData(self, request):
        return request.param
