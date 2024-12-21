from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    # Наводим на иконку профиля в верхнем правом углу
    # @allure.step("Открыть боковое меню")
    # def open_menu(self):
    #      self.__driver.find_element(By.CSS_SELECTOR, 'div[data-tid="caacc44c"]').moveTo()

    # Получаем информацию о пользователе:
    # @allure.step("Прочитать информацию о пользователе")
    # def get_account_info(self) -> list[str]:
    #      menu = self.__driver.find_element(By.XPATH,"//span[class='Text Text_typography_primary UserId-FirstLine' and text()='Константин Погодин']").text
        # Возвращаем имя и почту пользователя:
        #  return [menu]