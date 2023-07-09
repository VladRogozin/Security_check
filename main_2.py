from bs4 import BeautifulSoup
import requests
import threading
from urllib.parse import urljoin
from check_base import load_and_response_time, content_size, status_code
from check_sql_injection import check_sql_injection
from check_xss_vulnerability import check_xss_vulnerability


LOCKER = threading.Lock()

def scan_page(url):
    response = requests.get(url,  timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            absolute_url = urljoin(url, href)
            thread = threading.Thread(target=check_link, args=(absolute_url,))
            thread.start()


def check_link(url):
    with LOCKER:
        response = requests.get(url)
        status_code(response, url)
        content_size(response, url)
        load_and_response_time(url)
        check_xss_vulnerability(response, url)
        check_sql_injection(url)


if __name__ == '__main__':
    start_url = 'https://www.youtube.com/'
    scan_page(start_url)