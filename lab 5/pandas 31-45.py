#31
import pandas as pd

df = pd.DataFrame({
    "order_id": [101, 102],
    "product_name": ["Laptop", "Mouse"],
    "price": [1200, 25]
})
def add_quantity(df):
    df["quantity"] = 1
    return df
print(add_quantity(df))

#32
import pandas as pd

df = pd.DataFrame({
    "order_id": [101, 102],
    "product_name": ["Laptop", "Mouse"],
    "price": [1200, 25],
    "quantity": [2, 3]
})
def add_total_price(df):
    df["total_price"] = df["quantity"] * df["price"]
    return df
print(add_total_price(df))

#33
import pandas as pd
df = pd.DataFrame({
    "product_name": ["Laptop", "T-Shirt"],
    "category": ["Electronics", "Clothing"],
    "price": [1200, 20]
})
def filter_electronics(df):
    return df[df["category"] == "Electronics"]
print(filter_electronics(df))

#34
import pandas as pd
df = pd.DataFrame({
    "product_name": ["Laptop", "Mouse", "Shirt"],
    "category": ["Electronics", "Electronics", "Clothing"],
    "price": [1200, 25, 20]
})
def count_products_by_category(df):
    result = df.groupby("category").size().reset_index(name="count")
    return result
print(count_products_by_category(df))

#35
def mean_price(df):
    result = df.groupby("category")["price"].mean().reset_index()
    result = result.rename(columns={"price": "mean_price"})
    return result
print(mean_price(df))

#36
def sort_by_price(df):
    return df.sort_values(by="price", ascending=False)
print(sort_by_price(df))

#37
import pandas as pd
df = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "total_price": [1200, 50, 500, 1500]
})
def top_n_orders(df, n=3):
    return df.sort_values(by="total_price", ascending=False).head(n)
print(top_n_orders(df, 3))

#38
import pandas as pd
users = pd.DataFrame({
    "user_id": [1, 2],
    "user_name": ["John", "Alice"]
})

orders = pd.DataFrame({
    "order_id": [101, 102],
    "user_id": [1, 2],
    "total_price": [1200, 50]
})
def merge_users_orders(users, orders):
    return pd.merge(orders, users, on="user_id")
print(merge_users_orders(users, orders))

#39
import pandas as pd

df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "total_price": [1200, 500, 50]
})
def mean_order_users(df):
    result = df.groupby("user_name")["total_price"].mean().reset_index()
    result = result.rename(columns={"total_price": "mean_total"})
    return result
print(mean_order_users(df))

#40
import pandas as pd

df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "order_id": [101, 103, 102]
})
def count_orders(df):
    result = df.groupby("user_name")["order_id"].count().reset_index()
    result = result.rename(columns={"order_id": "count"})
    return result
print(count_orders(df))

#41
import pandas as pd
df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "total_price": [1200, 50, 500]
})
def max_order_users(df):
    result = df.groupby("user_name")["total_price"].max().reset_index()
    result = result.rename(columns={"total_price": "max_order"})
    return result
print(max_order_users(df))

#42
import pandas as pd
df = pd.DataFrame({
    "user_name": ["John", "John", "John", "Alice"],
    "category": ["Electronics", "Electronics", "Clothing", "Clothing"]
})
def unique_categories(df):
    result = df.groupby("user_name")["category"].nunique().reset_index()
    result = result.rename(columns={"category": "unique"})
    return result
print(unique_categories(df))

#43
import pandas as pd
df = pd.DataFrame({
    "user_name": ["John", "Alice"],
    "total_price": [1200, 500]
})
def add_vips(df):
    df["VIP"] = df["total_price"] > 1000
    return df
print(add_vips(df))

#44
import pandas as pd
df = pd.DataFrame({
    "user_name": ["John", "Alice", "Bob"],
    "total_sum": [1700, 25, 1700],
    "mean_total": [850, 25, 600]
})
def sort_users(df):
    return df.sort_values(
        by = ["total_sum", "mean_total"],
        ascending =[False, True]
    )
print(sort_users(df))

#45
import pandas as pd

df = pd.DataFrame({
    "user_name": ["John", "John", "Alice"],
    "order_id": [101, 103, 102],
    "total_price": [1200, 500, 25],
    "category": ["Electronics", "Clothing", "Clothing"]
})
def final_report(df):
    result = df.groupby("user_name").agg(
        total_orders = ("order_id", "count"),
        total_sum = ("total_price", "sum"),
        mean_total = ("total_price", "mean"),
        max_order = ("total_price", "max"),
        unique_categories = ("category", "nunique")
    ).reset_index()
    result["VIP"] = result["total_sum"] > 1000
    return result
print(final_report(df))