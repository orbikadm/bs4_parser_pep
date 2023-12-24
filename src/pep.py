from bs4 import BeautifulSoup
import requests_cache
import re
from urllib.parse import urljoin
from tqdm import tqdm
from collections import Counter
import logging


PEP_DOC_URL = 'https://peps.python.org/'
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
count_statuses = Counter()


def get_pep_info(url):
    session = requests_cache.CachedSession()
    response = session.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    return soup.find('abbr').text


def pep():
    session = requests_cache.CachedSession()
    response = session.get(PEP_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    section_tag = soup.find('section', {'id': 'numerical-index'})
    tr_tags = section_tag.find_all('tr')
    for tr_tag in tqdm(tr_tags[1:], desc='Пошла жара'):
        abbr_tag = tr_tag.find('abbr')
        preview_status = abbr_tag.text[1:]
        href_attr = tr_tag.find('a', string=re.compile(r'\d{1,4}'))
        pep_url = urljoin(PEP_DOC_URL, href_attr['href'])
        pep_status = get_pep_info(pep_url)
        if pep_status not in EXPECTED_STATUS[preview_status]:
            logging.info(f"""
Несовпадающие статусы:
{pep_url} 
Статус в карточке: {pep_status} 
Ожидаемые статусы: {EXPECTED_STATUS[preview_status]}
""")

        count_statuses[pep_status] += 1

    results = [('Статус', 'Количество')]
    results.extend(count_statuses.items())
    all_pep = sum(count_statuses.values())
    results.append(('Total', all_pep))
    print('RESULT: ', results)


if __name__ == '__main__':
    pep()
