import time
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators2:
    """Класс поиска локаторов."""
    # Кнопка создания нового поста
    LOCATOR_NEW_POST_CREATE_BUTTON = (By.XPATH, """//*[@id="create-btn"]""")
    # Заголовок нового поста
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    # Описание нового поста
    LOCATOR_NEW_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    # Контент нового поста
    LOCATOR_NEW_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    # Фото нового поста
    LOCATOR_NEW_POST_PHOTO = (By.XPATH, """//*[@id="create-item"]/div/div/div[6]/div/div/label/input""")
    # Кнопка сохранения нового поста
    LOCATOR_NEW_POST_SAVE_BUTTON = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    # Поле названия созданного поста
    LOCATOR_NEW_POST_CREATED_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")


class OperationsAddPost(BasePage):
    def click_create_post_button(self):
        logging.info('Click create new post button')
        self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_CREATE_BUTTON).click()

    def fill_fields(self, title=None, description=None, content=None, photo=None):
        time.sleep(1)

        if title is not None:
            logging.info(f'Sent {title} to element {TestSearchLocators2.LOCATOR_NEW_POST_TITLE[1]}')
            title_field = self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_TITLE)
            title_field.send_keys(title)

        if description is not None:
            logging.info(f'Sent {description} to element {TestSearchLocators2.LOCATOR_NEW_POST_DESCRIPTION[1]}')
            description_field = self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_DESCRIPTION)
            description_field.send_keys(description)

        if content is not None:
            logging.info(f'Sent {content} to element {TestSearchLocators2.LOCATOR_NEW_POST_CONTENT[1]}')
            content_field = self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_CONTENT)
            content_field.send_keys(content)

        if photo is not None:
            logging.info(f'Sent file {photo} to element {TestSearchLocators2.LOCATOR_NEW_POST_PHOTO[1]}')
            photo_field = self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_PHOTO)
            photo_field.send_keys(photo)

    def click_publish_post_button(self):
        logging.info('Click publish post button')
        self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_SAVE_BUTTON).click()

    def get_published_post_title(self):
        time.sleep(1)
        title_field = self.find_element(TestSearchLocators2.LOCATOR_NEW_POST_CREATED_TITLE, time=3)
        text = title_field.text
        logging.info(f'We find text {text} in field {TestSearchLocators2.LOCATOR_NEW_POST_CREATED_TITLE[1]}')
        return text
