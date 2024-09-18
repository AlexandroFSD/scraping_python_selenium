# import the required libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# run Chrome in headless mode
options = Options()
options.add_argument("--headless")

# start a driver instance
driver = webdriver.Chrome(options=options)

# open the target website
url = "https://scrapingcourse.com/ecommerce/"
driver.get(url)


# define a function to get scroll dimensions
def get_scroll_dimension(axis):
    return driver.execute_script(
        f"return document.body.parentNode.scroll{axis}")


# get the page scroll dimensions
width = get_scroll_dimension("Width")
height = get_scroll_dimension("Height")

# set the browser window size
driver.set_window_size(width, height)

# get the full body element
full_body_element = driver.find_element(By.TAG_NAME, "body")

# take a full-page screenshot
full_body_element.screenshot("screenshots/full_page_screenshot.png")

# quit the browser
driver.quit()
