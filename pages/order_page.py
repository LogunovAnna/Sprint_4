from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    Order_Down_Button = By.CLASS_NAME, "Home_FinishButton__1_cWm"   # Нижняя кнопка "Заказать" на главной странице
    order_locator = [BasePage.Order_Up_Button, Order_Down_Button]   # Объединенный локатор верхней и нижней кнопки "Заказать для параметризации"
    User_Name = By.XPATH, "//input[@placeholder='* Имя']"   # Поле ввода Имени на странице заказа
    User_Surname = By.XPATH, "//input[@placeholder='* Фамилия']"    # Поле ввода Фамилии на странице заказа
    User_Address = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"  # Поле ввода Адреса на странице заказа
    Metro_Stations = By.XPATH, "//input[@placeholder='* Станция метро']"    # Поле ввода станции метро на странице заказа
    User_Metro_Station = By.XPATH, "//li[@data-index='0']"    # Первая станция метро в выпадающем списке
    User_Phone_Number = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"  # Поле ввода номера телефона на странице заказа
    Next_Button = By.XPATH,  "//button[text()='Далее']"  # Кнопка "Далее" - переход со страницы ввода данных пользователя к вводу данных об аренде
    About_Rent_Header = By.XPATH, "//div[text()='Про аренду']"  # Заголовок "Про аренду" на странице ввода данных аренды
    Cookie_Button = By.ID, "rcc-confirm-button"     # Приниятие куки-файлов
    Rent_Date = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"    # Поле ввода даты аренды
    User_Rent_Date = By.XPATH, "//div[@aria-label ='Choose воскресенье, 6-е августа 2023 г.']"  # Дата 06.07.2023 в календаре
    Rental_Period = By.CLASS_NAME, "Dropdown-root"  # Поле ввода периода аренды
    User_Rental_Period = By.XPATH,  "//div[@class='Dropdown-option' and text()='двое суток']"   # Значение "двое суток" в выпадающем списке
    Scooter_Color = By.ID, "black"  # Чекбокс "чёрный жемчуг" в поле выбора цвета самоката
    User_Comment = By.XPATH, "//input[@placeholder='Комментарий для курьера']"  # Поле ввода комментария для курьера
    Order_Confirm_Button = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"   # Финальная кнопка "Заказть" на странице оформления заказа
    Confirm_Button = By.XPATH,  "//button[text()='Да']"    # Кнопка "Да" - подтверждение оформления заказа
    Confirm_Order_Header = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"    # Заголовок "Заказ оформлен" в окне с подтверждением оформления заказа

    def input_user_data(self, user_data):
        self.element_set_data(self.User_Name, user_data[0])
        self.element_set_data(self.User_Surname, user_data[1])
        self.element_set_data(self.User_Address, user_data[2])
        self.element_click(self.Metro_Stations)
        self.element_click(self.User_Metro_Station)
        self.element_set_data(self.User_Phone_Number, user_data[3])
        self.go_to_element(self.Next_Button)
        self.element_click(self.Next_Button)

    def check_user_input(self, header):
        self.element_wait_for_load(self.About_Rent_Header)
        actually_header = self.driver.find_element(*self.About_Rent_Header).text
        assert actually_header == header

    def input_rent_data(self, rent_data):
        self.element_click(self.Rent_Date)
        self.element_click(self.User_Rent_Date)
        self.element_click(self.Rental_Period)
        self.element_click(self.User_Rental_Period)
        self.element_click(self.Scooter_Color)
        self.element_set_data(self.User_Comment, rent_data)
        self.element_click(self.Order_Confirm_Button)
        self.element_click(self.Confirm_Button)

    def check_rent_input(self, header):
        self.element_wait_for_load(self.Confirm_Order_Header)
        actually_header = self.driver.find_element(*self.Confirm_Order_Header).text
        print(actually_header)
        assert header in actually_header







