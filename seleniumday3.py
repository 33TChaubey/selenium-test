import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.durgasoft.com/registration.asp")
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME, "a")
