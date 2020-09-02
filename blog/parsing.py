import requests
import re

from bs4 import BeautifulSoup
from datetime import datetime

from .models import News



def parsing_tut_by():
    resourses = [
        'https://news.tut.by/rss/index.rss',
    ]
    for r in resourses:
        result = requests.get(r)
        soup = BeautifulSoup(result.text, 'xml')
        data = soup.find_all('item')

        for block in data:

            title = block.find('title').string
            if not News.objects.filter(title=title).exists():
                link = block.find('link').string
                date_str = block.find('pubDate').string
                date = re.findall(r",\s(.*)\s\+", date_str)[0]
                date = datetime.strptime(date, '%d %b %Y %H:%M:%S')

                desc = str(block.find('description'))

                try:
                    description = re.findall(r"&gt;(.+)&lt", desc)[0]
                except IndexError:
                    continue

                category = block.find('category').string

                if block.find('atom:name') and block.find('atom:uri'):
                    author_name = block.find('atom:name').string
                    author_uri = block.find('atom:uri').string
                    News.objects.create(title=title, link=link, date=date, description=description,
                                        category=category, author_name=author_name, author_uri=author_uri)
                else:
                    News.objects.create(title=title, link=link, date=date, description=description,
                                        category=category)

