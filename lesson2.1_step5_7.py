import math
import time
from selenium import webdriver

link_step5 = 'http://suninjuly.github.io/math.html'  # ссылка для задачи шага 5
link_step7 = 'http://suninjuly.github.io/get_attribute.html'  # ссылка для задачи шага 7


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get(link_step7)
    search = browser.find_element_by_id("treasure")  # для шага 5 input_value
    x = search.get_attribute("valuex")  # для шага 5 search.text
    result = calc(x)
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
