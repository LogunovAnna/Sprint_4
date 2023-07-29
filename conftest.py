import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")

    yield driver
    driver.quit()


@pytest.fixture
def user_data_1():
    user_1 = ["Анна", "Логунова", "Московская обл., г.Ивантеевка, ул. Заречная, д. 1", "+905415106602"]
    return user_1


@pytest.fixture
def user_data_2():
    user_2 = ["Иван", "Иванов", "Москва", "+7990999999"]
    return user_2


@pytest.fixture
def about_rent_data_1():
    rent_data_1 = 'буду в жёлтом'
    return rent_data_1


@pytest.fixture
def about_rent_data_2():
    rent_data_2 = 'мы поедем мы помчимся'
    return rent_data_2
