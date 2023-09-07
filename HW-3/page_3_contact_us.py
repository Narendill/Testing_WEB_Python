import time
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators3:
    """Класс поиска локаторов."""
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_BUTTON_CONTACT_US = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsContactUs(BasePage):
    def click_contact(self):
        logging.info('Click Contact')
        self.find_element(TestSearchLocators3.LOCATOR_CONTACT).click()

    def fill_fields(self, name=None, email=None, content=None):
        time.sleep(1)

        if name is not None:
            logging.info(f'Sent {name} to element {TestSearchLocators3.LOCATOR_NAME[1]}')
            name_field = self.find_element(TestSearchLocators3.LOCATOR_NAME)
            name_field.send_keys(name)

        if email is not None:
            logging.info(f'Sent {email} to element {TestSearchLocators3.LOCATOR_EMAIL[1]}')
            description_field = self.find_element(TestSearchLocators3.LOCATOR_EMAIL)
            description_field.send_keys(email)

        if content is not None:
            logging.info(f'Sent {content} to element {TestSearchLocators3.LOCATOR_CONTENT[1]}')
            content_field = self.find_element(TestSearchLocators3.LOCATOR_CONTENT)
            content_field.send_keys(content)

    def click_send_contact_us_button(self):
        time.sleep(1)
        logging.info('Click contact us button')
        self.find_element(TestSearchLocators3.LOCATOR_BUTTON_CONTACT_US).click()

        time.sleep(1)
        alert_text = self.get_alert_text()
        logging.info(f'We find text {alert_text} in alert')
        return alert_text
