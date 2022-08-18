from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    chest = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    chest_val = chest.get_attribute('valuex')
    y = calc(chest_val)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    field.send_keys(y)
    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()
    rad = browser.find_element(By.ID, 'robotsRule')
    rad.click()
    but = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    but.click()
    
    

finally:
    time.sleep(30)
    browser.quit()
