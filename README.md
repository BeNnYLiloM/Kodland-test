# Kodland-test

*Пердполагается что у вас уже установлен Python 3 последней версии*

Запуск проекта:
1. Установить *Django*
2. Установить *PostgreSQL*
3. Создать таблицу (имя по умолчанию *kodland*)
4. Сделать миграцию в БД командой
```
python manager.py makemigrations
```
и
```
python manager.py migrate
```

И запустить сервер командой
```
python manager.py runserver
```

P.S. Адрес для создания статьи */add-article*