# Задание
# Условие: Добавить в проект тест по проверке механики работы формы Contact Us
# на главной странице личного кабинета. Должно проверятся открытие формы, ввод данных в поля,
# клик по кнопке и появление всплывающего alert.
#
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
#
# Формат сдачи: В качестве решения принимается написанный нами ранее проект с добавлением шага
# по проверке Contact Us и правками всех необходимых вспомогательных файлов.
#
# Что ещё можно почитать:
# • Легкое веб-тестирование с Python, Pytest и Selenium WebDriver, часть 5:
# создание теста Page Object Selenium при помощи Python

from page_1_auth import OperationsHelper
from page_2_create_post import OperationsAddPost
from page_3_contact_us import OperationsContactUs
import logging
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    

def test_step_1(browser):
    """Тест на вход с неверными кредами."""
    logging.info('Test 1 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['incorrect_password'])
    test_page.click_login_button()
    assert test_page.get_error_text() == '401', 'test_step_1 FAILED'


def test_step_2(browser):
    """Тест на вход с валидными кредами."""
    logging.info('Test 2 starting')
    test_page = OperationsHelper(browser)
    test_page.enter_login(testdata['login'])
    test_page.enter_pass(testdata['password'])
    test_page.click_login_button()
    assert test_page.get_success_login_text() == f'Hello, {testdata["login"]}', 'test_step_2 FAILED'


def test_step_3(browser):
    """Тест на добавление поста со всеми введенными полями."""
    logging.info('Test 2 starting')
    test_page = OperationsAddPost(browser)
    test_page.click_create_post_button()
    test_page.fill_fields(testdata['post_title'], testdata['post_description'], testdata['post_content'],
                          testdata['post_photo'])
    test_page.click_publish_post_button()
    assert test_page.get_published_post_title() == testdata['post_title'], 'test_step_3 FAILED'


def test_step_4(browser):
    """Тест на добавление поста без фото."""
    logging.info('Test 2 starting')
    test_page = OperationsAddPost(browser)
    test_page.go_to_site()
    test_page.click_create_post_button()
    test_page.fill_fields(testdata['post_title'], testdata['post_description'], testdata['post_content'])
    test_page.click_publish_post_button()
    assert test_page.get_published_post_title() == testdata['post_title'], 'test_step_4 FAILED'


def test_step_5(browser):
    """Тест на добавление поста без title."""
    logging.info('Test 2 starting')
    test_page = OperationsAddPost(browser)
    test_page.go_to_site()
    test_page.click_create_post_button()
    test_page.fill_fields(description=testdata['post_description'], content=testdata['post_content'],
                          photo=testdata['post_photo'])
    test_page.click_publish_post_button()
    assert test_page.get_published_post_title() == '', 'test_step_5 FAILED'


def test_step_6(browser):
    """Тест на добавление поста без description."""
    logging.info('Test 2 starting')
    test_page = OperationsAddPost(browser)
    test_page.go_to_site()
    test_page.click_create_post_button()
    test_page.fill_fields(title=testdata['post_title'], content=testdata['post_content'],
                          photo=testdata['post_photo'])
    test_page.click_publish_post_button()
    assert test_page.get_published_post_title() == testdata['post_title'], 'test_step_6 FAILED'


def test_step_7(browser):
    """Тест на добавление поста без content."""
    logging.info('Test 2 starting')
    test_page = OperationsAddPost(browser)
    test_page.go_to_site()
    test_page.click_create_post_button()
    test_page.fill_fields(title=testdata['post_title'], description=testdata['post_description'],
                          photo=testdata['post_photo'])
    test_page.click_publish_post_button()
    assert test_page.get_published_post_title() == testdata['post_title'], 'test_step_7 FAILED'


def test_step_8(browser):
    """Тест на форму обратной связи."""
    logging.info('Test 8 starting')
    test_page = OperationsContactUs(browser)
    test_page.click_contact()
    test_page.fill_fields('Ilya', '123@us.com', 'Мама мыла раму.')
    assert test_page.click_send_contact_us_button() == 'Form successfully submitted', 'test_step_8 FAILED'
