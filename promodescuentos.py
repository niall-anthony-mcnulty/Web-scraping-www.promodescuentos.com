from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

DRIVER_PATH = "/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/Web Scraping/chromedriver"

options=Options()
options.headless = True
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.promodescuentos.com/")
print(driver.page_source)
driver.quit()







