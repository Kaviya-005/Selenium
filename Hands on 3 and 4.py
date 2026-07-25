Hands on 3


Task 1: Automation Decision and Test Case Selection
1. Criteria for Automation

1. Repetitive Test

Tests executed frequently should be automated.
Example: POST /api/courses/ regression test.

2. Stable Functionality

Features that rarely change are good automation candidates.
Example: Course creation API.

3. High-Risk Functionality

Critical business features should be automated.
Example: Course creation endpoint.

4. Data-Driven Testing

Tests requiring multiple input combinations are suitable for automation.
Example: Testing course creation with different course codes.

5. Time-Consuming Manual Tests

Long-running manual tests save effort through automation.
Example: Regression testing after every build.
Automation or Manual
Test Case	Decision	Reason
Regression testing of CRUD APIs	Automate	Executed frequently
Exploratory testing	Manual	Requires human observation
Performance testing (100 users)	Automate	Uses automation/load tools
Login UI testing	Automate	Stable and repetitive
Swagger documentation verification	Manual	Content changes frequently
Smoke testing after deployment	Automate	Fast validation after deployment
Test Automation ROI

Definition:
Automation ROI measures whether the time invested in automation is recovered through reduced manual execution effort.

Calculation

Automation Time = 4 hours = 240 minutes

Manual Execution = 30 minutes

Break-even Runs

240 ÷ 30 = 8 runs

After the 10th run, a 20% maintenance overhead applies.

Maintenance Time

30 × 20% = 6 minutes

Effective Time Saved

30 − 6 = 24 minutes per run
Flaky Test

A flaky test is a test that sometimes passes and sometimes fails without any code changes.

Example

Selenium clicks a button before it becomes clickable.

Ways to Prevent

Use Explicit Waits.
Avoid Thread.sleep().
Use stable locators (ID, Name).
Task 2: Automation Framework Types
Linear Framework

Description
Tests are executed sequentially in a single script.

Advantage

Easy to develop.

Disadvantage

Poor reusability.

Example

Simple login automation.
Modular Framework

Description
Application is divided into reusable modules.

Advantage

Reusable code.

Disadvantage

Requires planning.

Example

Separate Login, Dashboard and Course modules.
Data-Driven Framework

Description
Test data is stored separately (Excel, CSV, JSON).

Advantage

One script runs multiple datasets.

Disadvantage

Data management required.

Example

Login with 50 username/password combinations.
Keyword-Driven Framework

Description
Keywords represent actions like Login, Click, Logout.

Advantage

Non-technical users can create tests.

Disadvantage

Complex implementation.

Example

Excel sheet containing keywords.
Hybrid Framework

Description
Combination of Modular, Data-Driven and Keyword-Driven frameworks.

Advantage

Flexible and scalable.

Disadvantage

Initial setup is complex.

Example

Enterprise Selenium automation framework.
Recommended Framework

Hybrid Framework

Reason:

Supports reusable modules.
Supports multiple test data.
Easy maintenance.
Suitable for both technical and non-technical users.



Hands on 4



Task 1: Selenium Architecture
"""
Selenium Components

1. WebDriver
   Controls the browser using browser drivers.

2. Selenium Grid
   Executes tests on multiple browsers and machines in parallel.

3. Selenium IDE
   Record-and-playback automation tool.
"""
Install
pip install selenium webdriver-manager
Basic Selenium Script
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground/")

print(driver.title)

driver.quit()
Implicit Wait
driver.implicitly_wait(10)

# Implicit wait is global.
# Explicit wait is preferred because it waits only for specific elements.
Headless Mode
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
Task 2: Navigation & Window Commands
Navigate
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element("link text","Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

driver.back()
Multiple Tabs
driver.execute_script(
'window.open("https://www.google.com");'
)

print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

print(driver.title)
Screenshot
driver.switch_to.window(driver.window_handles[0])

driver.save_screenshot("playground_screenshot.png")
Window Size
print(driver.get_window_size())

driver.set_window_size(1280,800)

# Consistent window size ensures
# reliable responsive UI testing.