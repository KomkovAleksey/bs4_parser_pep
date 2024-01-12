import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import DATETIME_FORMAT, PRETTY, FILE, BASE_DIR


def control_output(results, cli_args):
    """Контроль вывода результатов парсинга."""
    outputs = {
        PRETTY: pretty_output,
        FILE: file_output,
    }

    output = cli_args.output
    if output in outputs:
        try:
            return outputs[output](results, cli_args)
        except TypeError:
            return outputs[output](results)
    else:
        return default_output(results)


def default_output(results):
    """Вывод данных в терминал построчно."""
    for row in results:
        print(*row)


def pretty_output(results):
    """Вывод данных в формате PrettyTable."""
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)


def file_output(results, cli_args, encoding='utf-8'):
    """
    Создание директории с результатами парсинга.
    Сохраненяет файл с результатами в формате .csv
    """
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding=encoding) as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')
