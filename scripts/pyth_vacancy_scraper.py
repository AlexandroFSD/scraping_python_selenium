from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
import time

# ChromeDriver path (update the path as per your setup)
chrome_driver_path = "chromedriver.exe"

# Configure WebDriver
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=service, options=options)


def extract_jobs(url):
    """
        Extracts job postings from the given URL.

        Args:
            url (str): The URL of the job listings page.

        Returns:
            list: A list of dictionaries containing job details.
        """
    driver.get(url)
    jobs = []

    try:
        # Wait for the vacancy list to load
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "vacancyListId"))
        )

        # Loop to load all vacancies
        while True:
            try:
                # Wait for the "Load More" button and click it
                load_more_button = WebDriverWait(driver, 5).until(
                    ec.presence_of_element_located(
                        (By.CSS_SELECTOR, ".more-btn a"))
                )
                load_more_button.click()
                time.sleep(2)  # Wait for the new vacancies to load
            except Exception:
                print("No more 'Load More' button found.")
                break

        # Extract job details
        job_elements = driver.find_elements(By.CSS_SELECTOR, "li.l-vacancy")

        for job_element in job_elements:
            try:
                title = job_element.find_element(By.CSS_SELECTOR,
                                                 ".title a.vt").text
                job_url = job_element.find_element(By.CSS_SELECTOR,
                                                   ".title a.vt").get_attribute(
                    "href")
                date = job_element.find_element(By.CSS_SELECTOR, ".date").text

                company = job_element.find_element(By.CSS_SELECTOR, ".company").text
                # Check for salary; it might not always be present
                try:
                    salary = job_element.find_element(By.CSS_SELECTOR,
                                                      ".salary").text
                except:
                    salary = None

                # Add the job details to the list
                jobs.append({
                    "date": date,
                    "title": title,
                    "url": job_url,
                    "company": company,
                    "salary": salary
                })
            except Exception as e:
                print(f"Error extracting job: {e}")

    except Exception as e:
        print(f"Error accessing the page: {e}")

    return jobs


# Define URL
base_url = "https://jobs.dou.ua/vacancies/?remote&category=Python"

# Extract jobs
job_data = extract_jobs(base_url)

# Save data to a JSON file
output_file = "pyth_remote.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(job_data, f, ensure_ascii=False, indent=4)

print(f"Extracted {len(job_data)} job postings. Data saved to {output_file}.")

# Close the driver
driver.quit()
