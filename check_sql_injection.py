import requests


def check_sql_injection(url):
    payload = "' OR '1'='1"
    modified_url = url + payload
    response = requests.get(modified_url)
    content = response.text

    if "error" in content:
        print(f"Scanning {url} - Vulnerable to SQL injection")

    params = {'param': payload}
    response = requests.get(url, params=params)

    if response.status_code == 200 and "error" in response.text:
        print(f"Scanning {url} - Vulnerable to SQL injection (through params)")