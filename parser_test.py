import requests
import textwrap
from bs4 import BeautifulSoup as BS


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.45 Safari/537.36',
    'accept': '*/*'
}


FILE = 'formatted_text.txt'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BS(html, 'html.parser')
    text_elements = [t.get_text() for t in soup.find_all('p')]
    text = '\n\n'.join(text_elements)
    return text


def save_file(text, new_file):
    width = int(
        input('Enter the number for maximum '
              'number of characters in a line: ')
    )
    should_save = input(
        'Would you like to create new txt file? '
        'Input "Yes" or "No: '
    )
    ready_str = textwrap.fill(
        text,
        width=width,
        replace_whitespace=False,
        break_long_words=False
    )
    print(ready_str)
    if should_save.strip() == 'Yes':
        with open(new_file, 'w', encoding="utf-8") as file:
            file.write(ready_str)


def parse():
    URL = input('Enter URL for parsing: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        raw_text = get_content(html.text)
        save_file(raw_text, FILE)
    else:
        print('Error')


parse()
