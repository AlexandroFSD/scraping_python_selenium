# import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# instantiate a Chrome options object
options = webdriver.ChromeOptions()

# set the options to use Chrome in headless mode
options.add_argument("--headless=new")

# initialize an instance of the Chrome driver (browser) in headless mode
driver = webdriver.Chrome(options=options)

# visit your target site
driver.get("https://www.scrapingcourse.com/javascript-rendering")

# wait up to 5 seconds until the image card appears
element = WebDriverWait(driver, 5).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-item"))
)

# you are now sure that the product grid has loaded
# and can scrape it
products = driver.find_elements(By.CSS_SELECTOR, ".product-item")

extracted_products = []

for product in products:
    product_data = {
        "name": product.find_element(By.CSS_SELECTOR, ".product-name").text,
        "price": product.find_element(By.CSS_SELECTOR, ".product-price").text,
    }

    extracted_products.append(product_data)

print(extracted_products)

# release the resources allocated by Selenium and shut down the browser
driver.quit()
