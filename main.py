from flask import requests
from bs4 import BeautifulSoup
import os

data = []

page_url = 'http://lol-yordle.blog.jp/'
r = requests.get(page_url)
soup = BeautifulSoup(r.text, features='html.parser')
h1_tags = soup.find_all('h1', class_='article-title')

for h1_tag in h1_tags:
    a_tags = h1_tag.find_all('a')
    a_tag = a_tags[0]
    title = a_tag.text
    url = a_tag.get('href')
    data.append([title, url])

# メッセージ作成
msg = ""
for i in range(5):
  d = data[i]
  msg = msg + d[0] + '：' + d[1] + '\n' + '----------------------------------\n'

# Lineに転送
line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
lone_notify_api = os.environ['LINE_NOTIFY_API']
headers = {'Authorization': 'Bearer ' + line_notify_token}
payload = {'message': msg}
requests.post(url=lone_notify_api, data=payload, headers=headers)
