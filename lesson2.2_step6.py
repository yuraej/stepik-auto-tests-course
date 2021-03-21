import time
from selenium import webdriver
from math import log, sin, e

link = 'http://suninjuly.github.io/execute_script.html'


def calc(num):
    return str(log(abs(12 * sin(int(num))), e))


try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get(link)
    num = browser.find_element_by_id('input_value').text
    answer = calc(num)
    browser.execute_script("window.scrollBy(0, 100);")   # javascript прокрутка страницы вниз
    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn-primary').click()


finally:
    time.sleep(5)
    browser.quit()
