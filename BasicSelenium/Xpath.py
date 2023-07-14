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
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # automatically downloads the chrome driver


class DemoFindById():
    def locate_by_id(self):
        driver.get("https://secure.yatra.com/social/common/yatra/register")

        # NOTE: I have written below code based on the HTML code I have put in "index.html" file. Check it out

        login_xpath_relative = "//input[@id='login-input']"
        login_xpath_by_id = "login-input"
        # driver.find_element(By.XPATH, login_xpath_relative).send_keys("Test1@test1.com")
        # driver.find_element(By.ID, login_xpath_by_id).send_keys("Test1@test1.com")


        # starts-with()
        # let's say login id is something like this "login-input-12345" where "12345" is dynamic and changes everytime/every page refresh.
        # in this case we use "starts_with" xpath. we can omit the dynamic part part and just include the static part 'login-input'.
        login_xpath_starts_with = "//input[starts-with(@id, 'login-input')]"
        # driver.find_element(By.XPATH, login_xpath_starts_with).send_keys("test@test.com")

        # contains() can have more than one element, we are only selecting the 1st one
        id_xpath_contains = "//input[contains(@id, 'login-')][1]"  
        # driver.find_element(By.XPATH, id_xpath_contains).send_keys('email@email.com')

        
        # <a href="https://www.yatra.com/online/terms-of-service.html" target="_blank" class="text-blue">Terms of Service</a>
        # text() - select the text
        text_xpath = "//a[text()='Terms of Service']"
        a = "Terms of Service"
        # driver.find_element(By.XPATH, text_xpath).click()


        # "AND" and "OR" in xpath, also combination of "OR/AND" and "contains()" or any other selectors
        or_xpath = "//input[@type='text' or @name='login-input']"
        and_xpath = "//input[@type='text' and @name='login-input']"
        or_contains_xpath = "//input[@type='text' or contains(@name, 'user[username]')][1]"
        driver.find_element(By.XPATH, or_xpath).send_keys('sdfsdf@jkfdslf.com')
        submit_button = "//button[@id='login-continue-btn']"
        driver.find_element(By.XPATH, submit_button).click()



        # Axes (Parent, Child, Self)
        # self select the same element (kind of write or don't write, won't make much difference)
        self_xpath = "//select[@id='signup-user-designation']//self::select"
        parent_xpath = "//select[@id='signup-user-designation']//parent::div"
        child_xpath = "//select[@id='signup-user-designation']//child::option"
        select_element = driver.find_element(By.XPATH, self_xpath)
        select = Select(select_element) # Message: Select only works on <select> elements, not on div
        select.select_by_visible_text('Mr.')


        # XPath - (ancestor, ancestor-or-self)
        ancestor_xpath = "//div[@class='login-form-container']//ancestor::div"
        ancestor_or_self_xpath = "//div[@class='login-form-container']//ancestor-or-self::div"
        driver.find_element(By.XPATH, ancestor_xpath)


        # XPath - (following, following-sibling) (no html reference added into index.html)
        follwing_xpath = "//option[@value='39']//follwing::option"
        following_sibling_xpath = "//option[@value='39']//follwing-sibling::option[@value='user']"
        driver.find_element(By.XPATH, follwing_xpath)



        # XPath - (preceding, preceding-sibling) (no html reference added into index.html)
        preceding_xpath = "//option[@value='355']//preceding::option[@value='93']"
        preceding_sibling_xpath = "//option[@value='39']//preceding-sibling::option"
        driver.find_element(By.XPATH, preceding_xpath)



findbyid = DemoFindById()
findbyid.locate_by_id()

# Add a delay of 5 seconds
time.sleep(5)

# Close the browser
# driver.quit()