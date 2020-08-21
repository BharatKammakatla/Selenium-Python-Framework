from selenium.webdriver.common.by import By


class BookingPage:

    def __init__(self, driver):
        self.driver = driver

    title = (By.CSS_SELECTOR, "h2")
    facilityDD = (By.CSS_SELECTOR, "select[id=combo_facility]")
    readmission = (By.CSS_SELECTOR, "input[id=chk_hospotal_readmission]")
    medicaid = (By.CSS_SELECTOR, "input[id=radio_program_medicaid]")
    visitDate = (By.CSS_SELECTOR, "input[id=txt_visit_date]")
    comment = (By.CSS_SELECTOR, "textarea[id=txt_comment]")
    bookBtn = (By.CSS_SELECTOR, "button[id=btn-book-appointment]")

    def getTitle(self):
        return self.driver.find_element(*BookingPage.title)

    def getFacilityDD(self):
        return self.driver.find_element(*BookingPage.facilityDD)

    def getReadmission(self):
        return self.driver.find_element(*BookingPage.readmission)

    def getMedicaid(self):
        return self.driver.find_element(*BookingPage.medicaid)

    def getVisitDate(self):
        return self.driver.find_element(*BookingPage.visitDate)

    def getComment(self):
        return self.driver.find_element(*BookingPage.comment)

    def getBookBtn(self):
        return self.driver.find_element(*BookingPage.bookBtn)
