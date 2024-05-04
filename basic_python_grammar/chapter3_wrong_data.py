import pandas as pd
import numpy as np

ns_book = pd.read_csv("data/ns_202405.csv", index_col = 0)
ns_book = ns_book[['도서명', '저자', 'ISBN', '발행년도', '출판사', '부가기호']]

#ns_book.astype({'발행년도': 'int32'})

# ns_book['발행년도']=='1988'처럼 쓰면 정확히 '1988'인 것만 찾고, '1988.'와 같은 것은 제외됩니다.
# contains() 메서드는 주어진 문자열이 포함된 모든 행을 찾습니다.
print(ns_book['발행년도'].str.contains('1988').sum())

invalid_number = ns_book['발행년도'].str.contains('\D', na = True)

print(invalid_number.sum())
print(ns_book[invalid_number].head())

# 정규식 이용하여 발행년도 앞과 뒤에 있는 문자 삭제
ns_book1 = ns_book.replace({'발행년도': r'(\d{4}).*'}, r'\1', regex=True)
print(ns_book1[invalid_number].head(5))

# 숫자 이외의 문자가 들어간 행의 개수와 데이터를 확인해보기
unknown_year = ns_book1['발행년도'].str.contains('\D', na=True)
print(unknown_year.sum())
print(ns_book1[unknown_year].head(5))

# 임의로 -1로 값 바꾸기
ns_book1.loc[unknown_year, '발행년도'] = '-1'
ns_book1 = ns_book1.astype({'발행년도': 'int32'})

# 연도가 4000년이 넘는 행의 전체 개수 확인
# print(ns_book1['발행년도'].gt(4000).sum())

# 위의 코드와 같은 코드
(ns_book1['발행년도']>4000).sum()

# 4000년이 넘는 연도에서 2333을 빼서 서기로 바꾼 다음 연도가 4000이 넘는 것이 있는지 확인
dangun_yy_rows = ns_book1['발행년도'].gt(4000)
ns_book1.loc[dangun_yy_rows, '발행년도'] = ns_book1.loc[dangun_yy_rows, '발행년도'] - 2333
dangun_year = ns_book1['발행년도'].gt(4000)
# print(dangun_year.sum())
# print(ns_book1[dangun_year].head(2))

# 연도가 이상하게 높은 도서들은 -1로 표시
ns_book1.loc[dangun_year, '발행년도'] = -1

# 연도가 작은 값 찾기
old_books = ns_book1['발행년도'].gt(0) & ns_book1['발행년도'].lt(1900)
# print(ns_book1[old_books])

# 이도서를 -1로 설정하고 전체 행 개수 확인
ns_book1.loc[old_books, '발행년도'] = -1
print(ns_book1['발행년도'].eq(-1).sum())

# 누락된 정보 채우기
# 도서명, 저자, 출판사 열에 누락된 값이 있거나, 발행년도 열이 -1인 행의 개수를 확인해보기
na_rows = ns_book1['도서명'].isna() | ns_book1['저자'].isna() | ns_book1['출판사'].isna() | ns_book1['발행년도'].eq(-1)

print(na_rows.sum())
print(ns_book1[na_rows].head(2))

# BeautifulSoup을 이용해서 누락된 정보를 채우기
import requests
from bs4 import BeautifulSoup

def get_book_title(ISBN):
    # Yes24 도서 검색 페이지 URL
    url = 'https://www.yes24.com/Product/Search?domain=BOOK&query={}'
    # URL에 ISBN을 넣어 HTML 가져옵니다.
    r = requests.get(url.format(ISBN))
    soup = BeautifulSoup(r.text, 'html.parser') # HTML parsing
    # Class name is 'gd_name' and get the <a> tag
    title = soup.find('a', attrs = {'class': 'gd_name'}).get_text()
    return title

# 도서명 추출 성공
get_book_title(9791191266054)

# 같은 방식으로 저자, 출판사, 발행 연도를 추출하는 함수 만들기


    
