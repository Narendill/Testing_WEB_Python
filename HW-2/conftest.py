import pytest
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def sel_1():
    """Фикстура на логин."""
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def sel_2():
    """Фикстура на пароль."""
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def sel_3():
    """Фикстура на кнопку."""
    return 'button'


@pytest.fixture()
def sel_4():
    """Фикстура на сообщение об ошибке."""
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def result():
    """Фикстура на ожидаемый результат."""
    return '401'


@pytest.fixture()
def greetings():
    """Фикстура на поиск приветствия при авторизации."""
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def find_greetings():
    """Фикстура на приветствие."""
    return f'Hello, {testdata["login"]}'


# Фикстуры на новый пост
@pytest.fixture()
def new_post_btn():
    """Фикстура на кнопку создания нового поста."""
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def get_title():
    """Фикстура на заголовок нового поста."""
    return """//*[@id="create-item"]/div/div/div[1]/div/label"""


@pytest.fixture()
def get_description():
    """Фикстура на описание нового поста."""
    return """//*[@id="create-item"]/div/div/div[2]/div/label"""


@pytest.fixture()
def get_content():
    """Фикстура на контент нового поста."""
    return """//*[@id="create-item"]/div/div/div[3]/div/label"""


@pytest.fixture()
def get_photo():
    """Фикстура на фотографию нового поста."""
    return """//*[@id="create-item"]/div/div/div[6]/div/div/label/input"""


@pytest.fixture()
def get_post():
    """Фикстура на сохранение поста."""
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def find_title():
    """Фикстура на поиск названия созданного поста."""
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def created_title():
    """Фикстура на заголовок созданного поста."""
    return testdata['post_title']