import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C://Users//chaub//OneDrive//Desktop//chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@ng-model='FirstName']").send_keys('Chandan')
driver.find_element(By.XPATH, "//input[@ng-model='LastName']").send_keys('Sharma')
driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys('Hyderabad')
driver.find_element(By.XPATH, "//input[@ng-model='EmailAdress']").send_keys('Hyderabad132@gmail.com')
driver.find_element(By.XPATH, "//input[@ng-model='Phone']").send_keys('9164654656')
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@value='Cricket']").click()
driver.find_element(By.XPATH,"//div[@id='msdd']").click()
time.sleep(2)
listoptions = driver.find_elements(By.XPATH, "//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']/li")
for i in listoptions:
    print(i.text)
    if "Danish" in i.text:
        i.click()
    else:
        pass
time.sleep(2)
select = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
select.select_by_visible_text("India")
time.sleep(5)


