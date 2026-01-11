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
dragdrop=driver.find_element(By.XPATH, "//a[contains(text(), 'Drag and Drop ')]")
static=driver.find_element(By.XPATH, "//a[contains(text(),'Static ')]")
action.move_to_element(interactions).perform()
action.move_to_element(dragdrop).perform()
static.click()


driver.get("https://testautomationpractice.blogspot.com/")
doubleclickbutton=driver.find_element(By.XPATH, "//button[text()='Copy Text']")
action.scroll_to_element(doubleclickbutton).perform()
action.double_click(doubleclickbutton).perform()

drag=driver.find_element(By.XPATH, "//div[@id='draggable']")
drop=driver.find_element(By.XPATH, "//div[@id='droppable']")
action.drag_and_drop(drag, drop).perform()
time.sleep(5)
