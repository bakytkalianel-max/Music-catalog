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

#2
genre_list = df["Genre"].unique().tolist()
key_list = df["Key"].unique().tolist()
print("\nУникальные жанры:")
print(genre_list)
print("\nУникальные ключи:")
print(key_list)