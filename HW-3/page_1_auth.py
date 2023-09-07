import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators:
    """Класс поиска локаторов."""
    # Имя пользователя
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    # Пароль
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # Кнопка
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    # Сообщение об ошибке
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    # Приветствие при успешном входе
    LOCATOR_GREETINGS = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Sent {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Sent {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_success_login_text(self):
        success_login_text = self.find_element(TestSearchLocators.LOCATOR_GREETINGS, time=3)
        text = success_login_text.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_GREETINGS[1]}')
        return text