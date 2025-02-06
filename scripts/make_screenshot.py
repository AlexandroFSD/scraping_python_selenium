# import the required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the Chrome driver (browser) in headless mode
driver = webdriver.Chrome(options=options)

# visit your target site
url = "https://www.scrapingcourse.com/javascript-rendering"
driver.get(url)

# Identify the element containing product information (replace
# 'product-container' with the actual selector)
product_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
)

# Wait for all elements within the product container to be visible (optional)
WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-grid "
                                                            ".product-item"))
)


# # ... wait for dynamic content to load
# # wait up to 10 seconds until the document is fully ready
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script(
        "return document.readyState") == "complete"
)

# Now the product elements should be fully loaded, screenshot the visible
# part of the page
driver.save_screenshot("screenshots/visible_part_screenshot.png")

# release the resources allocated by Selenium and shut down the browser
driver.quit()
