import requests
import textwrap
from bs4 import BeautifulSoup as BS


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.45 Safari/537.36',
    'accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    text_elements = [t.get_text() for t in soup.find_all('p')]
    text = '\n\n'.join(text_elements)
    return text


def parse():
    URL = input('Enter URL for parsing: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        raw_text = get_content(html.text)
        print(raw_text)
    else:
        print('Error')


parse()