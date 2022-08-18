from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'

def get_x(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.ID, 'book')
    button.click()
    browser.implicitly_wait(3)
    x = browser.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap').text
    xx = get_x(x)
    field = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    field.send_keys(xx)
    subm = browser.find_element(By.CSS_SELECTOR, 'button#solve.btn.btn-primary')
    subm.click()






finally:
    time.sleep(120)
    browser.quit()
