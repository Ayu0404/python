from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://en.wikipedia.org/wiki/Main_Page'
CHROME_DRIVER_PATH = r'C:\Users\ayush\Downloads\Applications\chromedriver-win64\chromedriver.exe'

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)

total_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(total_articles.text)

# to click
total_articles.click()
