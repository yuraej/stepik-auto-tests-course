import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link_step3 = 'http://suninjuly.github.io/selects1.html'


def calc(num1, num2):
    return num1 + num2


try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get(link_step3)
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    answer = calc(int(num1), int(num2))
    browser.find_element_by_tag_name('select')
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(answer))
    browser.find_element_by_css_selector('[type="submit"]').click()


finally:
    time.sleep(10)
    browser.quit()
