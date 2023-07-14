import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Downloaded/saved Chrome Driver path
chrome_driver_path = "/broswer_drivers/chromedriver_linux64/chromedriversss"

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(service=ChromeService(chrome_driver_path)) # driver using driver_path

# Below approach will download the appropriate ChromeDriver version based on your Chrome browser version and ensure compatibility. so no need to worry about path and all
# for diff. diff. browsers, you can go here and change it accordingly: https://pypi.org/project/webdriver-manager/
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # automatically downloads the chrome driver

class DemoFindById():
    def locate_by_id(self):
        driver.get("https://secure.yatra.com/social/common/yatra/register")

        login_xpath_relative = "//input[@id='login-input']"
        login_xpath_by_id = "login-input"
        css_login_id  = "#login-input"
        driver.find_element(By.XPATH, login_xpath_relative).send_keys("Test1@test1.com")
        driver.find_element(By.ID, login_xpath_by_id).send_keys("Test1@test1.com")
        driver.find_element(By.CSS_SELECTOR, css_login_id).send_keys("Test1@test1.com")

findbyid = DemoFindById()
findbyid.locate_by_id()

# Rest of your code...

# Add a delay of 5 seconds
time.sleep(4)

# Close the browser
driver.quit()