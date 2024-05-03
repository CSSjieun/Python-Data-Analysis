import pandas as pd
import numpy as np

ns_book4 = pd.read_csv("ns_book4.csv", low_memory=False)
print(ns_book4.head())
print(ns_book4.info())

# 누락된 값 개수 확인하기 isna()
print(ns_book4.isna().sum())
print(ns_book4.notna().sum())

# 누락된 값 바꾸기 
isbn_na_rows = ns_book4['ISBN'].isna() # 누락된 값을 찾아 불리언 배열로 반환합니다.
ns_book4.loc[isbn_na_rows, 'ISBN'] = '' # 누락된 값을 빈 문자열로 바꿉니다.
print(ns_book4['ISBN'].isna().sum()) # 누락된 값이 몇 개인지 셉니다.

# fillna() 사용
print(ns_book4.fillna("none").isna().sum())

# 특정 열만 선택해서 NaN을 바꾸기
print(ns_book4['도서명'].fillna('none').isna().sum())

# 특정 열의 NaN을 바꾸면서 전체 데이터 프레임을 반환하기
print(ns_book4.fillna({'도서명': 'none'}).isna().sum()) # 딕셔너리 형태

# 누락된 값 바꾸기 2 replace()
# 1. 바꾸려는 값이 하나일 때
# replace(원래 값, 새로운 값)
print(ns_book4.replace(np.nan, "none").isna().sum())

# 2. 바꾸려는 값이 여러개 일 때
# replace([원래 값1, 원래 값2], [새로운 값1, 새로운 값2])
print(ns_book4.replace([np.nan, '2021'], ['none', '21']).head(2))
print(ns_book4.replace({np.nan: 'none', '2021': '21'}).head(2))

# 3. 열 마다 다른 값으로 바꿀 때
# 열 이름과 바꾸려는 값을 딕셔너리 형식으로 전달하여 열마다 다른 값을 바꿀 수 있습니다.
# replace({열 이름: 원래 값}, 새로운 값)
print(ns_book4.replace({'권': np.nan}, 'none').head(3))