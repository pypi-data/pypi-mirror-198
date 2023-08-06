import json
import re

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from yt_scrape.exceptions import ChannelDeleted

ua = UserAgent()
sess = requests.Session()

def get_content(url):
    headers = {
        'User-Agent': ua.random,
        "Accept-Language": "en-US,en;q=0.5",
        "accept": """text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"""
    }
    try:
        r = sess.get(url, headers=headers)
        r.raise_for_status()
        if r.ok:
            return r.text

    except requests.exceptions.HTTPError:
        raise ChannelDeleted()

    except requests.RequestException:
        raise requests.RequestException


def get_js_script(data: str):
    bs = BeautifulSoup(data, 'lxml')

    try:
        script_tags = bs.find("script", string=re.compile('responseContext'))
        return script_tags.string

    except AttributeError as e:
        print(e)
        return


def extract_json(data: str):
    python_str = re.sub("var ytInitialData = ", "", data, 1)
    main_part = python_str.rsplit('}', 1)[0] + "}"
    try:
        obj = json.loads(main_part)
        return obj

    except json.decoder.JSONDecodeError as e:
        raise e

def data_dict(html):
    content_string = get_js_script(html)
    try:
        obj = extract_json(content_string)
        return obj
    except json.decoder.JSONDecodeError:
        return None
