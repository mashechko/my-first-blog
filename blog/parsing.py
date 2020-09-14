import requests
import re

from bs4 import BeautifulSoup
from datetime import datetime

from .models import News


def get_data(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, 'xml')
    data = soup.find_all('item')
    return data


def parsing_tut_by():
    data = get_data('https://news.tut.by/rss/index.rss')

    for block in data:

        title = block.find('title').string
        if not News.objects.filter(title=title).exists():
            link = block.find('link').string
            date_str = block.find('pubDate').string
            date = re.findall(r",\s(.*)\s\+", date_str)[0]
            date = datetime.strptime(date, '%d %b %Y %H:%M:%S')

            desc = block.find('description').string

            try:
                description = re.findall(r"&gt;(.+)&lt", desc)[0]
            except IndexError:
                continue

            category = block.find('category').string

            News.objects.create(title=title, link=link, date=date, description=description,
                            category=category, author='TUT.by')


def parsing_onliner():
    data = get_data('https://www.onliner.by/feed')

    for block in data:
        title = block.find('title').string

        if not News.objects.filter(title=title).exists():
            link = block.find('link').string

            date_str = block.find('pubDate').string
            date = re.findall(r",\s(.*)\s\+", date_str)[0]
            date = datetime.strptime(date, '%d %b %Y %H:%M:%S')

            desc = block.find('description').string

            try:
                description = re.findall(r"</p><p>(.+)</p><p>", desc)[0]
            except IndexError:
                continue

            category = block.find('category').string

            News.objects.create(title=title, link=link, date=date, description=description,
                                category=category, author='Onliner')
