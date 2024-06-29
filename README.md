# Инструкция по запуску проекта

1. Нужно установить docker. Для этого необходимо перейти на сайт https://www.docker.com/products/docker-desktop/ и
   скачать версию под вашу систему
2. Открыть проект
3. Скопировать файлы `.env.example` и `.env.db.example` в `.env` и `.env.db` и заполнить
4. Запустить билд образов `docker-compose build`
5. Запустить проект `docker-compose up`
6. Чтобы перейти в admin панель нужно создать аккаунт. Для этого нужно открыть терминал в новой вкладке и запустить
   данную команду `docker-compose exec web python manage.py createsuperuser`
7. Have fun :)