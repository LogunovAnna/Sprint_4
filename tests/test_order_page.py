
import pytest
from pages.order_page import OrderPage


@pytest.mark.parametrize('order_locator', OrderPage.order_locator)
def test_order_button_get_order_page(driver, order_locator):
    """ Тест кнопок Заказать. ОР открывается форма заказа"""
    scooter_order_page = OrderPage(driver)
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.go_to_element(order_locator)
    scooter_order_page.element_click(order_locator)
    scooter_order_page.element_wait_for_load(scooter_order_page.Order_Header)
    assert scooter_order_page.element_is_enabled(scooter_order_page.Order_Header)


@pytest.mark.parametrize('user_data', ['user_data_1', 'user_data_2'])
def test_input_user_data_get_about_rent_page(driver, user_data, request: pytest.FixtureRequest):
    """ Тест ввода данных пользователя. ОР перезод на следующую страницу """
    data = request.getfixturevalue(user_data)
    scooter_order_page = OrderPage(driver)
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.element_click(scooter_order_page.Order_Up_Button)
    scooter_order_page.element_wait_for_load(scooter_order_page.Order_Header)
    scooter_order_page.input_user_data(data)
    scooter_order_page.check_user_input('Про аренду')


@pytest.mark.parametrize('about_rent', ['about_rent_data_1', 'about_rent_data_2'])
def test_input_rent_data_successful_ordering(driver, about_rent, request: pytest.FixtureRequest, user_data_1):
    """ Тест ввода данныых об оренде. ОР открытие окна с подтверждением оформления заказа"""
    rent_data = request.getfixturevalue(about_rent)
    scooter_order_page = OrderPage(driver)
    scooter_order_page.element_click(scooter_order_page.Cookie_Button)
    scooter_order_page.element_click(scooter_order_page.Order_Up_Button)
    scooter_order_page.element_wait_for_load(scooter_order_page.Order_Header)
    scooter_order_page.input_user_data(user_data_1)
    scooter_order_page.element_wait_for_load(scooter_order_page.About_Rent_Header)
    scooter_order_page.input_rent_data(rent_data)
    scooter_order_page.check_rent_input('Заказ оформлен')





