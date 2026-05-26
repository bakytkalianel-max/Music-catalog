#1
import pandas as pd
import numpy as np
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

#3
upper_titles = df["Title"].str.upper().tolist()
title_lengths = df["Title"].str.len().tolist()
mean_length = np.mean(title_lengths)
print(f"Орташа атау ұзындығы: {mean_length:.2f}")

#4
top_tracks = df[
    (df["User_Rating"] >= 8) &
    (df["Streams_million"] >= 100)
]
print("\nТоп популярных треков:")
print(top_tracks[["Title","Artist","Streams_million","User_Rating"]].head(10))