import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
alert1 = driver.find_element(By.XPATH,"//button[text()='Simple Alert']")
alert1.click()
switcher1 = driver.switch_to.alert
time.sleep(3)
switcher1.accept()
time.sleep(3)
alert2 = driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']")
alert2.click()
time.sleep(3)
switcher1.accept()
time.sleep(3)
alert3 = driver.find_element(By.XPATH,"//button[text()='Prompt Alert']")
alert3.click()
time.sleep(3)
switcher1.send_keys("Chaubey")
time.sleep(3)
switcher1.accept()
time.sleep(3)



