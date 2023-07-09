import time
import requests


def load_and_response_time(url):
    # LOAD TIME
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    print(f"Scanning {url} - Load time: {load_time} seconds")

    # Response time
    response_time = response.elapsed.total_seconds()
    print(f"Scanning {url} - Response time: {response_time} seconds")


def content_size(response, url):
    content_size = len(response.content)
    print(f"Scanning {url} - Content size: {content_size} bytes")


def status_code(response, url):
    status = response.status_code
    print(f"status {status}")