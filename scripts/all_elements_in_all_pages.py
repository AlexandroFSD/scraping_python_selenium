# import the required library
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def scrape_products(url):
    """Scrapes product data from all pages on the provided URL.
        Args:
            url: The base URL of the product listing.
        Returns:
            A list of dictionaries containing product data (link,name,price,image).
    """
    options = Options()
    options.add_argument("--headless")

    # Record start time
    start_time = time.time()

    all_products = []
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)

        # Extract last page number (moved inside the function)
        page_numbers_text = driver.find_element(By.XPATH,
                                                "//*[@id='pagination']").text
        last_page_number = re.findall(r'\d+', page_numbers_text)[-1]
        print("Last page number:", last_page_number)

        # Loop through all pages
        for page_number in range(1, int(last_page_number) + 1):
            current_url = f"{url}page/{page_number}"
            driver.get(current_url)
            print(f"Page URL: {current_url}")
            print("Page Title:", driver.title)

            parent_elements = driver.find_elements(By.XPATH,
                                                   "//a[@class='woocommerce"
                                                   "-LoopProduct-link "
                                                   "woocommerce-loop"
                                                   "-product__link']")
            for parent_element in parent_elements:
                product_link = parent_element.get_attribute("href")
                product_name = parent_element.find_element(By.XPATH,
                                                           ".//h2").text
                product_price = parent_element.find_element(By.XPATH,
                                                            ".//span").text

                # Extract image source
                image_element = parent_element.find_element(By.XPATH, ".//img")
                image_src = image_element.get_attribute("src")

                all_products.append({
                    "name": product_name,
                    "link": product_link,
                    "image": image_src,
                    "price": product_price
                })

                # Counting the number of scraped products
                total_products = len(all_products)
    # calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time

    print(
        f"Successfully scraped {total_products} products.")
    print(f"Execution Time: {execution_time:.2f} seconds")
    return all_products


# Define the target URL here
target_url = "https://www.scrapingcourse.com/ecommerce/"
all_products_data = scrape_products(target_url)
print(all_products_data)
