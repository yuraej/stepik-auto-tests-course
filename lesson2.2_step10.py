import time
from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test')   # добавляем к этому пути имя файла

try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get('http://suninjuly.github.io/file_input.html')
    browser.find_element_by_name('firstname').send_keys("test")
    browser.find_element_by_name('lastname').send_keys('test')
    browser.find_element_by_name('email').send_keys('test')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector('button.btn-primary').click()

finally:
    time.sleep(4)
    browser.quit() 
