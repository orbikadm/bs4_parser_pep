import logging

from requests import RequestException
from bs4 import BeautifulSoup

from constants import TAG_STATUS_ON_PEP_PAGE
from exceptions import ParserFindTagException


def get_response(session, url):
    """
    Функция отправляет запрос по url и возвращает ответ.
    Принимает параметры:
    session - сессия (кешируемая либо некешируемая)
    url - адрес, на который нужно отправить запрос.
    Расширена обработкой исключения RequestException.
    """
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )


def find_tag(soup, tag, attrs=None):
    """
    Функция ищет тег в экземпляре объект Beautifullsoup и возвращает его.
    Принимает параметры:
    soup - экземпляр объекта Beautifullsoup
    tag - искомый тег
    attrs - словарь аттрибутов и их значений, которые должен включать тег.
    Расширена обработкой исключения ParserFindTagException.
    """
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def get_pep_info(session, url):
    """
    Функция делает запрос по урл, ищет тег со статусом PEP на странице и
    возвращает статус PEP в текстовом формате.
    Принимает параметры:
    session - сессия (кешируемая либо некешируемая)
    url - адрес страницы PEP.
    """
    response = get_response(session, url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    return find_tag(soup, TAG_STATUS_ON_PEP_PAGE).text
