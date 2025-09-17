import random
import string

def generate_email():
    digits = "".join(random.choices(string.digits, k=3))
    return f"test_user_01_{digits}@yandex.ru"

def generate_password():
    letters = string.ascii_letters + string.digits
    return "".join(random.choices(letters, k=8))
