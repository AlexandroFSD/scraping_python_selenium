import time
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    start_time = time.time()  # Record script start time

    # initialize options for headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    # initialize Chrome driver
    driver = webdriver.Chrome(options=options)

    # target URL
    url = "https://www.scrapingcourse.com/infinite-scrolling"
    driver.get(url)

    # variables for infinite scroll
    last_height = driver.execute_script("return document.body.scrollHeight")
    num_scraped_products = 0  # Initialize product counter

    while True:
        # scroll and wait for loading
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        # get new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # check for new content
        if new_height == last_height:
            break

        last_height = new_height

    # extract products
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    extracted_products = []

    for product in products:
        product_data = {
            "Url": product.find_element(By.CSS_SELECTOR,
                                        ".product-item a").get_attribute(
                "href"),
            "Name": product.find_element(By.CSS_SELECTOR,
                                         ".product-name").text,
            "Image": product.find_element(By.CSS_SELECTOR,
                                          ".product-image").get_attribute(
                "src"),
            "Price": product.find_element(By.CSS_SELECTOR,
                                          ".product-price").text,
        }

        extracted_products.append(product_data)
        num_scraped_products += 1  # Increment product counter

    # calculate execution time
    end_time = time.time()
    total_time = end_time - start_time

    # print results
    print(f"Total scraped products: {num_scraped_products}")
    print(f"Script execution time: {total_time:.2f} seconds")

    # save data to JSON file (adjust filename as needed)
    # Set the path to the folder where the file will be saved
    folder_path = "scraped"
    file_name = "products.json"
    file_path = os.path.join(folder_path, file_name)

    # We create a folder if it does not exist yet
    os.makedirs(folder_path, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(extracted_products, f, indent=4)

    # quit Chrome driver
    driver.quit()


if __name__ == "__main__":
    main()
