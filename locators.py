from selenium.webdriver.common.by import By

class Locators:
    '''Авторизация на сайте'''
    account_button = (By.XPATH, "//a[@href = '/account']")
    email_input = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    password_input = (By.XPATH, './/input[@name="Пароль"]')
    enter_click = (By.XPATH, './/button[contains(text(),"Войти")]')

    '''Кнопка Войти'''
    enter_button = (By.XPATH, ".//a[text()='Войти']")

    '''Кнопка Выход'''
    exit_button = (By.XPATH, './/button[contains(text(),"Выход")]')

    '''Проверка текста ВХОД'''
    text_enter = (By.XPATH, ".// h2[text() = 'Вход']")

    '''Кнопка зарегистрироваться'''
    registr_button = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    '''Кнопка восстановить пароль'''
    recover_pass = (By.XPATH, ".//a[text()='Восстановить пароль']")

    '''Кнопка Войти в аккаунт'''
    account_enter = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт']")

    '''Поле ввода имени'''
    name_input = (By.XPATH, './/input[@name="name"]')

    '''Оформить заказ'''
    button_order = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    '''Переход в личный кабинет'''
    account_autorize_button = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    '''Переход в конструктор'''
    constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    '''Клик на логотип'''
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    '''Переход по кнопке выйти из ЛК'''
    exit_button = (By.XPATH, "//button[contains(text(),'Выход')]")

    '''Переход Булки'''
    bread = (By.XPATH, "//span[text() = 'Булки']")

    '''Проверка перехода на Булки'''
    bread_check = (By.XPATH, ".// h2[text() = 'Булки']")

    '''Переход Соусы'''
    sauce = (By.XPATH, "//span[text() = 'Соусы']")

    '''Проверка перехода на Соусы'''
    sauce_check = (By.XPATH, ".// h2[text() = 'Соусы']")

    '''Переход Начинки'''
    filling = (By.XPATH, "//span[text() = 'Начинки']")

    '''Проверка перехода на Начинки'''
    filling_check = (By.XPATH, ".// h2[text() = 'Начинки']")

    '''Проверка личного кабинета'''
    check_account_page = (By.XPATH, ".//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")
