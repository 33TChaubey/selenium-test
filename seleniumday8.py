import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)
interactions=driver.find_element(By.XPATH, "//a[contains(text(), 'Interactions ')]")
draganddrop=driver.find_element(By.XPATH, "//a[contains(text(), 'Drag and Drop ')]")
static=driver.find_element(By.XPATH, "//a[contains(text(),'Static ')]")
action.move_to_element(interactions).perform()
time.sleep(5)
action.move_to_element(draganddrop).perform()
time.sleep(5)
static.click()
time.sleep(5)