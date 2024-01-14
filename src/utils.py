import logging

from requests import RequestException
from bs4 import BeautifulSoup

from exceptions import ParserFindTagException, NotResponseException


def get_response(session, url, encoding='utf-8'):
    """Перехват ошибки RequestException."""
    error_msg = f'Возникла ошибка при загрузке страницы {url}'
    try:
        response = session.get(url)
        response.encoding = encoding
        return response
    except RequestException:
        raise NotResponseException(error_msg)


def find_tag(soup, tag, attrs=None):
    """Перехват ошибки поиска тегов."""
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    error_msg = f'Не найден тег {tag} {attrs}'
    if searched_tag is None:
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)

    return searched_tag


def get_soup(session, url, encoding='utf-8'):
    """Beautiful Soup"""
    response = get_response(session, url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, features='lxml')

    return soup
