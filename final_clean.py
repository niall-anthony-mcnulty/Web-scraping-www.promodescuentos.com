import pandas as pd
import openpyxl

df = pd.read_csv('promodescuentos-nuevas-1201.csv')

df.to_excel("promodescuentos-nuevas-first-1201.xlsx", encoding="utf-8")

