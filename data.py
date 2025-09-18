from utils.generators import generate_email, generate_password

# Ссылка на приложение
BASE_URL = "https://stellarburgers.nomoreparties.site"

# Валидные данные (зарегистрированный пользователь)
VALID_EMAIL = "Boris_Logvinov_30_567@yandex.ru"
VALID_PASSWORD = "pass123"

# Данные для регистрации
REG_NAME = "Тестовый Пользователь"
def get_reg_email():
    return generate_email()

def get_reg_password():
    return generate_password()

# Невалидные данные
INVALID_PASSWORD = "qwer"
