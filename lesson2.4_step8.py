from math import log, sin, e
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(num):
    return str(log(abs(12 * sin(int(num))), e))


try:
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # задаем явное ожидание до наступления события: цена = 100, затем жмем кнопку Book
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_id('solve').click()
    print(browser.switch_to.alert.text[-18:-1])

finally:
   browser.quit()
