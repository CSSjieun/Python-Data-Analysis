import gdown
#gdown.download('https://bit.ly/3pK7iuu', 'ns_book7.csv', quiet=False)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ns_book7 = pd.read_csv('ns_book7.csv', low_memory=False)
print(ns_book7.head())

# plt.scatter([1,2,3,4],[1,2,3,4])
# plt.show()

# plt.scatter(ns_book7['번호'], ns_book7['대출건수'])
# plt.show()

# plt.scatter(ns_book7['도서권수'], ns_book7['대출건수'], alpha = 0.1) # alpha 0에 가까울 수록 투명하고 1에 가까울수로 불투명하게 그려집니다. 
# plt.show()

# print(ns_book7['도서권수'].quantile(.9))

# plt.scatter((ns_book7['대출건수']/ns_book7['도서권수']), ns_book7['대출건수'], alpha=0.1)
# plt.show()

# plt.hist([0,3,5,6,7,7,9,13], bins=5)
# plt.show()

# print(np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5))

# 넘파이의 randn() 함수는 표준정규분포를 따르는 랜덤한 실수를 생성할 수 있습니다.
# 이 함수에 원하는 샘플 개수를 전달하여 난수 random number을 생성해보겠습니다.

np.random.seed(42)
random_samples = np.random.randn(1000)
# print(random_samples)

# 표준정규분포를 따르는지 평균값과 표준편차를 확인하기
# print(np.mean(random_samples), np.std(random_samples))

# 히스토그램으로 그려보기
# plt.hist(random_samples)
# plt.show()

# plt.hist(ns_book7['대출건수'])
# plt.show()

# change y axis in log scale
# plt.hist(ns_book7['대출건수'])
# plt.yscale('log')
# plt.show()

# plt.hist(ns_book7['대출건수'], bins=100)
# plt.yscale('log')
# plt.show()

# title_len = ns_book7['도서명'].apply(len) # title_len 변수는 각 도서명의 길이가 젖아된 판다스 시리즈 객체가 됩니다.
# plt.hist(title_len, bins=100)
# plt.xscale('log')
# plt.show()

# plt.boxplot(ns_book7[['대출건수', '도서권수']], whis=(0,100))
# plt.yscale('log')
# plt.show()


