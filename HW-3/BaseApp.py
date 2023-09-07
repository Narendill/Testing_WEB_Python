from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс страницы."""

    def __init__(self, driver):
        """Инициализация."""
        self.driver = driver

    def find_element(self, locator: tuple, time: int = 10):
        """Метод поиска элемента."""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Can not find element by locator {locator}')

    def get_element_property(self, locator: tuple, property: str):
        """Метод получения свойств элемента."""
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self, url='https://test-stand.gb.ru'):
        """Метод открытия страницы."""
        return self.driver.get(url)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text
