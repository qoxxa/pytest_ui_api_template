from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://passport.yandex.ru/auth?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fhd.kinopoisk.ru%252F%26uuid%3D54f3af97-a0c2-494c-b34d-3261b51ef3e4"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):

        # Ожидаем появления поля ввода логина
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-login")))

        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-login").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        # Ожидаем появления поля ввода пароля
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-passwd")))

        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-passwd").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        # Ожидаем появления логотипа
        # (убеждаемся что главная страница полностью загружена)
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-tid="NextLink"]')))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url