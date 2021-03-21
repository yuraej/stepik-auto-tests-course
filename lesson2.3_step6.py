from selenium import webdriver
from math import log, sin, e


def calc(num):
    return str(log(abs(12 * sin(int(num))), e))


try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('button.btn-primary').click()
    browser.switch_to.window(browser.window_handles[1])
    num = browser.find_element_by_id('input_value').text
    answer = calc(num)
    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_css_selector('button.btn-primary').click()
    print(browser.switch_to.alert.text[-18:-1])


finally:
    browser.quit()
