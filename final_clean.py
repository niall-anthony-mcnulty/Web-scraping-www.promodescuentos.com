import pandas as pd
import openpyxl

df = pd.read_csv('promodescuentos-nuevas-39981.csv')

df.to_excel("promodescuentos-nuevas-final.xlsx", encoding="utf-8")

