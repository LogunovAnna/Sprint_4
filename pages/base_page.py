
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

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

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
