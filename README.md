# 👨‍💻 [Проект парсинга bs4_parser_pep.](https://github.com/KomkovAleksey/bs4_parser_pep)


## Оглавление

- [Автор](#Автор)
- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Запуск проекта](#запуск-проекта)
- [Примеры команд](#Gримеры-команд)



## Технологии:

- Python 3.9.10
- BeautifulSoup4
- PrettyTable
- Logging

## Описание проекта:

Проект парсинга документации [python](https://docs.python.org/3/) и [PEP](https://peps.python.org/).

В проекте реализованы 4 парсера:
- whats-new - Парсер статей о нововедениях в Python.
- latest_versions - Парсер статуса версии Python.
- download - Парсер скачивающий документацию Python.
- pep - Парсер документации [PEP](https://peps.python.org/).

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/KomkovAleksey/bs4_parser_pep) и перейдите в него в командной строке:
```
git clone https://github.com/danlaryushin/bs4_parser_pep.git

cd bs4_parser_pep
```
Создайте виртуальное окружение и активируйте его:
```
python -m venv vevn

source venv/Scripts/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Проект готов к работе!

## Примеры команд
Команды нужно вводить в терминале находясь в директории bs4_parser_pep/src

Вывод справки:
```
python main.py pep -h
```
Список ссылок на описание обновлений Python
```
python main.py whats-new
```
Cкачивание архива с документацией актуальной версии Python
```
python main.py download
```
Cписок ссылок на актуальные версии Python
```
python main.py latest-versions
```
Информация по статусам и количеству PEP
```
python main.py pep
```
Создает в папке results csv файл с таблицей из двух колонок «Статус» и «Количество»:

```
python main.py pep -o file
```


## Автор

[Алексей Комков](https://github.com/KomkovAleksey)
