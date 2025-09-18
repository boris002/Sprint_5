# Sprint_5
Регистрация
test_success_registration – проверяет успешную регистрацию пользователя с валидными данными.
test_registration_with_invalid_password – проверяет, что при вводе некорректного пароля отображается ошибка.

Вход в систему
test_login_from_main – проверяет вход через кнопку «Войти в аккаунт» на главной странице.
test_login_from_personal_account – проверяет вход через кнопку «Личный Кабинет».
test_login_via_registration_form – проверяет вход через кнопку «Войти» из формы регистрации.
test_login_via_password_recovery_form – проверяет вход через кнопку «Войти» из формы восстановления пароля.

Личный кабинет
test_open_personal_account – проверяет переход в личный кабинет после входа в систему.
test_logout – проверяет выход из аккаунта по кнопке «Выйти».
test_go_to_constructor_via_logo – проверяет переход в конструктор по клику на логотип Stellar Burgers из личного кабинета.

Конструктор
test_go_to_buns – проверяет переход в раздел «Булки».
test_go_to_sauces – проверяет переход в раздел «Соусы».
test_go_to_fillings – проверяет переход в раздел «Начинки».

Технологии:
selenium
pytest


consfest.py - фикстуры проекта
data.py - Данные для входа
locators.py - Содеражит Xpath на элементы страницы
utils/generators.py - генерация почты и пароля.
 