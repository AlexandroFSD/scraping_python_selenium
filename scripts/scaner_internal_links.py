import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def scrape_internal_links(url):
    """Collects internal links to goods from all pages.

  Args:
      url: Basic URL of the first page.

  Returns:
      List of unique internal links to goods.
  """
    options = Options()
    options.add_argument("--headless")

    all_product_links = set()
    processed_pages = 0
    start_time = time.time()  # Correct the start time

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)

        # Extracting the number of the last page
        page_numbers_text = driver.find_element(By.XPATH,
                                                "//*[@id='pagination']").text
        last_page_number = int(re.findall(r'\d+', page_numbers_text)[-1])

        # Cycle on all pages
        for page_number in range(1, last_page_number + 1):
            current_url = f"{url}page/{page_number}"
            driver.get(current_url)
            processed_pages += 1

            # Search for items with links to goods
            parent_elements = driver.find_elements(By.XPATH,
                                                   "//a[@class='woocommerce"
                                                   "-LoopProduct-link "
                                                   "woocommerce-loop"
                                                   "-product__link']")

            # Collecting all links to goods from this page
            for parent_element in parent_elements:
                product_link = parent_element.get_attribute("href")
                all_product_links.add(product_link)

    end_time = time.time()  # Correct completion time
    elapsed_time = end_time - start_time  # Calculate the execution time

    print(f"General processing {processed_pages} pages.")
    print(f"Found {len(all_product_links)} unique links.")
    print(f"Fulfillment time: {elapsed_time:.2f} seconds.")

    return list(all_product_links)


# An example of use
base_url = "https://www.scrapingcourse.com/ecommerce/"
all_links = scrape_internal_links(base_url)

print(all_links)
