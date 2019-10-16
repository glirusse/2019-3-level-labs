from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import urllib.request


# 1. Crawler

def valid():
    urllib.request.urlopen("https://3dnews.ru/").getcode()
    r1 = urllib.request.urlopen("https://3dnews.ru/").getcode()
    if r1 == 200:
        return r1
    else:
        print('invalid URL')


valid()
# 1.1. valid url

siteurl = 'https://3dnews.ru/'
page = requests.get(siteurl)
page.encoding = 'utf-8'
html_page = page.text

soup = BeautifulSoup(html_page, 'html.parser')
divs = soup.find('div', id='section-content')
heads = soup.find_all('h1')
heads_list = [i.get_text().strip() for i in heads]
print(heads_list)

# 1.2. parser
now = datetime.now()
articles = [{'title': i} for i in heads_list]
articlesjs = {'url': 'https://3dnews.ru/', 'creation Date': '{0}'.format(now.strftime("%d/%m/%Y %H:%M:%S")),
              'articles': articles}
with open("articles.json", "w") as file:
    json.dump(articlesjs, file, indent=2, ensure_ascii=False)
# 1.3. json
