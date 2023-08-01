
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import user_1
from data import user_2
from data import rent_data_1
from data import rent_data_2


@pytest.mark.parametrize('order_locator', OrderPage.order_locator)
def test_order_button_get_order_page(driver, order_locator):
    """ Тест кнопок Заказать. ОР открывается форма заказа"""
    scooter_order_page = OrderPage(driver)
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.go_to_element(order_locator)
    scooter_order_page.element_click(order_locator)
    scooter_order_page.element_wait_for_load(MainPage.Order_Header)
    assert scooter_order_page.element_is_enabled(MainPage.Order_Header)


@pytest.mark.parametrize('user_data', [user_1, user_2])
def test_input_user_data_get_about_rent_page(driver, user_data):
    """ Тест ввода данных пользователя. ОР перезод на следующую страницу """
    scooter_order_page = OrderPage(driver)
    scooter_order_page.get_order_page()
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.input_user_data(user_data)
    scooter_order_page.check_user_input('Про аренду')


@pytest.mark.parametrize('about_rent', [rent_data_1, rent_data_2])
def test_input_rent_data_successful_ordering(driver, about_rent):
    """ Тест ввода данныых об оренде. ОР открытие окна с подтверждением оформления заказа"""
    scooter_order_page = OrderPage(driver)
    scooter_order_page.get_order_page()
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.input_user_data(user_1)
    scooter_order_page.element_wait_for_load(scooter_order_page.About_Rent_Header)
    scooter_order_page.input_rent_data(about_rent)
    scooter_order_page.check_rent_input('Заказ оформлен')
