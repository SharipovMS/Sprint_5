from locators import Locators
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:

    def test_log_in_using_Log_in_to_account_button_on_main_page(self, wd):
        wd.find_element(*Locators.account_enter).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        check_text = wd.find_element(*Locators.button_order).text
        WebDriverWait(wd, 3).until(expected_conditions.element_to_be_clickable(check_text))
        assert check_text == 'Оформить заказ'

    def test_login_personal_account_button(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        check_text = wd.find_element(*Locators.button_order).text
        WebDriverWait(wd, 3).until(expected_conditions.element_to_be_clickable(check_text))
        assert check_text == 'Оформить заказ'

    def test_log_in_button_registration_form(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.registr_button).click()
        wd.find_element(*Locators.enter_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        check_text = wd.find_element(*Locators.button_order).text
        WebDriverWait(wd, 3).until(expected_conditions.element_to_be_clickable(check_text))
        assert check_text == 'Оформить заказ'

    def test_login_button_in_password_recovery_form(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.recover_pass).click()
        wd.find_element(*Locators.enter_button).click()
        wd.find_element(*Locators.email_input).send_keys(email)
        wd.find_element(*Locators.password_input).send_keys(password)
        wd.find_element(*Locators.enter_click).click()
        check_text = wd.find_element(*Locators.button_order).text
        WebDriverWait(wd, 3).until(expected_conditions.element_to_be_clickable(check_text))
        assert check_text == 'Оформить заказ'

