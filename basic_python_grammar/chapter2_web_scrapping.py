import pandas as pd
import requests
from bs4 import BeautifulSoup

ns = pd.read_csv("ns_202405.csv", index_col = 0)
print(ns.head())

books = ns[['번호', '도서명', '저자', 'ISBN', '대출건수']]
print(books.head())

print(books.loc[[0,1], ['도서명', '저자']])

# 슬라이스 연산자 : 사용하기 + step 사용하기 (하나씩 건너뛰면서 실행)
slice = books.loc[::2, '도서명':'ISBN'].head()
print(slice)

# 검색 결과 페이지 HTML 가져오기 request.get()
isbn = 9791190090018 
url = 'http://www.yes24.com/Product/Search?domain=BOOK&query={}'

r = requests.get(url.format(isbn))
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

prd_link = soup.find('a', attrs={'class':'gd_name'})
print(prd_link)

# prd_link로 태그 안의 속성 찾기
print(prd_link['href'])

# 도서 상세 페이지 HTML 가져오기
url = 'http://www.yes24.com'+prd_link['href']
r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
prd_detail = soup.find('div', attrs={'id':'infoset_specific'})
print(prd_detail)

# 앞에 찾은 <div> 태크 안에 다음과 같은 품목정보 테이블이 들어 있습니다.
# 이 테이블에서 '쪽수, 무게, 크기'에 해당하는 행인 <tr> 태그를 찾아 <td> 태그 안에 있는 텍스트를 가져오면 됩니다.
# find_all 메소드를 사용하면 특정 HTML 태그를 모두 찾아서 리스트로 반환해줍니다.
# prd_detail에 포함된 <tr> 태그를 모두 리스트로 만들면 다음과 같습니다.
prd_tr_list = prd_detail.find_all('tr')
print(prd_tr_list)

# prd_tr_list 리스트를 순회하면서 쪽수 행을 찾아 출력해 보기
for tr in prd_tr_list:
    if tr.find('th').get_text() == '쪽수, 무게, 크기':
        page_td = tr.find('td').get_text()
        break
    
print(page_td)

print(page_td.split()[0])

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

get_page_cnt(9791190090018)
