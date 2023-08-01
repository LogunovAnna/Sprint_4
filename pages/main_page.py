from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    Order_Up_Button = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"  # Верхняя кнопка "Заказать" на главной странице
    Order_Header = By.XPATH, "//div[text()='Для кого самокат']"   # Заголовок "Для кого самокат" на странице оформления заказа
    Header = By.XPATH, "//div[text()='Самокат ']"  # Заголовок "Самокат на пару дней" на глайной странице
    Logo_Scooter = By.XPATH, "//img[@alt = 'Scooter']"   # Логотип "Самокат" в шапке
    Logo_Yandex = By.XPATH, "//img[@alt = 'Yandex']"   # Логотип "Яндекс" в шапке
    Logo_Dzen = By.XPATH, "//a[@aria-label='Логотип Дзен']"   # Логотип "Дзен" на странице в новом окне
    Questions_Header = By.XPATH, "//div[text()='Вопросы о важном']"  # Заголовок "Вопросы о важном" на глайной странице
    Questions = By.ID, 'accordion__heading-{}'  # Локатор воросов в разделе "Вопросы о важном"
    Answers = By.XPATH, "//div[@id = 'accordion__panel-{}']//p"

    def check_location_on_page(self, header):
        actually_header = self.driver.find_element(*self.Header).text
        assert header in actually_header

    def check_location_on_dzen(self, header):
        actually_header = self.driver.find_element(*self.Logo_Dzen).get_attribute('aria-label')
        assert actually_header == header

    def get_question(self, item):
        method, locator = self.Questions
        locator = locator.format(item)
        question = method, locator
        return question

    def get_answer(self, item):
        method, locator = self.Answers
        locator = locator.format(item)
        answer = self.driver.find_element(method, locator).text
        return answer



