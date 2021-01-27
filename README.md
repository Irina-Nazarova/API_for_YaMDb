# API Yamdb
![workflow yamdb](https://github.com/Irina-Nazarova/infra_sp2/raw/master/image/image.png)

Yamdb — база отзывов о фильмах, книгах и музыке. Для этой базы был написан RESTfull API. Проект можно развернуть в трех Docker-контейнерах с помощью docker-compose.

### Как развернуть проект

1. Склонируйте репозиторий на свой компьютер.
2. В файле .env задайте переменные окружения.
3. В терминале выполните команду для применения миграций

```
docker-compose run --rm web python manage.py migrate
```

4. Выполните запуск сборки и запуск контейнеров

```
docker-compose up
```

5. В новом терминале зайдите в контейнер и создайте суперпользователя 

```
docker exec -it <CONTAINER ID> bash
```
```
python manage.py createsuperuser
```

6. Загрузите в базу тестовые данные

```
python manage.py loaddata fixtures.json
```
