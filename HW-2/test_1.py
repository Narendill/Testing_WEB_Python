# Добавить в тестовый проект шаг добавления
# поста после входа. Должна выполняться
# проверка на наличие названия поста на странице
# сразу после его создания.
# Совет:
# Не забудьте добавить небольшие ожидания
# перед и после нажатия кнопки создания поста.
import time
import yaml
from module import Site


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])


def test_step_1(sel_1, sel_2, sel_3, sel_4, result):
    """Тест на авторизацию пользователя с неверными кредами."""
    # Имя пользователя
    input1 = site.find_element('xpath', sel_1)
    input1.clear()
    input1.send_keys(testdata['login'])

    # Пароль
    input2 = site.find_element('xpath', sel_2)
    input2.clear()
    input2.send_keys(testdata['incorrect_password'])

    # Кнопка
    btn = site.find_element('css', sel_3)
    btn.click()

    # Переход на страницу профиля и поиск текста
    err_label = site.find_element('xpath', sel_4)
    res = err_label.text

    assert res == result, 'test_step_1 FAILED'


def test_step_2(sel_1, sel_2, sel_3, sel_4, greetings, find_greetings):
    """Тест на авторизацию пользователя с валидными кредами."""
    # Имя пользователя
    input1 = site.find_element('xpath', sel_1)
    input1.clear()
    input1.send_keys(testdata['login'])

    # Пароль
    input2 = site.find_element('xpath', sel_2)
    input2.clear()
    input2.send_keys(testdata['password'])

    # Кнопка
    btn = site.find_element('css', sel_3)
    btn.click()

    # Приветствие при авторизации
    greetings = site.find_element('xpath', greetings)
    res = greetings.text

    assert res == find_greetings, 'test_step_2 FAILED'


def test_step_3(new_post_btn, get_title, get_description, get_content, get_post, find_title, created_title, get_photo):
    """Тест на добавление поста."""

    # Сделал задержку везде, а то форма почему-то заполняется полностью не всегда, словно проскакивает поля иногда.

    # Кнопка создания нового поста
    time.sleep(testdata['sleep_time'])
    post_btn = site.find_element('xpath', new_post_btn)
    post_btn.click()

    # Заполнение заголовка
    time.sleep(testdata['sleep_time'])
    title = site.find_element('xpath', get_title)
    title.send_keys(testdata['post_title'])

    # Заполнение описания поста
    time.sleep(testdata['sleep_time'])
    description = site.find_element('xpath', get_description)
    description.send_keys(testdata['post_description'])

    # Заполнение содержания поста
    time.sleep(testdata['sleep_time'])
    content = site.find_element('xpath', get_content)
    content.send_keys(testdata['post_content'])

    # Загрузка фото
    time.sleep(testdata['sleep_time'])
    photo = site.find_element('xpath', get_photo)
    photo.send_keys(testdata['post_photo'])

    # Публикация поста
    save_post = site.find_element('xpath', get_post)
    save_post.click()

    time.sleep(testdata['sleep_time'])

    result = site.find_element('xpath', find_title)
    result_title = result.text

    site.close()

    assert result_title == created_title, 'test_step_3 FAILED'
