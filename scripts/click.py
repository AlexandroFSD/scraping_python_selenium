# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize an instance of the chrome driver (headless browser)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# open the target website
url = "https://www.scrapingcourse.com/javascript-rendering"
driver.get(url)

# get the brand name element
brand_name = driver.find_element(By.CSS_SELECTOR, ".brand-name")

# perform a click action
brand_name.click()

# screenshot the result page
driver.save_screenshot("screenshots/homepage-screenshot.png")

