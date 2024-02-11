from conftest import init_webdriver as wd
from locators import Locators
from time import sleep

class TestExitAccount:
    def test_log_out_account(self, wd):
        wd.find_element(*Locators.account_button).click()
        wd.find_element(*Locators.email_input).send_keys('sharipov_5@gmail.com')
        wd.find_element(*Locators.password_input).send_keys('hSTwgB83')
        wd.find_element(*Locators.enter_click).click()
        sleep(1)
        wd.find_element(*Locators.account_button).click()
        sleep(1)
        wd.find_element(*Locators.exit_button).click()
        sleep(1)
        check_text_enter = wd.find_element(*Locators.text_enter).text
        assert check_text_enter == 'Вход'

