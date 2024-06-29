# Инструкция по запуску проекта

1. Нужно установить docker. Для этого необходимо перейти на сайт https://www.docker.com/products/docker-desktop/ и
   скачать версию под вашу систему
2. Открыть проект
3. Запустить билд образов `docker-compose build`
4. Запустить проект `docker-compose up`
5. Чтобы перейти в admin панель нужно создать аккаунт. Для этого нужно открыть терминал в новой вкладке и запустить
   данную команду `docker-compose exec web python manage.py createsuperuser`
6. Have fun :)