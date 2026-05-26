#1
import pandas as pd
df = pd.read_excel("music_catalog.xlsx")
print("Первые 5 строк:")
print(df.head())
print("\nФорма DataFrame:")
print(df.shape)
print("\nТипы данных:")
print(df.dtypes)
print("\nПропуски:")
print(df.isnull().sum())