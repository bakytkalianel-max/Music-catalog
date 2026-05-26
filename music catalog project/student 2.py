#2.1
import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)
df = pd.read_excel(r"C:\Users\Acer\Documents\music_catalog.xlsx")
numeric_columns = [
    "Year",
    "Duration_sec",
    "BPM",
    "Energy",
    "Danceability",
    "Popularity",
    "Streams_million",
    "Awards_won",
    "Awards_nominated",
    "User_Rating"
]
numeric_data = df[numeric_columns].to_numpy()
print("Форма массива:")
print(numeric_data.shape)
print("\nПервые 5 строк массива:")
print(numeric_data[:5])

# 2.2
stat_columns = ["Streams_million", "User_Rating", "Popularity"]
for col in stat_columns:
    mean_value = df[col].mean()
    median_value = df[col].median()
    std_value = df[col].std()

    print(f"\n{col}:")
    print(f"mean = {mean_value}")
    print(f"median = {median_value}")
    print(f"std = {std_value}")

#2.3
streams = df["Streams_million"].to_numpy()
ratings = df["User_Rating"].to_numpy()
indexes = np.where((streams > 200) & (ratings >= 8))[0]
popular_tracks = df.iloc[indexes]

print("Первые 10 популярных треков:")
print(popular_tracks[["Title", "Artist", "Streams_million", "User_Rating"]].head(10))

# 2.4
explicit_by_genre = {}
for genre in df["Genre"].unique():
    count = df[(df["Genre"] == genre) & (df["Explicit"] == 1)].shape[0]
    explicit_by_genre[genre] = count
print("\nКоличество explicit-треков по жанрам:")
print(explicit_by_genre)

top_3_explicit = sorted(
    explicit_by_genre.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]
print("\nТоп-3 жанра по explicit-трекам:")
print(top_3_explicit)