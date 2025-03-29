from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

# Use the Service class to specify the chromedriver path
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com/")
print(driver.title)
driver.quit()
