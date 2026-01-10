import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[text()='Open Seperate Multiple Windows']").click()
driver.find_element(By.XPATH, "//button[@onclick='multiwindow()']").click()
multiple_windows = driver.window_handles
time.sleep(5)
print(multiple_windows)
driver.switch_to.window(multiple_windows[2])
driver.close()
time.sleep(5)
driver.switch_to.window(multiple_windows[1])
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id='btn2']").click()
time.sleep(5)