from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )



from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.ID, "showInput")
    MESSAGE = (By.ID, "message")

    def enter_message(self, text):
        self.wait_for_element(self.MESSAGE_INPUT).send_keys(text)

    def click_submit(self):
        self.wait_for_element(self.SUBMIT_BUTTON).click()

    def get_displayed_message(self):
        return self.wait_for_element(self.MESSAGE).text



from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):

    CHECKBOX = (By.ID, "isAgeSelected")

    def check_option(self, index=0):
        self.wait_for_element(self.CHECKBOX).click()

    def uncheck_option(self, index=0):
        self.wait_for_element(self.CHECKBOX).click()

    def is_option_checked(self, index=0):
        return self.wait_for_element(self.CHECKBOX).is_selected()




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):

    DROPDOWN = (By.ID, "select-demo")

    def select_day(self, day_name):
        Select(
            self.wait_for_element(self.DROPDOWN)
        ).select_by_visible_text(day_name)




from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InputFormPage(BasePage):

    NAME = (By.NAME, "name")

    EMAIL = (By.NAME, "email")

    PHONE = (By.NAME, "phone")

    ADDRESS = (By.NAME, "address")

    SUBMIT = (By.XPATH, "//button[@type='submit']")

    SUCCESS = (By.CLASS_NAME, "success-msg")

    def fill_form(self, name, email, phone, address):

        self.wait_for_element(self.NAME).send_keys(name)

        self.wait_for_element(self.EMAIL).send_keys(email)

        self.wait_for_element(self.PHONE).send_keys(phone)

        self.wait_for_element(self.ADDRESS).send_keys(address)

    def submit_form(self):

        self.wait_for_element(self.SUBMIT).click()

    def get_success_message(self):

        return self.wait_for_element(self.SUCCESS).text




from pages.simple_form_page import SimpleFormPage

def test_simple_form_submission(driver, base_url):

    page = SimpleFormPage(driver)

    page.navigate_to(base_url + "simple-form-demo")

    page.enter_message("Hello Selenium")

    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"



from pages.checkbox_page import CheckboxPage

def test_checkbox_demo(driver, base_url):

    page = CheckboxPage(driver)

    page.navigate_to(base_url + "checkbox-demo")

    page.check_option()

    assert page.is_option_checked()

    page.uncheck_option()

    assert not page.is_option_checked()



from pages.input_form_page import InputFormPage

def test_input_form_submit(driver, base_url):

    page = InputFormPage(driver)

    page.navigate_to(base_url + "input-form-demo")

    page.fill_form(

        "John",

        "john@gmail.com",

        "9876543210",

        "Chennai"

    )

    page.submit_form()

    assert "success" in page.get_success_message().lower()