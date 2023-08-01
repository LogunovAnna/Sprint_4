
import pytest
from pages.main_page import MainPage
from data import answers


def test_click_logo_scooter_get_main_page(driver):
    """ Тест клика на логотип Самокат. ОР переход на главную страницу """
    scooter_main_page = MainPage(driver)
    scooter_main_page.element_click(scooter_main_page.Order_Up_Button)
    scooter_main_page.element_wait_for_load(scooter_main_page.Order_Header)
    scooter_main_page.element_click(scooter_main_page.Logo_Scooter)
    scooter_main_page.element_wait_for_load(scooter_main_page.Header)
    scooter_main_page.check_location_on_page('Самокат')


def test_click_logo_yandex_get_dzen_page(driver):
    """ Тест клика на логотип Яндекс. ОР открытие в новом окне страницы Дзен"""
    scooter_main_page = MainPage(driver)
    scooter_main_page.element_click(scooter_main_page.Logo_Yandex)
    scooter_main_page.switch_to_new_window()
    scooter_main_page.element_wait_for_load(scooter_main_page.Logo_Dzen)
    scooter_main_page.check_location_on_dzen('Логотип Дзен')


@pytest.mark.parametrize('questions_number', range(0, 8))
def test_click_question_get_answer(driver, questions_number):
    """ Тест раздела Вопросы о важном. ОР при клике на вопрос виден ответ"""
    scooter_main_page = MainPage(driver)
    scooter_main_page.go_to_element(scooter_main_page.Questions_Header)
    scooter_main_page.element_wait_for_load(scooter_main_page.Questions_Header)
    scooter_main_page.element_click(scooter_main_page.get_question(questions_number))
    assert answers[questions_number] in scooter_main_page.get_answer(questions_number)
