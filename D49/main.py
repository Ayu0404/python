from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('LINKEDIN_USERNAME')
pswd = os.getenv('LINKEDIN_PSWD')

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4085169510&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
CHROME_DRIVER_PATH = r'C:\Users\ayush\Downloads\Applications\chromedriver-win64\chromedriver.exe'

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)

# signin button click
time.sleep(5)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()


input_username = driver.find_element(By.ID, 'username')
input_username.click()
input_username.send_keys(username)

input_pswd = driver.find_element(By.ID, 'password')
input_pswd.click()
input_pswd.send_keys(pswd)

time.sleep(50)
