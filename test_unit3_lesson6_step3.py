import pytest
from selenium import webdriver
import time
import math
import unittest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    empty_string = ""

    @pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])
    def test_enter_answer(self, browser, link):
        answer = str(math.log(int(time.time())))
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".textarea").send_keys(answer)
        browser.find_element_by_css_selector("button.submit-submission").click()
        check_text = browser.find_element_by_class_name("smart-hints__hint").text
        assert check_text == 'Correct!'


if __name__ == "__main__":
    unittest.main()
