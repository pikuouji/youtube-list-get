import requests
import bs4
from bs4 import BeautifulSoup
from urllib import request
import gspread
import json
import datetime
from time import sleep
import sys

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)

date = now.strftime('%Y年%m月%d日 %H:%M:%S')
print(date)

# スクレイピング
# URLの指定
url = "https://www.youtube.com/playlist?list=PLmzORdod514DyGHpR_nrkGIIzig2ghlpv"
#ユーザーエージェントの設定（設定必須）
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
# ここでcookieを指定
cookie = {'age_check_done': '1'}  #クッキーの指定
#htmlの取得
#BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(requests.get(url=url, headers=headers).content, 'html.parser', from_encoding="utf-8")

print(soup)

listA = [i.text for i in soup.find_all(class_='yt-simple-endpoint style-scope ytd-playlist-video-renderer')]
listA.insert(0,date)

listB = [listA]
print(listB)
