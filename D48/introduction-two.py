from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r'C:\Users\ayush\Downloads\Applications\chromedriver-win64\chromedriver.exe'
URL = 'https://www.python.org/'


service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)

# finding element by name
# bar = driver.find_element(By.NAME, 'q')
# print(bar.get_attribute('placeholder'))

# finding nested element
# links = driver.find_element(By.TAG_NAME, 'a')
# for link in links:
# print(links.text)

# x-path
# elem = driver.find_element(
#     By.XPATH, '/html/body/div/footer/div[1]/div/ul/li[1]/ul/li[1]/a')

# print(elem.get_attribute('href'))


# -------- Upcoming Events --------

title = driver.find_element(By.CSS_SELECTOR, '.event-widget h2').text
eventsTime = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
eventsName = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul li a')

data = {}
data[title] = []
for i in range(len(eventsTime)):
    data[title].append({eventsTime[i].text: eventsName[i].text})

# using list and dictionary comprehension
# data = {title: [{t.text: n.text} for t, n in zip(eventsTime, eventsName)]}


print(data)
