
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:

    Order_Up_Button = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"  # Верхняя кнопка "Заказать" на главной странице
    Order_Header = By.XPATH, "//div[text()='Для кого самокат']"  # Заголовок "Для кого самокат" на странице оформления заказа

    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        self.driver.find_element(*locator).click()

    def element_set_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def element_wait_for_load(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_enabled(self, locator):
        return self.driver.find_element(*locator).is_enabled()
