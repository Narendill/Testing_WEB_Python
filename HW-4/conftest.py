import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    current_browser = testdata['browser']


@pytest.fixture(scope='session')
def browser():
    """Фикстура инициализации браузера."""
    if current_browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def title_to_find():
    """Фикстура возвращает текст искомого заголовка."""
    return 'пост с картинкой больше 2 мб'
