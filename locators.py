from selenium.webdriver.common.by import By

# --- Главная страница ---
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
TEXT_CONSTRUCTOR_PAGE = (By.XPATH, "//button[text()='Оформить заказ']")

TAB_BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']")
TAB_SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
TEXT_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')
TEXT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")

# --- Страница регистрации ---
INPUT_NAME = (By.XPATH, ".//fieldset[1]//input")
INPUT_EMAIL = (By.XPATH, ".//fieldset[2]//input")
INPUT_PASSWORD = (By.XPATH, ".//fieldset[3]//input")
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
LINK_REGISTER_TO_LOGIN = (By.XPATH, "//a[text()='Войти']")
TEXT_REGISTRATION_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

# --- Страница авторизации ---
INPUT_LOGIN_EMAIL = (By.XPATH, "//input[@name='name']")
INPUT_LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
TEXT_LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
BLOCK_LOGIN_FORM = (By.XPATH, "//div[@class='Auth_login__3hAey']")
LINK_LOGIN_TO_REGISTER = (By.XPATH, "//a[@href='/register' and contains(@class,'Auth_link')]")

# --- Восстановление пароля ---
LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
TEXT_RECOVER_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
LINK_RECOVER_TO_LOGIN = (By.XPATH, "//a[text()='Войти']")

# --- переход по логотипу ---
LOGO_STELLAR = (By.XPATH, "//header//nav//div/a")

# --- Личный кабинет ---
BLOCK_PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account/profile' and contains(@class,'Account_link_active')]")
