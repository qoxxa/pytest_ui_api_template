from page.AuthPage import AuthPage
from page.MainPage import MainPage


def test_auth(browser):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("qooxxa", "wBC-2DP-NrL-3Vy")

    main_page = MainPage(browser)

    # info = main_page.get_account_info()

    # with allure.step("Проверить, что указаны данные пользователя"):
    # assert info == "Константин Погодин"

    with allure.step("Проверить, что URL " + current_url + "заканчивается на.... /boards"):
        assert auth_page.get_current_url().endswith("https://hd.kinopoisk.ru/")