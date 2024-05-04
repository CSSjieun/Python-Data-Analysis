import pandas as pd
import numpy as np

ns_book = pd.read_csv("data/ns_202405.csv", index_col = 0)
ns_book = ns_book[['도서명', '저자', 'ISBN', '발행년도', '출판사', '부가기호']]

# print(ns_book.head(5))

ns_book = ns_book.replace({'부가기호': {np.nan: 'none'}})

# 패턴에 맞는 문자열을 찾은 후 첫 번째 그룹에 해당하는 뒷자리 연도 두 개를 추출합니다.
# 패턴 안에 있는 그룹을 나타낼 때는 \1, \2처럼 사용합니다.
# 그룹의 번호는 패턴 안에 등장하는 순서대로 매겨집니다.
print(ns_book.replace({'발행년도': {r'\d\d(\d\d)': r'\1'}}, regex=True)[100:102]) # 패턴 안에 있는 첫 번째 그룹으로 연도를 바꿉니다.

# 위 코드와 같은 코드
ns_book.replace({'발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex=True)[100:102]

# 정규 표현식 활용
print(ns_book.replace({'저자': {r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)': r'\1\2'},
                 '발행년도': {r'\d{2}(\d{2})': r'\1'}}, regex = True)[100:106])