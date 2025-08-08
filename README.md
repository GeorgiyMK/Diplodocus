Backend-приложение, реализованное на Django и Django REST Framework, для публикации постов с изображениями, комментариев и лайков.
Поддерживается регистрация, авторизация по токену и работа с API.


Регистрация и авторизация пользователей по токену.

Создание, редактирование и удаление публикаций с изображениями.

Добавление комментариев к постам.

Лайки и их подсчёт.

Просмотр списка постов и комментариев через API.

Панель администратора Django для управления контентом.

API эндпоинты
Метод	URL	Описание
GET	/api/posts/	Получить список постов
POST	/api/posts/	Создать новый пост
POST	/api/posts/{id}/like/	Лайк/анлайк поста
GET	/api/posts/{id}/comments/	Получить комментарии к посту
POST	/api/comments/	Добавить комментарий
GET	/api/likes/	Список лайков
POST	/api/token/	Получить токен авторизации

Авторизация через токен
Получите токен:
POST /api/token/
{
  "username": "ваш_логин",
  "password": "ваш_пароль"
}

PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diplom',
        'USER': 'postgres',
        'PASSWORD': 'NewPassword123!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

