Hands on 5

Task 1: Locator Strategies
ID
driver.find_element(By.ID, "user-message")
Name
driver.find_element(By.NAME, "message")
Class Name
driver.find_element(By.CLASS_NAME, "form-control")
Tag Name
driver.find_element(By.TAG_NAME, "input")
XPath (Absolute)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/input")
XPath (Relative)
driver.find_element(By.XPATH, "//input[@id='user-message']")
CSS Selectors
By ID
driver.find_element(By.CSS_SELECTOR, "#user-message")
By Attribute
driver.find_element(By.CSS_SELECTOR, "input[name='message']")
Parent → Child
driver.find_element(By.CSS_SELECTOR, "div > input")
XPath using text()
driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)
XPath using contains()
driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)
Preferred Locator Ranking
Rank	Locator	Reason
1	ID	Unique, fastest
2	Name	Simple and readable
3	CSS Selector	Fast and flexible
4	Relative XPath	Flexible
5	Class Name	May not be unique
6	Absolute XPath	Breaks easily if HTML changes
Task 2: Explicit Waits
Visibility Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver,10).until(

EC.visibility_of_element_located(

(By.CSS_SELECTOR,".alert-success")

)

)

assert "successfully" in driver.find_element(
By.CSS_SELECTOR,
".alert-success"
).text
Using time.sleep()
import time

time.sleep(3)

Why avoid it?

Always waits the full time.
Slower execution.
Makes tests flaky.
Element Clickable
WebDriverWait(driver,10).until(

EC.element_to_be_clickable(

(By.ID,"showInput")

)

).click()

Difference

visibility_of_element_located() → Element is visible.
element_to_be_clickable() → Element is visible and clickable.
Fluent Wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

wait = WebDriverWait(

driver,

10,

poll_frequency=0.5,

ignored_exceptions=[NoSuchElementException]

)

wait.until(

EC.presence_of_element_located(

(By.ID,"table")

)

)




Hands on 6




Install
pip install pytest pytest-html
test_playground.py
def test_simple_form_submission(driver):
    pass

def test_checkbox_demo(driver):
    pass
conftest.py
import pytest

from selenium import webdriver

@pytest.fixture(scope="function")

def driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()
Simple Form Test
def test_simple_form_submission(driver):

    driver.get(
"https://www.lambdatest.com/selenium-playground/"
)

    driver.find_element(
    By.ID,
    "user-message"
    ).send_keys("Hello Selenium")

    driver.find_element(
    By.ID,
    "showInput"
    ).click()

    assert driver.find_element(
    By.ID,
    "message"
    ).text == "Hello Selenium"
Checkbox Test
def test_checkbox_demo(driver):

    checkbox = driver.find_element(
    By.ID,
    "isAgeSelected"
    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()
Parameterization
import pytest

@pytest.mark.parametrize(

"message",

["Hello",

"Selenium Automation",

"12345"]

)

def test_messages(driver,message):

    print(message)
Screenshot on Failure
def pytest_runtest_makereport(item,call):

    if call.excinfo is not None:

        driver.save_screenshot(

        "failure.png"

        )
HTML Report
pytest test_playground.py --html=report.html --self-contained-html
Base URL Fixture
@pytest.fixture(scope="session")

def base_url():

    return "https://www.lambdatest.com/selenium-playground/"
Dropdown Test
from selenium.webdriver.support.ui import Select

def test_dropdown_selection(driver):

    dropdown = Select(

    driver.find_element(
    By.ID,
    "select-demo"
    )

    )

    dropdown.select_by_visible_text(

    "Wednesday"

    )

    assert dropdown.first_selected_option.text == "Wednesday"
