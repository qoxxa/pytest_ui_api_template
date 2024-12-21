import pytest
import allure
from selenium import webdriver

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()