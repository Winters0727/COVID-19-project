import lxml
import requests
import bs4
import pandas as pd
import os

# 3월 5일 이후의 포맷에 맞춰져 있습니다. 이전 데이터를 가져오려면 코드를 변경해야합니다.

file_list = os.listdir()
if 'dataset' not in file_list:
    os.mkdir('dataset')

data_list = os.listdir('dataset')

def update_dataset(url, title):
    global data_list
    if (title + '.csv') in data_list:
        return None
    response = requests.get(url)
    BS = bs4.BeautifulSoup(response.text, features='lxml')
    ct = BS.select('td > p > span')
    for idx, info in enumerate(ct):
        if info.text == '총계':
            main_idx = idx
            break

    df = pd.DataFrame([
    [ct[main_idx+12].text,ct[main_idx+13].text,ct[main_idx+14].text,ct[main_idx+15].text,ct[main_idx+16].text,ct[main_idx+17].text,ct[main_idx+18].text,ct[main_idx+19].text],
    [ct[main_idx+25].text,ct[main_idx+26].text,ct[main_idx+27].text,ct[main_idx+28].text,ct[main_idx+29].text,ct[main_idx+30].text,ct[main_idx+31].text,ct[main_idx+32].text],
    [ct[main_idx+34].text,ct[main_idx+35].text,ct[main_idx+36].text,ct[main_idx+37].text,ct[main_idx+38].text,ct[main_idx+39].text,ct[main_idx+40].text,ct[main_idx+41].text]
],\
    index=[ct[main_idx+7].text + ct[main_idx+8].text + ct[main_idx+9].text + ct[main_idx+10].text + ct[main_idx+11].text, ct[main_idx+20].text + ct[main_idx+21].text + ct[main_idx+22].text + ct[main_idx+23].text + ct[main_idx+24].text, ct[main_idx+33].text],\
    columns=['총계','계(확진)', '격리해제', '격리 중', '사망', '계(검사)', '검사 중', '결과 음성'])

    df.to_csv('dataset/' + title + '.csv', encoding='cp949')

N = input('# of pages : ')

base_url = 'https://www.cdc.go.kr'

for j in range(int(N), 1, -1):
    find_url = 'https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015&nPage={0}'.format(j)

    find_response = requests.get(find_url)
    find_BS = bs4.BeautifulSoup(find_response.text, features='lxml')

    find_article = find_BS.find_all('li', {'class' : 'title'})
    for article in find_article:
        if '코로나바이러스감염증-19 국내 발생 현황' in str(article):
            title = article.a.get('title')
            url = base_url + article.a.get('href')
            update_dataset(url, title)