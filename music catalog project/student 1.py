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

#5
df["total_awards"] = df["Awards_won"] + df["Awards_nominated"]
top_awards = df.sort_values(by="total_awards", ascending=False).head(10)
print("\nТоп-10 треков по наградам:")
print(top_awards[["Title", "Artist", "Awards_won", "Awards_nominated", "total_awards"]])

#6
top_tracks.to_excel("student1_top_tracks.xlsx", index=False)
print("\nФайл student1_top_tracks.xlsx успешно сохранён")

#7
song_1_tracks = df[df["Title"].str.contains("Song_1", case=False, na=False)]
print(song_1_tracks[["Title", "Artist", "Genre", "User_Rating"]])

#8
top_streams = df.sort_values(by="Streams_million", ascending=False).head(10)
print("\nТоп-10 по стримам:")
print(top_streams[["Title", "Artist", "Streams_million"]])
shortest_tracks = df.sort_values(by="Duration_sec", ascending=True).head(10)
print("\n10 самых коротких треков:")
print(shortest_tracks[["Title", "Artist", "Duration_sec"]])