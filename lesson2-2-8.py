from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'file.txt')

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    f_name = browser.find_element(By.NAME, 'firstname')
    f_name.send_keys('Oleksii')
    s_name = browser.find_element(By.NAME, 'lastname')
    s_name.send_keys('Ptashynskyi')
    mail = browser.find_element(By.NAME, 'email')
    mail.send_keys('test@mail.com')
    attach = browser.find_element(By.CSS_SELECTOR, 'input#file')
    attach.send_keys(file_path)
    subm = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    subm.click()
    


    


finally:
    time.sleep(30)
    browser.quit()
