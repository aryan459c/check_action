import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument("--headless")  # Required for GitHub Actions
option.add_argument("--disable-gpu")
option.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=option)
driver.get("https://google.com")

search_box = driver.find_element(By.CSS_SELECTOR, 'textarea[title="Search"]')
search_box.send_keys("Kodehash")
search_box.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
