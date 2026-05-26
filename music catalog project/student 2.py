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