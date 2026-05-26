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

#2.5
artist_album_set = set(zip(df["Artist"], df["Album"]))
print("\nКоличество уникальных комбинаций Artist + Album:")
print(len(artist_album_set))

#2.6
df["streams_per_award"] = df.apply(
    lambda row: row["Streams_million"] / (row["Awards_won"] + 1),
    axis=1
)
high_efficiency = (
    row for _, row in df[df["streams_per_award"] >= 50].iterrows()
)
result = []
for i, row in enumerate(high_efficiency):
    if i == 10:
        break
    result.append(row)
result_df = pd.DataFrame(result)
print("\nПервые 10 треков high_efficiency:")
print(result_df[["Title", "Artist", "Streams_million", "streams_per_award"]])

#2.7
df["streams_per_award"] = df["Streams_million"] / (df["Awards_won"] + 1)
rating_pivot = pd.pivot_table(
    df,
    index="Genre",
    columns="Year",
    values="User_Rating",
    aggfunc="mean"
)
efficiency_pivot = pd.pivot_table(
    df,
    index="Genre",
    columns="Year",
    values="streams_per_award",
    aggfunc="mean"
)
rating_pivot.to_csv("student2_rating_pivot.csv")
efficiency_pivot.to_csv("student2_efficiency_pivot.csv")
print("Сводные таблицы сохранены.")

#2.8
df.to_excel("student2_music_analysis.xlsx", index=False)
check_df = pd.read_excel("student2_music_analysis.xlsx")
print("\nПроверка чтения файла:")
print(check_df.head())

#2.9
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 5))
plt.hist(df["User_Rating"], bins=20)
plt.title("Distribution of User Rating")
plt.xlabel("User Rating")
plt.ylabel("Count")
plt.grid(True)
plt.savefig("user_rating_histogram.png")
plt.show()

plt.figure(figsize=(10, 6))
genres = df["Genre"].unique()
for genre in genres:
    genre_data = df[df["Genre"] == genre]
    plt.scatter(
        genre_data["Streams_million"],
        genre_data["Popularity"],
        label=genre,
        alpha=0.6
    )
plt.title("Streams vs Popularity")
plt.xlabel("Streams_million")
plt.ylabel("Popularity")
plt.legend()
plt.grid(True)
plt.savefig("streams_vs_popularity.png")
plt.show()

#2.10
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Genre")
plt.title("Count of Tracks by Genre")
plt.xticks(rotation=45)
plt.savefig("genre_countplot.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Genre", y="streams_per_award")
plt.title("Streams per Award by Genre")
plt.xticks(rotation=45)
plt.savefig("streams_per_award_boxplot.png")
plt.show()

plt.figure(figsize=(8, 6))
corr_columns = [
    "User_Rating",
    "Streams_million",
    "Duration_sec",
    "BPM",
    "Popularity"
]
correlation = df[corr_columns].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()
print("\nВсе графики сохранены в PNG.")