from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'

def get_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    butt = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn.btn-primary')
    butt.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap').text
    xx = get_x(x)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    field.send_keys(xx)
    sumb = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    sumb.click()



finally:
    time.sleep(30)
    browser.quit()
