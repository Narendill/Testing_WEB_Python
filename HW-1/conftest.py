import pytest
import requests
import yaml


with open('config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def get_token() -> str:
    """Возвращает токен с сайта, полученный по логину и паролю."""
    result = requests.post(url=data['url_auth'],
                           data={'username': data['username'], 'password': data['password']}).json()['token']
    return result


@pytest.fixture()
def find_title():
    """Возвращает заголовок, который хотим найти."""
    return 'python'


