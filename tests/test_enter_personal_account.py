from conftest import init_webdriver as wd
from locators import Locators
from time import sleep

class TestPersonalAccount:
    def test_transfer_to_personal_account(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys('sharipov_5@gmail.com')
        wd.find_element(*Locators.password_input).send_keys('hSTwgB83')
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        sleep(2)
        check_account_page = wd.find_element(*Locators.check_account_page).text
        assert check_account_page == 'В этом разделе вы можете изменить свои персональные данные'
        # wd.find_element(*Locators.)

    def test_transfer_to_constructor(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys('sharipov_5@gmail.com')
        wd.find_element(*Locators.password_input).send_keys('hSTwgB83')
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.constructor).click()
        sleep(1)
        check_text = wd.find_element(*Locators.button_order).text
        assert check_text == 'Оформить заказ'

    def test_transfer_to_logo(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys('sharipov_5@gmail.com')
        wd.find_element(*Locators.password_input).send_keys('hSTwgB83')
        wd.find_element(*Locators.enter_click).click()
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.logo).click()
        sleep(1)
        check_text = wd.find_element(*Locators.button_order).text
        assert check_text == 'Оформить заказ'

