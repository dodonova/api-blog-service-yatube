### Проект API Yatube

**For documentation in English, please refer to [README_EN.md](./README_EN.md).**


Yatube — это платформа для блогов. В проекте реализованы возможности: регистрация, создание, редактирования или удалить постов, комментирования постов другого автора и подписки на него.

После запуска проекта, по адресу  http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube.

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dodonova/api-blog-service-yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры

Пример POST-запроса с токеном пользователя user: добавление нового поста.

*POST .../api/v1/posts/*

```
{
    "text": "Текст поста.",
    "group": 1
}
```

Пример ответа:

```
{
    "id": 14,
    "text": "Текст поста.",
    "author": "user",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

Пример POST-запроса для добавления нового комментария к посту с `id=14`.

*POST .../api/v1/posts/14/comments/*

```
{
    "text": "тест тест"
}
```

Пример ответа:

```
{
    "id": 4,
    "author": "user",
    "post": 14,
    "text": "тест тест",
    "created": "2021-06-01T10:14:51.388932Z"
}
```

Пример GET-запроса на получение информации о группе.

GET *.../api/v1/groups/2/*

Пример ответа:

`{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}`
