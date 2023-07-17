import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium_recaptcha_solver import RecaptchaSolver

# Downloaded/saved Chrome Driver path
chrome_driver_path = "/broswer_drivers/chromedriver_linux64/chromedriversss"

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path)) # driver using driver_path

# Maximize the window
driver.maximize_window()

# Below approach will download the appropriate ChromeDriver version based on your Chrome browser version and ensure compatibility. so no need to worry about path and all
# for diff. diff. browsers, you can go here and change it accordingly: https://pypi.org/project/webdriver-manager/
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # automatically downloads the chrome driver

class DemoFindById():

    def locate_by_id_css_selector(self):
        """ locate element by id and css selector """

        driver.get("https://secure.yatra.com/social/common/yatra/register")
        login_xpath_relative = "//input[@id='login-input']"
        login_by_id = "login-input"
        css_login_id  = "#login-input"
        driver.find_element(By.XPATH, login_xpath_relative).send_keys("Test1@test1.com")
        driver.find_element(By.ID, login_by_id).send_keys("Test1@test1.com")
        driver.find_element(By.CSS_SELECTOR, css_login_id).send_keys("Test1@test1.com")

    def locate_by_link(self):
        """ link/partial_link xpath and link/partial_link text """

        driver.get("https://www.yatra.com/")
        link_xpath = "//a[text()=' Yatra for Business ']"
        # link_xpath = "//a[contains(text(), ' Yatra for Business ')]"
        link_text = "Yatra for Business"
        driver.find_element(By.XPATH, link_xpath).click()
        driver.find_element(By.LINK_TEXT, link_text).click()


        partial_link_xpath = "//a[text()=' Yatra for Busin ']"
        partial_link_text = "Yatra for Busin"
        driver.find_element(By.XPATH, partial_link_xpath).click()
        driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text[1]).click()

    def locate_by_tag_class_name(self):
        """
        Locates an element by tag name and performs an action.

        It is designed to interact with web elements using their tag name, such as <input>, <button>, <div>, etc.

        Inputs:
        - None

        Behavior:
        - Navigates to the specified web page.
        - Locates the first occurrence of the specified tag name.
        - Performs an action (e.g., enters text, clicks, etc.) on the located element.

        Usage:
        - To locate the first input element on the registration page and enter an email address, call this function.

        Example:
        >>> locate_by_tag_class_name()
        """

        driver.get("https://secure.yatra.com/social/common/yatra/register")

        # It will find the first occurrence of an element with the specified tag name and performs the assigned action.
        tag_name = "input"
        tag_name_xpath = "//input[1]"
        driver.find_element(By.TAG_NAME, tag_name).send_keys("Test1@test1.com")
        driver.find_element(By.XPATH, tag_name_xpath).send_keys("Test1@test1.com")

        class_namee = "email-login-box"
        driver.find_element(By.CLASS_NAME, class_namee).send_keys("test@test.com")

    def locate_by_tag_names(self):
        
        driver.get("https://www.yatra.com/")
        tag_name = "a"
        tags_list = driver.find_elements(By.TAG_NAME, tag_name)
        print("➡ tags_list :", len(tags_list))
        for i in tags_list:
            print(i.text)
    
    def get_text_from_xpath(self):
        driver.get("https://www.yatra.com/")
        text_xpath = "//p[contains(text(), '7 Brilliant reasons Yatra should be your one-stop-shop!')]"
        get_text = driver.find_element(By.XPATH, text_xpath)
        print("➡ text :", get_text.text)

        pre_text = "7 Brilliant reasons Yatra should be your one-stop-shop!"
        if pre_text == get_text.text:
            print('success!')

    def get_attr_value(self):
        driver.get("https://www.yatra.com/")
        attr_xpath = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
        attr_value = driver.find_element(By.XPATH, attr_xpath)
        print("➡ attr_value get attr :", attr_value.get_attribute('type'))

    def autofill_captcha_simple(self):
        # driver.get("https://rsps100.com/vote/760")
        driver.get("https://www.google.com/recaptcha/api2/demo")

        # Wait for the page to load
        time.sleep(10)

        # Switch to the iframe
        iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
        driver.switch_to.frame(iframe)

        wait = WebDriverWait(driver, 20)
        checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='recaptcha-checkbox-border']")))
        checkbox.click()

    def autofill_captcha_complex(self):
        # driver.get("https://rsps100.com/vote/760")
        driver.get("https://www.google.com/recaptcha/api2/demo")

        # Wait for the page to load
        time.sleep(10)

        # Switch to the iframe
        iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
        driver.switch_to.frame(iframe)

        # Solve the CAPTCHA using RecaptchaSolver
        solver = RecaptchaSolver(driver=driver)
        solver.click_recaptcha_v2(iframe=iframe)

        # Switch back to the default content
        driver.switch_to.default_content()

        # Continue with the rest of your code...

        # Wait for the checkbox to be visible within the main content
        wait = WebDriverWait(driver, 20)
        checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='recaptcha-checkbox-border']")))

        # Click on the checkbox
        checkbox.click()
    
        

findbyid = DemoFindById()
# findbyid.locate_by_id_css_selector()
# findbyid.locate_by_link()
# findbyid.locate_by_tag_class_name()
# findbyid.locate_by_tag_names()
# findbyid.get_text_from_xpath()
# findbyid.get_attr_value()
findbyid.autofill_captcha_simple()
# findbyid.autofill_captcha_complex()


# Add a delay of x seconds
time.sleep(100)

# Close the browser
driver.quit()