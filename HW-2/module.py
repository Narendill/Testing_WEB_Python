import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class Site:
    def __init__(self, address):
        """Метод инициализации класса."""
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(testdata['implicitly_wait'])
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode: str, path: str):
        """Метод поиска элемента."""
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None

        return element

    def get_element_property(self, mode: str, path: str, property: str):
        """Метод получения свойств элемента."""
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        """Метод закрытия соединения."""
        self.driver.close()
