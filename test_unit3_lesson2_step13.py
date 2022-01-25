from selenium import webdriver
import time
import unittest

def site_check (link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector('.first_block input.first').send_keys("Ivan")
    browser.find_element_by_css_selector('.first_block input.second').send_keys("Petrov")
    browser.find_element_by_css_selector('.first_block input.third').send_keys("fgh@mail.ru")
        
    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # находим элемент, содержащий текст
    welcome_text = browser.find_element_by_tag_name("h1").text

    time.sleep(5)

    return welcome_text

    browser.quit()

class TestRgst(unittest.TestCase):
    def test_rgst1(self):
        self.assertEqual(site_check("http://suninjuly.github.io/registration1.html"), 
        "Congratulations! You have successfully registered!", "Регистрация не удалась")
        
        
    def test_rgst2(self):
        self.assertEqual(site_check("http://suninjuly.github.io/registration2.html"), 
        "Congratulations! You have successfully registered!", "Регистрация не удалась")


if __name__ == "__main__":
    unittest.main()
