import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_page_cnt(isbn):
    # Yest24 도서 검색 페이지 URL
    url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져오기
    r = requests.get(url.format(isbn))
    soup = BeautifulSoup(r.text, 'html.parser') # HTML 파싱
    # 검색 결과에서 해당 도서를 선택합니다.
    prd_info = soup.find('a', attrs={'class':'gd_name'})
    if prd_info == None:
        return ''
    # 도서 상세 페이지를 가져옵니다.
    url = 'http://www.yes24.com'+prd_info['href']
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    # 품목정보 <div>를 선택합니다.
    prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
    # 테이블에 있는 <tr> 태그를 가져옵니다.
    prd_tr_list = prd_detail.find_all('tr')
    # 쪽수가 들어 있는 <th>를 찾아서 <tb>에 담긴 값을 반환합니다.
    for tr in prd_tr_list:
        if tr.find('th').get_text() == '쪽수, 무게, 크기':
            return tr.find('td').get_text().split()[0]
    return ''

#print(get_page_cnt(9791190090018))
#print(get_page_cnt(9791198517425))

ns = pd.read_csv("ns_202405.csv", index_col = 0)
print(ns.head())

books = ns[['번호', '도서명', '저자', 'ISBN', '대출건수']]
top10_books = books.head(10)

def get_page_cnt2(row):
    isbn = row['ISBN']
    return get_page_cnt(isbn)

page_count = top10_books.apply(get_page_cnt2, axis=1)
print(page_count)

# page_count 시리즈 객체에 이름을 지정해줍니다.
page_count.name = 'page_count'
print(page_count)

top10_with_page_count = pd.merge(top10_books, page_count, left_index = True, right_index = True)
print(top10_with_page_count)