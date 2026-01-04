import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/#")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Sachin Tendulkar")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
time.sleep(5)
result = driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']")
for i in result:
    print(i.text)

driver.find_element(By.XPATH,"//div[@class='wikipedia-search-results']/div[1]/a").click()
time.sleep(5)
windowhandle1 = driver.window_handles
driver.switch_to.window(windowhandle1[1])
assert "Sachin Tendulkar - Wikipedia" in driver.title
print("switch to child window")
time.sleep(5)


driver.switch_to.window(windowhandle1[0])
assert "Automation Testing Practice" in driver.title
print("switch to parent window")
time.sleep(5)
