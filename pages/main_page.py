from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    Header = By.CLASS_NAME, "Home_Header__iJKdX"   # Заголовок "Самокат на пару дней" на глайной странице
    Logo_Scooter = By.CLASS_NAME, "Header_LogoScooter__3lsAR"   # Логотип "Самокат" в шапке
    Logo_Yandex = By.CLASS_NAME, "Header_LogoYandex__3TSOI"   # Логотип "Яндекс" в шапке
    Logo_Dzen = By.XPATH, "//a[@aria-label='Логотип Дзен']"   # Логотип "Дзен" на странице в новом окне
    Questions_Header = By.XPATH, "//div[text()='Вопросы о важном']"  # Заголовок "Вопросы о важном" на глайной странице
    Questions = By.ID, 'accordion__heading-{}'  # Локатор воросов в разделе "Вопросы о важном"
    Answers = By.ID, 'accordion__panel-{}'  # Локатор ответов в разделе "Вопросы о важном"

    def check_location_on_page(self, header):
        actually_header = self.driver.find_element(*self.Header).text
        assert header in actually_header

    def check_location_on_dzen(self, header):
        actually_header = self.driver.find_element(*self.Logo_Dzen).get_attribute('aria-label')
        assert actually_header == header

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_question(self, item):
        method, locator = self.Questions
        locator = locator.format(item)
        question = method, locator
        return question

    def get_answer(self, item):
        method, locator = self.Answers
        locator = locator.format(item)
        answer = By.ID, locator
        return answer



