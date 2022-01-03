import pandas as pd
import openpyxl

df = pd.read_csv('promodescuentos-nuevas-11281.csv')

df.to_excel("promodescuentos-nuevas-nov-2-date.xlsx", encoding="utf-8")

