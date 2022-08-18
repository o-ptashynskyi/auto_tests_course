from select import select
from webbrowser import BackgroundBrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'

def get_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap').text
    xx = get_x(x)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    field.send_keys(xx)
    ch_box = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotCheckbox"]')
    ch_box.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    rad = browser.find_element(By.CSS_SELECTOR, 'label.form-check-label[for="robotsRule"]')
    rad.click()
    button.click()
    


finally:
    time.sleep(30)
    browser.quit()
