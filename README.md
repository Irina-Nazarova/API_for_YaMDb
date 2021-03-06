![Build Status](https://github.com/Irina-Nazarova/API_for_YaMDb/workflows/Yamdb-app%20workflow/badge.svg)

# API Yamdb

Yamdb — база отзывов о фильмах, книгах и музыке. Для этой базы был написан RESTfull API. Проект можно развернуть в трех Docker-контейнерах с помощью docker-compose.

![](img/VM_Yamdb.png)

### Как развернуть проект

1. Склонируйте репозиторий на свой компьютер
2. В файле .env задайте переменные окружения

```bash
DB_ENGINE=django.db.backends.postgresql    # указываем, что работаем с postgresql
DB_NAME=postgres                           # имя базы данных
POSTGRES_USER=postgres                     # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres                 # пароль для подключения к БД (установите свой)
DB_HOST=db                                 # название сервиса (контейнера)
DB_PORT=5432                               # порт для подключения к БД
```

3. Выполните запуск сборки и запуск контейнеров

```bash
docker-compose up
docker ps 


➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
dde33dc956f1        infra_sp2_web       "gunicorn api_yamdb.…"   6 minutes ago       Up 6 minutes        0.0.0.0:8000->8000/tcp   infra_sp2_web_1
9fc134d8e619        postgres:12.4       "docker-entrypoint.s…"   6 minutes ago       Up 6 minutes        5432/tcp                 infra_sp2_db_1
```


4. Подключитесь к контейнеру

```bash
docker exec -it infra_sp2_web_1 bash
```

5. Внутри контейнера выполните миграции

```bash
python manage.py migrate
```

6. Загрузите в базу тестовые данные

```bash
python manage.py loaddata fixtures.json
```

### Устранение неполадок 

В случае проблем с миграциями:

1. Зайдите в контейнер postgres

```bash
docker exec -it infra_sp2_web_1 bash

psql -U postgres

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
```

2. Подключитесь к БД: postgres

```bash
postgres=# \c postgres
```

Если существуют таблицы в БД

```bash
postgres=# \dt
                 List of relations
 Schema |          Name          | Type  |  Owner
--------+------------------------+-------+----------
 public | auth_group             | table | postgres
 public | auth_group_permissions | table | postgres
 public | auth_permission        | table | postgres
 public | category               | table | postgres
 public | comments               | table | postgres
 public | django_admin_log       | table | postgres
 public | django_content_type    | table | postgres
 public | django_migrations      | table | postgres
 public | django_session         | table | postgres
 public | genre                  | table | postgres
 public | genre_title            | table | postgres
 public | review                 | table | postgres
 public | titles                 | table | postgres
 public | users                  | table | postgres
 public | users_groups           | table | postgres
 public | users_user_permissions | table | postgres
(16 rows)

```

Можно их удалить (ВСЕ ДАННЫЕ БУДУТ ПОТЕРЯНЫ). Но если там только данные из fixtures.json - это не страшно

3. Удалите таблицы

```bash
postgres=# DROP TABLE auth_group, auth_group_permissions, auth_permission, category, comments, django_admin_log, django_content_type, django_migrations, django_migrations, django_session, genre, genre_title, review, titles, users, users_groups, users_user_permissions;
DROP TABLE

postgres=# \dt
Did not find an

```

Далее повторно выполните миграции и загрузку фикстур

### GitHub Actions/Workflow

Как работать с GitHub Actions/Workflow:

Workflow — это набор команд, которые выполнятся в виртуальном окружении после того, как произойдёт какое-то событие-триггер (например запушить код в репозиторий).
   
1. Зайдите в свой репозиторий на GitHub, перейдите во вкладку Actions, для 
   создания директории .github/workflows с шаблоном main.yml нажмите ссылку
   set up a workflow yourself.
   
   Нажмите зеленую кнопку Start commit, дайте имя коммиту и нажмите Commit new file.
   
   Чтобы запустить workflow — надо сделать pull в master, тогда сработает инструкция on — и jobs начнут выполняться.
   
2. Перейдите в настройки репозитория Settings-Secrets-New secret
   
3. Задайте имя переменным и нажмите Add secret:
   
    DOCKER_USERNAME
   
    DOCKER_PASSWORD
   
    USER - имя пользователя для подключения к серверу
   
    HOST - IP-адрес вашего сервера
    
    SSH_KEY - приватный ключ от своего сервера
   
    PASSPHRASE - пароль при создании ssh-ключа
   
    TELEGRAM_TO - ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot.
   
    TELEGRAM_TOKEN - токен вашего бота. Получить этот токен можно у бота @BotFather.

### Авторы

[Ирина Назарова](https://github.com/Irina-Nazarova)  - написала категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[Вадим Кокшаров](https://github.com/Vadim3x4)  - написал часть, касающуюся управления пользователями (Auth и Users): систему регистрации и аутентификации, права доступа, работу с токеном, систему подтверждения e-mail, поля.

[Елизавета Безякина](https://github.com/bezyakina)  - написаны отзывы (Review) и комментарии (Comments): описывала модели и view, настраивала эндпойнты, определяла права доступа для запросов. Рейтинги произведений.

