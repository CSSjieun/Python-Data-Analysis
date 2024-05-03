import pandas as pd

ns_df = pd.read_csv("ns_202405.csv", low_memory=False, index_col = 0)
print(ns_df.columns)
print(ns_df.columns[0])

# column에서 부가기호 열 빼고 추출
selected_columns = ns_df.columns != '부가기호'
ns_book = ns_df.loc[:, selected_columns]
print(ns_book.head())

# 열이나 행을 삭제하는 drop() 메서드
ns = pd.read_csv("ns_202405.csv")
print(ns.head())

ns_book = ns.drop(['Unnamed: 0', '부가기호'], axis = 1) # axis = 0 행 삭제, axis = 1 열 삭제
print(ns_book.head())

ns_book.drop('주제분류번호', axis = 1, inplace = True) # inplace = True 선택한 데이터프레임에 덮어쓴다.
print(ns_book.head())

# NA 삭제
ns_book = ns_book.dropna(axis = 1)
print(ns_book.head())

# 모든 값이 NaN인 열을 삭제: how = 'all'
ns_book = ns_book.dropna(axis = 1, how = 'all')
print(ns_book.head())

# 행삭제
ns_book2 = ns_book.drop([0,1])
print(ns_book2.head())

ns_book2 = ns_book[0:2]
print(ns_book2.head())

# 출판사가 한빛미디어인 경우
selected_rows = ns['출판사'] == '한빛미디어'
ns_book2 = ns_book[selected_rows]
print(ns_book2.head())

# 대출건수가 1000이하인 행 삭제
ns_book2 = ns[ns['대출건수']>1000]
print(ns_book2.head())

# 중복된 행 찾기
print(sum(ns_book.duplicated()))

# 일부 열을 기준으로 중복된 행 찾기
print(sum(ns.duplicated(subset=['도서명', '저자', 'ISBN'])))

# 중복된 데이터 확인
ns_book = ns[['도서명', '저자', 'ISBN']]
print(ns_book.head())
dup_rows = ns_book.duplicated(subset=['도서명','저자','ISBN'], keep=False)
ns_book3 = ns_book[dup_rows]
print(ns_book3.head())

# 그룹별로 모으기
ns_book = ns[['도서명', '저자', 'ISBN', '권','대출건수']]
group_df = ns_book.groupby(by=['도서명','저자','ISBN','권'], dropna=False) # dropna -> NaN이 있는 행을 삭제하지 않습니다.
loan_count = group_df.sum()
print(loan_count.head())

loan_count = ns_book.groupby(by=['도서명','저자','ISBN','권'],dropna = False).sum()
print(loan_count.head())

# 고유한 행만을 가지고 있는 데이터프레임 만들기
dup_rows = ns.duplicated(subset = ['도서명','저자','ISBN','권']) # 1. 중복된 행을 True로 표시합니다.
unique_rows = ~dup_rows # 2. 불리언 배열을 반전시켜 고유한 행을 True로 표시합니다.
ns_book3 = ns[unique_rows].copy() # 3. 고유한 행만 선택합니다.

print(sum(ns_book3.duplicated(subset=['도서명','저자','ISBN','권'])))

# 원본 데이터프레임 인덱스 설정하기
ns_book3.set_index(['도서명','저자','ISBN','권'], inplace = True)
ns_book3.drop('Unnamed: 0', axis = 1, inplace = True)
print(ns_book3.head())

# update하기
ns_book3.update(loan_count)
print(ns_book3.head())

# 인덱스 열 해제
ns_book4 = ns_book3.reset_index()
print(ns_book4.head())

# 대출건수가 100회 이상인 책의 개수 세기
print(ns_book4[ns_book4['대출건수']>100])
print(sum(ns_book['대출건수']>100))
print(sum(ns_book4['대출건수']>100))

# 열의 순서 바꾸기
ns_book4 = ns_book4[ns_book.columns]
print(ns_book4.head())

# 데이터 저장하기
ns_book4.to_csv('ns_book4.csv', index = False)