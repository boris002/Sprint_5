from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BUTTON_LOGIN, BUTTON_PERSONAL_ACCOUNT, INPUT_LOGIN_EMAIL, INPUT_LOGIN_PASSWORD, LINK_FORGOT_PASSWORD, LINK_RECOVER_TO_LOGIN, TEXT_CONSTRUCTOR_PAGE, TEXT_RECOVER_HEADER
from data import VALID_EMAIL, VALID_PASSWORD

def test_login_via_password_recovery_form(driver):
    driver.find_element(*BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*LINK_FORGOT_PASSWORD).click()

    # Ожидание появления формы восстановления пароля
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TEXT_RECOVER_HEADER))

    # Возврат на форму логина
    driver.find_element(*LINK_RECOVER_TO_LOGIN).click()

    # Ожидание появления формы авторизации
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(INPUT_LOGIN_EMAIL)).send_keys(VALID_EMAIL)
    driver.find_element(*INPUT_LOGIN_PASSWORD).send_keys(VALID_PASSWORD)
    driver.find_element(*BUTTON_LOGIN).click()

    # Проверка загрузки страницы конструктора
    constructor_page = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TEXT_CONSTRUCTOR_PAGE))
    assert constructor_page.is_displayed()

