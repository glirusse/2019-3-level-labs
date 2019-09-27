from bs4 import BeautifulSoup
from datetime import datetime
import requests

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

siteurl = 'https://3dnews.ru/'
page = requests.get(siteurl)
page.encoding = 'utf8'
html_page = page.text

soup = BeautifulSoup(html_page, 'html.parser')
divs = soup.find('div', id='section-content')
heads = soup.find_all('h1')
heads_list = [i.get_text().strip() for i in heads]
print(heads_list)
