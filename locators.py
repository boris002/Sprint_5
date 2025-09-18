from selenium.webdriver.common.by import By

# --- Главная страница ---
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
TEXT_CONSTRUCTOR_PAGE = (By.XPATH, "//button[text()='Оформить заказ']")

TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']")
TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
TEXT_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
TEXT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")

# --- Страница регистрации ---
INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD = (By.XPATH, "//input[@type='password' and @name='Пароль']")
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
LOGO_STELLAR = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")

# --- Личный кабинет ---
BLOCK_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@class,'Account_link_active')]")
