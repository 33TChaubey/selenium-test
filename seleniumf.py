import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.durgasoft.com/registration.asp")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Trilokinath")
ph_no = 56465465464
driver.find_element(By.XPATH,"//input[@id='ph_no']").send_keys(ph_no)
time.sleep(5)