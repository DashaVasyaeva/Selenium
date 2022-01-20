from selenium import webdriver
import time
import math
import unittest

def site_check (link):
    browser = webdriver.Chrome()
    browser.get(link)

class TestLogin:
    self.x = ""
    self.ss = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ]

    @pytest.mark.parametrize('links', "self.ss")
    def test_guest_should_see_login_link(self, browser, links):
        

7.  Первые 2 строчки как в предыдущем примере 2 предпоследние с небольшим изменением в link

8. browser.implicity_wait(10)

9. Ищем textarea

10. Записываем в неё через  send_key(str(math.log(int(time.time())))  с примера

11. Через WebDriverWait EC.element_to_be_clickable находим класс кнопку

12. нажимаем на кнопку

13. Через WebDriverWait EC.visibility_of_element_located().text находим класс сообщения и текст его присваиваем переменной

14. Проверяем не равен ли он !="Correct!"

15. если не равен то добавляем в переменную с 4 пункта посредством self. название переменной += с пункта 13 пунк переменная и print()

16. assert с пункта13  переменная == False проверяем

if __name__ == "__main__":
    unittest.main()
    browser.quit()




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

class TestRgst(unittest.TestCase):
    def test_rgst1(self):
        self.assertEqual(site_check("http://suninjuly.github.io/registration1.html"), 
        "Congratulations! You have successfully registered!", "Регистрация не удалась")
        
        
    def test_rgst2(self):
        self.assertEqual(site_check("http://suninjuly.github.io/registration2.html"), 
        "Congratulations! You have successfully registered!", "Регистрация не удалась")



