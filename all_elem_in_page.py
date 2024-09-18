# import the required library
import time
import os
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_and_save_products(url, folder_name="scraped",
                             csv_file="products.csv"):
    """Scrapes product data from page on the provided URL.
          Args:
              url: The target URL of the product listing.
          Returns: A list of dictionaries containing product data (link,name,
          image,price).
    """
    start_time = time.time()  # Record start time

    # initialize an instance of the chrome driver (headless browser)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        # visit your target site
        driver.get(url)

        # extract all the product containers
        products = driver.find_elements(By.CSS_SELECTOR, ".product")

        # declare an empty list to collect the extracted data
        extracted_products = []

        # loop through the product containers
        for product in products:
            # extract the elements into a dictionary using the CSS selector
            product_data = {
                "Url": product.find_element(
                    By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
                ).get_attribute("href"),
                "Name": product.find_element(By.CSS_SELECTOR,
                                             ".product-name").text,
                "Image": product.find_element(By.CSS_SELECTOR,
                                              ".product-image").get_attribute(
                    "src"
                ),
                "Price": product.find_element(By.CSS_SELECTOR, ".price").text,
            }

            # append the extracted data to the extracted_product list
            extracted_products.append(product_data)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Construct the full file path
        file_path = os.path.join(folder_name, csv_file)

        # write the extracted data to the CSV file
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            # write the headers
            writer = csv.DictWriter(file, fieldnames=["Url", "Name", "Image",
                                                      "Price"])
            writer.writeheader()
            # write the rows
            writer.writerows(extracted_products)

        print(f"Data has been written to {file_path}")

    except Exception as e:
        print(f"Error scraping data: {e}")

    finally:
        # calculate execution time
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.2f} seconds")

        # release resources
        driver.quit()


# URL you want to scrape
target_url = "https://www.scrapingcourse.com/ecommerce"
scrape_and_save_products(target_url)
