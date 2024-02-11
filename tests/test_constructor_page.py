from conftest import init_webdriver as wd
from locators import Locators
from time import sleep

class TestConstructorPage:
    def test_constructor_transfer_sauce(self, wd):
        wd.find_element(*Locators.sauce).click()
        check_text_sauce = wd.find_element(*Locators.sauce_check).text
        assert check_text_sauce == 'Соусы'

    def test_constructor_transfer_bread(self, wd):
        wd.find_element(*Locators.filling).click()
        wd.find_element(*Locators.bread).click()
        check_text_bread = wd.find_element(*Locators.bread_check).text
        assert check_text_bread == 'Булки'

    def test_constructor_transfer_filling(self, wd):
        wd.find_element(*Locators.filling).click()
        check_text_filling = wd.find_element(*Locators.filling_check).text
        assert check_text_filling == 'Начинки'