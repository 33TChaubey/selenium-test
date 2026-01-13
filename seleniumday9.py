import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)
rows=driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
row = len(rows)
list1 = []
for i in range(2, row+1):
    a = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[4]")
    list1.append(a.text)
print(list1)