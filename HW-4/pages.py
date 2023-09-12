from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time
import yaml


class TestSearchLocators:
    """Класс поиска локаторов."""
    ids = dict()
    with open('./locators.yaml', encoding='utf-8') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    # МЕТОДЫ ВВОДА ТЕКСТА
    def enter_text_into_field(self, locator, word, description=None):
        """Вспомогательный метод для ввода текста."""
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password form')

    def fill_post_fields(self, title=None, description=None, content=None, photo=None):
        time.sleep(1)
        if title:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NEW_POST_TITLE'], title,
                                       description='title create post')
        if description:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NEW_POST_DESCRIPTION'], description,
                                       description='description create post')
        if content:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NEW_POST_CONTENT'], content,
                                       description='content create post')
        if photo:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NEW_POST_PHOTO'], photo,
                                       description='photo create post')

    def fill_contact_fields(self, name=None, email=None, content=None):
        time.sleep(1)
        if name:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME'], name,
                                       description='name contact field')
        if email:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL'], email,
                                       description='email contact field')
        if content:
            self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT'], content,
                                       description='content contact field')

    # МЕТОДЫ НАЖАТИЯ НА КНОПКИ
    def click_button(self, locator, description=None):
        """Вспомогательный метод для клика."""
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_CREATE_BUTTON'], description='create post')

    def click_publish_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_SAVE_BUTTON'], description='publish new post')

    def click_contact(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='contact us')

    def click_send_contact_us_button(self):
        time.sleep(1)
        self.click_button(TestSearchLocators.ids['LOCATOR_BUTTON_CONTACT_US'], description='contact us send')

    # МЕТОДЫ ПОЛУЧЕНИЯ ТЕКСТА
    def get_text_from_element(self, locator, description=None):
        """Вспомогательный метод для получения текста."""
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error text')

    def get_success_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_GREETINGS'], description='greetings')

    def get_published_post_title(self):
        time.sleep(1)
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_NEW_POST_CREATED_TITLE'],
                                          description='published title')

    def get_alert(self):
        """Получение текста из alert."""
        logging.info('Get alert text')
        text = self.get_alert_text()
        logging.info(text)
        return text
