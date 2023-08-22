# Написать тест с использованием pytest и requests, в котором:
# ● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# ● conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей параметров
# “username" и "password" и возвращающей токен авторизации
# ● Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого
# пользователя, для этого выполняется get запрос по адресу
# https://test-stand.gb.ru/api/posts c хедером, содержащим токен
# авторизации в параметре "X-Auth-Token". Для отображения
# постов другого пользователя передается "owner": "notMe".
# ______________________________________________________________________________________
# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
#
# Подсказка: создание поста выполняется запросом к
# https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.


import requests
import yaml

with open('config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_find_title_in_posts(get_token, find_title):
    """Тест по поиску заголовка."""
    res = requests.get(url=data['url_posts'],
                       params={'owner': 'notMe'},
                       headers={'X-Auth-Token': get_token}).json()

    find = False
    for topic in res['data']:
        if topic['title'] == find_title:
            find = True
            break
    assert find, 'test_header_post FAILED'


def test_creation_new_post(get_token):
    """Тест на создание нового поста."""
    params = {'title': 'NEW POST', 'description': 'Me new post here...', 'content': 'testing API'}
    create_new_post = str(requests.post(url=data['url_posts'],
                                        params=params,
                                        headers={'X-Auth-Token': get_token}))
    get_my_posts = requests.get(url=data['url_posts'], headers={'X-Auth-Token': get_token}).json()

    assert create_new_post == '<Response [200]>' and get_my_posts['data'][0]['description'] == params['description'], \
        'test_creation_new_post FAILED '
