from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TEXT_CONSTRUCTOR_PAGE,BLOCK_LOGIN_FORM, BUTTON_LOGIN, BUTTON_LOGOUT, BUTTON_PERSONAL_ACCOUNT, INPUT_LOGIN_EMAIL, INPUT_LOGIN_PASSWORD
from data import VALID_EMAIL, VALID_PASSWORD

def test_logout(driver):
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Ждём появления формы логина
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
    driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()

    # Ждём, пока вернёмся на страницу конструктора (успешный логин)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))

    # Переходим в личный кабинет
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()

    # Ждём появления кнопки "Выйти"
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(BUTTON_LOGOUT)).click()

    # Проверяем, что снова отобразилась форма авторизации
    auth_form = WebDriverWait(driver, 7).until(EC.visibility_of_element_located(BLOCK_LOGIN_FORM))
    assert auth_form.is_displayed()

