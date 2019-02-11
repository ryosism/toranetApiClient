import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "tp00000"
PASS = "xxxxxxxx"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "userId":USER,
    "password":PASS,
    "buttonName":"",
    "lang":1
}

# action
url_login = "https://tora-net.sti.chubu.ac.jp/portal/top.do"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

soup = BeautifulSoup(res.text, features='lxml')
print(soup.prettify())
