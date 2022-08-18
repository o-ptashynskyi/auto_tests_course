from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def get_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    but = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    but.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap').text
    xx = get_x(x)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    field.send_keys(xx)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()


finally:
    time.sleep(30)
    browser.quit()
