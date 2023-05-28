import requests
from bs4 import BeautifulSoup


URLS = [
    "https://www.nollyverse.com/serie/house-m-d/season-3",
    "https://www.nollyverse.com/serie/house-m-d/season-4",
    "https://www.nollyverse.com/serie/house-m-d/season-5",
    "https://www.nollyverse.com/serie/house-m-d/season-6",
    "https://www.nollyverse.com/serie/house-m-d/season-7",
    "https://www.nollyverse.com/serie/house-m-d/season-8",
]
BTN_CLASS = 'btn-danger'
HEADER = '#!/bin/bash'
PREFIX = 'aria2c -c -x 4 --http-proxy="http://username:password@proxyserver:port" '
OUTPUT_PATH = 'DrHouseDownloader.sh'


def parse(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    for link in soup.find_all('a', BTN_CLASS):
        yield link.get('href')
    return


def get_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        print('All is good!')
        return r.text


def create_script(urls):
    doc = HEADER + '\n'
    for url in urls:
        for line in parse(get_page(url)):
            doc += PREFIX + line + ' ; \\ \n'
    doc += 'echo "END"'
    return doc


def main():
    with open(OUTPUT_PATH, 'w') as fs:
        fs.write(create_script(URLS))


if __name__ == '__main__':
    main()
