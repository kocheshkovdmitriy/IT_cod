import requests
import re


def get_dog():
    url = "https://random.dog/"
    response = requests.request(method='GET', url=url, timeout=1)

    if response.status_code == 200:
        return  url + re.search('src=".*?"', response.text).group()[5:-1]
    return f"Ошибка запроса на сайт https://random.dog/"

