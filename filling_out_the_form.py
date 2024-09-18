# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize an instance of the chrome driver (headless browser)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# initialize an instance of the chrome driver (browser)
# driver = webdriver.Chrome()

# open the target website
url = "https://www.scrapingcourse.com/login"
driver.get(url)

# retrieve the form elements
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit-button")

# filling out the form elements
email_input.send_keys("admin@example.com")
password_input.send_keys("password")

# submit the form and log in
submit_button.click()
