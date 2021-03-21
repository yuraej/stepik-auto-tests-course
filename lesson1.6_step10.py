from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"   # test must be right
    browser = webdriver.Edge('../drivers/msedgedriver.exe')
    browser.get('http://suninjuly.github.io/registration2.html')  # test must be wrong

    # Ваш код, который заполняет обязательные поля
    input_first = browser.find_element_by_tag_name("[placeholder='Input your first name']")
    input_first.send_keys('test')
    input_second = browser.find_element_by_tag_name("[placeholder='Input your last name']")
    input_second.send_keys('test')
    input_third = browser.find_element_by_css_selector("[placeholder='Input your email']")
    input_third.send_keys('test')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
