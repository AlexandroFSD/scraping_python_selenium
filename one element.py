# import the required library
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_product_data(url):
    """Scrapes one product data from page on the provided URL.

          Args:
              url: The target URL of the product listing.

          Returns: A list of dictionaries containing product data (link,name,
          image,price).
        """
    start_time = time.time()  # Record start time

    # initialize an instance of the chrome driver (browser)
    # driver = webdriver.Chrome()

    # initialize an instance of the Chrome driver (browser) in headless mode
    # instantiate a Chrome options object
    options = webdriver.ChromeOptions()
    # set the options to use Chrome in headless mode
    options.add_argument("--headless=new")
    # initialize an instance of the Chrome driver (browser) in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # visit your target site
        driver.get(url)

        # extract product data
        product_data = {
            "Url": driver.find_element(
                By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
            ).get_attribute("href"),
            "Name": driver.find_element(By.CSS_SELECTOR, ".product-name").text,
            "Image": driver.find_element(By.CSS_SELECTOR, ".product-image").
            get_attribute("src"),
            "Price": driver.find_element(By.CSS_SELECTOR, ".price").text,
        }

        # print the extracted data
        print(product_data)

    except Exception as e:
        print(f"Error scraping data: {e}")

    finally:
        # calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.2f} seconds")

        # release the resources allocated by Selenium and shut down the browser
        driver.quit()


# visit your target site
target_url = "https://www.scrapingcourse.com/ecommerce/"
scrape_product_data(target_url)
