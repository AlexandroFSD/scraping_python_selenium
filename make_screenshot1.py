# import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the Chrome driver (browser) in headless mode
driver = webdriver.Chrome(options=options)

# visit your target site
url = "https://scrapingcourse.com/ecommerce/product/abominable-hoodie"
driver.get(url)

# get the element using the ID selector
summary_element = driver.find_element(By.CLASS_NAME, "product")

# screenshot the selected element
summary_element.screenshot("screenshots/one_elem_screenshot.png")
