
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BLOCK_PERSONAL_ACCOUNT, BUTTON_LOGIN, BUTTON_LOGIN_MAIN, BUTTON_LOGOUT, BUTTON_PERSONAL_ACCOUNT, INPUT_LOGIN_EMAIL, INPUT_LOGIN_PASSWORD, LINK_LOGIN_TO_REGISTER, LINK_RECOVER_TO_LOGIN, LINK_REGISTER_TO_LOGIN, TEXT_CONSTRUCTOR_PAGE
from data import VALID_EMAIL, VALID_PASSWORD

class TestLogin:

    def test_login_from_main(self,driver):
        # Открываем форму логина через кнопку "Войти в аккаунт"
        driver.find_element(*BUTTON_LOGIN_MAIN).click()
    
        # Вводим данные и логинимся
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
        driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
        driver.find_element(*BUTTON_LOGIN).click()

        # Ждём появления страницы конструктора
        constructor_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()


    def test_login_from_personal_account(self,driver):
        # Переходим в личный кабинет
        driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

         # Вводим данные для авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
        driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
        driver.find_element(*BUTTON_LOGIN).click()

        # Ждём появления страницы конструктора
        constructor_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()

    def test_login_via_registration_form(self, driver):
        # Открываем страницу авторизации через "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(BUTTON_PERSONAL_ACCOUNT)).click()

        # Ждём появления ссылки "Зарегистрироваться" и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_LOGIN_TO_REGISTER)).click()

        # Ждём появления ссылки "Войти" на странице регистрации и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LINK_REGISTER_TO_LOGIN)).click()

        # Ждём появления поля email на форме авторизации и заполняем его
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
        driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
        driver.find_element(*BUTTON_LOGIN).click()

        # Ждём появления конструктора
        constructor_page = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()