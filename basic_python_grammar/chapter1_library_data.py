# from IPython.display import display
import pandas as pd # read_excel()

ns = pd.read_csv("ns_202405.csv", index_col = 0)
print(ns.head())

