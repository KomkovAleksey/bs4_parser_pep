import re
import logging
from urllib.parse import urljoin
from collections import Counter

import requests_cache
from tqdm import tqdm

from exceptions import ParserFindTagException
from constants import (
    MAIN_DOC_URL,
    PEP_DOC_URL,
    EXPECTED_STATUS,
    PATTERN,
    BASE_DIR,
)
from configs import configure_argument_parser, configure_logging
from outputs import control_output
from utils import get_response, find_tag, get_soup


def whats_new(session):
    """Парсер статей о нововедениях в Python."""
    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    soup = get_soup(session, whats_new_url)
    main_div = find_tag(soup, 'section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = find_tag(main_div, 'div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all(
        'li', attrs={'class': 'toctree-l1'}
    )
    for section in tqdm(sections_by_python):
        version_a_tag = find_tag(section, 'a')
        href = version_a_tag['href']
        version_link = urljoin(whats_new_url, href)
        soup = get_soup(session, version_link)
        h1 = find_tag(soup, 'h1')
        dl = find_tag(soup, 'dl')
        dl_text = dl.text.replace('\n', ' ')
        results.append((version_link, h1.text, dl_text))

    return results


def latest_versions(session):
    """Парсер статуса версии Python."""
    soup = get_soup(session, MAIN_DOC_URL)
    sidebar = find_tag(soup, 'div', {'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
        else:
            raise ParserFindTagException('Не найден список c версиями Python')
    results = [('Ссылка на документацию', 'Версия', 'Статус')]
    for a_tag in a_tags:
        link = a_tag['href']
        text_match = re.search(PATTERN, a_tag.text)
        if text_match is not None:
            version, status = text_match.groups()
        else:
            version, status = a_tag.text, ''
        results.append((link, version, status))

    return results


def download(session):
    """Парсер скачивающий документацию Python."""
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    soup = get_soup(session, downloads_url)
    main_tag = find_tag(soup, 'div', {'role': 'main'})
    table_tag = find_tag(main_tag, 'table', {'class': 'docutils'})
    pdf_a4_tag = find_tag(
        table_tag, 'a', {'href': re.compile(r'.+pdf-a4\.zip$')}
    )
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(MAIN_DOC_URL, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    response = get_response(session, archive_url)
    if response is None:
        return
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    logging.info(f'Архив был загружен и сохранён: {archive_path}')


def pep(session):
    """Парсер документации PEP."""
    results = [('Статус', 'Количество')]
    actual_statuses = Counter()
    soup = get_soup(session, PEP_DOC_URL)
    section_tag = find_tag(soup, 'section', attrs={'id': 'numerical-index'})
    tbody_tag = find_tag(section_tag, 'tbody')
    tr_tag = tbody_tag.find_all('tr')
    for tr in tqdm(tr_tag):
        pep_status_in_table = find_tag(tr, 'abbr').text[1:]
        if pep_status_in_table is None:
            return
        pep_link = find_tag(tr, 'a')['href']
        pep_page = urljoin(PEP_DOC_URL, pep_link)
        soup = get_soup(session, pep_page)
        dl_tag = find_tag(soup, 'dl')
        pep_status_in_pep_page = dl_tag.find(
            string='Status'
        ).parent.find_next_sibling('dd').string
        if pep_status_in_pep_page is None:
            return
        actual_statuses[pep_status_in_pep_page] += 1
        if pep_status_in_pep_page not in EXPECTED_STATUS[pep_status_in_table]:
            error_msg = (
                'Несовпадающие статусы:\n'
                f'{pep_page}\n'
                f'Статус в карточке {pep_status_in_pep_page}\n'
                f'Ожидаемые статусы: {EXPECTED_STATUS[pep_status_in_table]}'
            )
            logging.warning(error_msg)

    for status, quantity in actual_statuses.items():
        results.append((status, quantity))
    results.append(('Total', sum(actual_statuses.values())))

    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep,
}


def main():
    """Главная фукция."""
    configure_logging()
    logging.info('Парсер запущен!')
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')
    try:
        session = requests_cache.CachedSession()
        if args.clear_cache:
            session.cache.clear()
        results = MODE_TO_FUNCTION[args.mode](session)
        if results is not None:
            control_output(results, args)
    except Exception as error:
        logging.exception(
            'Во время выполнения скрипта возникла ошибка {error}'.format(error=error)
        )
    logging.info('Парсер завершил работу.')
 
 
if __name__ == '__main__':
    main()
