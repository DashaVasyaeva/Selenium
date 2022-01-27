from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    # Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements.
    # Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException,
    # которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат:
    # если ничего не было найдено, то он вернёт пустой список
    # и ваша программа перейдет к выполнению следующего шага в коде.
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
