from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://orteil.dashnet.org/experiments/cookie/'
CHROME_DRIVER_PATH = r'C:\Users\ayush\Downloads\Applications\chromedriver-win64\chromedriver.exe'

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)

cookie = driver.find_element(By.ID, 'cookie')


def money():
    return int(driver.find_element(By.ID, 'money').text)


while True:
    # helpers
    buyGrandma = driver.find_element(By.ID, 'buyGrandma')
    # buyFactory = driver.find_element(By.ID, 'buyFactory')
    # buyMine = driver.find_element(By.ID, 'buyMine')
    # buyShipment = driver.find_element(By.ID, 'buyShipment')

    # parent divs of helpers
    grandmas = driver.find_element(By.ID, 'grandmas')
    # factories = driver.find_element(By.ID, 'factories')

    # helper cost
    grandmaCost = int(driver.find_element(
        By.CSS_SELECTOR, '#buyGrandma b').text.split('-')[1])

    cookie.click()

    if money() > grandmaCost:
        buyGrandma.click()
        numGrandmas = int(driver.find_element(
            By.CSS_SELECTOR, '#buyGrandma .amount').text)
