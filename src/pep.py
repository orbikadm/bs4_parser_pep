from bs4 import BeautifulSoup
import requests_cache
import re
from urllib.parse import urljoin
from time import sleep
from tqdm import tqdm


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

def get_pep_info(url):
    # url = 'https://peps.python.org/pep-0249/' # Final
    # url = 'https://peps.python.org/pep-0430/' # Final
    # url = 'https://peps.python.org/pep-0708/' # Provisional
    # url = 'https://peps.python.org/pep-0458/' # Accepted
    session = requests_cache.CachedSession()
    response = session.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    status = soup.find('abbr').text
    print(status)


# def validate_tr():


def pep():
    session = requests_cache.CachedSession()
    response = session.get(PEP_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')







### РАБОЧИЙ ВАРИАНТ
    # tr_tags = soup.find_all('tr')
    # for tr_tag in tr_tags:
    #     abbr_tag = tr_tag.find('abbr')
    #     if abbr_tag:
    #         pep_status_in_list = abbr_tag.text
    #     else:
    #         continue
    #     href_attr = tr_tag.find('a', string=re.compile(r'\d{1,4}'))
    #     if href_attr:
    #         pep_url = urljoin(PEP_DOC_URL, href_attr['href'])
    #     else:
    #         continue
    #
    #     print(pep_status_in_list, pep_url)
### РАБОЧИЙ ВАРИАНТ

        # for url in pep_urls:
        #     page_url = urljoin(PEP_DOc_URL, url['href'])
        #     print(page_url)
        #     sleep(1)
        #     get_pep_info(page_url)


if __name__ == '__main__':
    pep()
    # url = 'https://peps.python.org/pep-8105/'
    #
    # get_pep_info(url)
