import requests
import logging


class BasesApi:
    """Базовый класс на подключение по API."""

    def __init__(self, username, password):
        """Инициализация класса."""
        self.url_login = 'https://test-stand.gb.ru/gateway/login'
        self.url_users_post = 'https://test-stand.gb.ru/api/posts'
        self.username = username
        self.password = password
        logging.info('Trying to get token')
        try:
            self.token = requests.post(url=self.url_login, data={'username': self.username,
                                                                 'password': self.password}).json()['token']
        except:
            logging.exception('Exception in GET request while receiving token')
            self.token = None


class OperationsApi(BasesApi):
    """Класс с операциями для API."""

    def get_users_posts(self) -> dict | None:
        """Получение постов чужих пользователей."""
        logging.info('Trying to get user\'s posts')
        try:
            users_post = requests.get(url=self.url_users_post,
                                      params={'owner': 'notMe'},
                                      headers={'X-Auth-Token': self.token}).json()
        except:
            logging.exception('Exception in GET request while receiving user\'s posts')
            users_post = None
        return users_post

    def get_my_posts(self) -> dict | None:
        """Получение постов самого пользователя."""
        logging.info('Trying to get my posts')
        try:
            my_posts = requests.get(url=self.url_users_post, headers={'X-Auth-Token': self.token}).json()
        except:
            logging.exception('Exception in GET request while receiving my posts')
            my_posts = None
        return my_posts

    def find_my_post_by_description(self, description: str) -> bool:
        """Поиск поста пользователя по описанию."""
        logging.info('Trying to find my post')
        try:
            my_posts = self.get_my_posts()
            for topic in my_posts['data']:
                if topic['description'] == description:
                    return True
        except:
            logging.exception('Exception in GET request while getting my posts')
        return False

    def create_new_post(self, title: str, description: str, content: str) -> bool:
        """Создание нового поста."""
        params = {'title': title, 'description': description, 'content': content}
        logging.info('Creating new post')
        try:
            create_new_post = str(requests.post(url=self.url_users_post,
                                                params=params,
                                                headers={'X-Auth-Token': self.token}))
        except:
            logging.exception('Exception while creating new post')
            create_new_post = None
        if create_new_post == '<Response [200]>':
            return True
        else:
            return False

    def find_title(self, title: str) -> bool:
        """Поиск заголовка статьи в постах чужих пользователей."""
        logging.info(f'Trying finding title {title}')
        try:
            users_posts = self.get_users_posts()
            for topic in users_posts['data']:
                if topic['title'] == title:
                    return True
        except:
            logging.exception('Exception while finding title')
        return False
