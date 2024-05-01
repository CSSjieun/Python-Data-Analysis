# JSON구조 만들기 - dictionary
d = {"name": "data analysis"}
print(d['name'])

# JSON 형태로 변환하기 - json.dumps()
import json

d_str = json.dumps(d)
print(d_str)

# 문자열 객체인지 확인하기
print(type(d_str))

# JSON파일을 다시 text 기반 dictionary로 바꾸기
d2 = json.loads(d_str)
print(d2['name'])

print(type(d2))

# 좀 더 복잡한 구조 - JSON 문자열을 json.loads() 함수에 직접 전달하기
d3 = json.loads('{"name":"data analysis", "author":"egoing", "year":2024}')
print(d3['name']); print(d3['author']); print(d3['year'])

# 좀 더 복잡한 구조 - author 키에 여러 항목 넣기 
d4 = json.loads('{"name":"data analysis", "author":["egoing", "noname"], "year":2024}')
print(d4['author'][1])

# 좀 더 복잡한 구조 - 두개의 도서를 하나의 JSON 배열로 나타내기
d5_str = """
[
    {"name":"data analysis", "author":"egoing", "year":2024},
    {"name":"data science", "author":"noname", "year":2023}
]
"""

d5 = json.loads(d5_str)
print(d5[0]['name'])

# JSON 문자열을 데이터프레임으로 변환하기: read_josin()
import pandas as pd
print(pd.read_json(d5_str))

# JSON을 Data Frame 클래스 이용해서 데이터 프레임으로 바꾸기
print(pd.DataFrame(d5))

# XML
x_str = """
<book>
    <name> data analysis </name>
    <author> noname </author>
    <year> 2024 </year>
</book>
"""

import xml.etree.ElementTree as et
book = et.fromstring(x_str)
print(type(book))
print(book.tag)

