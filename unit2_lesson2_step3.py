from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
 
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
