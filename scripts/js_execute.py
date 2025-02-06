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
url = "https://www.scrapingcourse.com/ecommerce/product/abominable-hoodie/"
driver.get(url)

# passing values to your script
title = driver.execute_script("return document.title")
print(title)

# select the desired element
card = driver.find_element(By.ID, "tab-description")

# retrieve the y position of the selected element on the page
card_y_location = card.location["y"]

# "-100" to give some extra space and make
# ensure the screenshot is taken correctly
javaScript = f"window.scrollBy(0, {card_y_location}-100);"

# execute JavaScript
driver.execute_script(javaScript)

driver.save_screenshot("screenshots/js_scroll_el_screen.png")
