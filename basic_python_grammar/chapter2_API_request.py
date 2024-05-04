import requests
import pandas as pd

url = "https://data4library.kr/api/loanItemSrch?format=json&startDt=2024-03-01&endDt=2024-03-31&age=20&authKey=8657bab1a580b3695a6fee9dcd7fd94424b42f9edcdb8396ce635a17550ae6cc"
r = requests.get(url)

data = r.json()
print(data)

# doc 키에 매핑된 딕셔너리를 추출한 후 리스트에 추가하기
books = []
for d in data['response']['docs']:
    books.append(d['doc'])

# 앞 코드와 같은 코드
books = [d['doc'] for d in data['response'['docs']]]

# 판다스 DataFrame 클래스에 이 리스트를 넘겨보기
books_df = pd.DataFrame(books)
books_df

# books_df의 내용을 JSON으로 변환해서 저장하기
books_df.to_json('20s_best_book.json', force_ascii = False)





