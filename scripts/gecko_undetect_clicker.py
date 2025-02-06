# import the required library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
# anti-detect option for selenium
options.set_preference('dom.webdriver.enabled', False)
# disable all notifications
options.set_preference('dom.webnotifications.enabled', False)
# mute off volume
options.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox(options=options)

browser.get('https://www.fakenamegenerator.com/gen-random-us-us.php')

while True:
    button = browser.find_element(By.ID, 'genbtn')
    button.click()

    # Find element by xpath
    element = browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/h3").text

    print(element)

