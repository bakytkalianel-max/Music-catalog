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