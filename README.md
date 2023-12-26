[![Practicum.Yandex](https://img.shields.io/badge/-Practicum.Yandex-464646?style=flat&logo=Practicum.Yandex&logoColor=56C0C0&color=008080)](https://practicum.yandex.ru/)

# Python Docs and PEP Parser

## Описание:

Python Docs and PEP Parser - парсер информации о python с сайта https://docs.python.org/3/ и информации о соглашениях PEP с сайта https://peps.python.org/.

В проекте реализован парсинг аргументов командной строки, который позволяет переключаться между разными режимами парсинга и вывода информации.

## Используемые ехнологии и библиотеки:
- [Python](https://www.python.org/);
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/);
- [argparse](https://docs.python.org/3/library/argparse.html);
- [prettytable](https://pypi.org/project/prettytable/);
- [tqdm](https://pypi.org/project/tqdm/);
- [requests_cache](https://pypi.org/project/requests-cache/).

## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке

- Создать виртуальное окружение и установить зависимости

- Перейти в директорию src

## Работа с парсером:
Получить справку с возможностями парсера:

```
python main.py -h
```

Получить список ссылок на перечень изменений в версиях Python:

```
python main.py whats-new
```

Получить список ссылок на документацию всех версий Python:

```
python main.py latest-versions
```

Скачать архив документации для последней версии Python:

```
python main.py download
```

Посчитать статусы всех соглашений PEP и вывести их в общем списке:

```
python main.py pep
```

## Кеширование:
По умолчанию парсер кеширует страницы.
Запустить парсер с предварительной очисткой кеша можно с помощью аргумента:

```
-c, --clear-cache
```

## Дополнительные опции вывода данных:
- **--output pretty**: выводит данные в терминале в виде таблицы.
- **--output file**: сохраняет данные в папке results в csv формате с указанием даты.

## Примеры использования:

```
python main.py [вариант парсера] [очистка кеша] [вариант вывода]
```

Парсинг информации о PEP с очисткой кеша и сохранением результата в файл CSV:

```
python main.py pep -c -o file
```

## Над проектом [Python Docs and PEP Parser](https://github.com/orbikadm/bs4_parser_pep) работал:

[Константин Упоров](https://github.com/orbikadm)