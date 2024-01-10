# 👨‍💻 [Проект парсинга документации python и pep.](https://github.com/KomkovAleksey/bs4_parser_pep)


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

Проект парсинга документации [python](https://docs.python.org/3/) и [pep](https://peps.python.org/).

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
Парсер готов к работе!

## Примеры команд
Команды нужно вводить находясь в директории bs4_parser_pep/src

Вывод справки:
```
python main.py pep -h
```
Создает в папке results csv файл с таблицей из двух колонок «Статус» и «Количество»:
```
python main.py pep -o file
```
Выводит таблицу prettytable с тремя колонками: "Ссылка на документацию", "Версия", "Статус":
```
python main.py latest-versions -o pretty 
```

## Автор

[Алексей Комков](https://github.com/KomkovAleksey)
