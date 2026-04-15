#21
import pandas as pd
from datetime import date

def users_dateframe(users):
    data=[]
    for user in users:
        data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "registration_date": user.registration_date
        })
    return pd.DataFrame(data)
#22
import pandas as pd
class Product:
    def __init__(self,id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

def product_dataframe(products):
    data=[]
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price
        })
    return pd.DataFrame(data)
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"T-Shirt",20.0,"Clothing")
]
print(product_dataframe(products))

#23
def users_orders(users_df, orders_df):
    merged = pd.merge(
        orders_df,
        users_df,
        left_on="user_id",
        right_on="id"
    )
    merged = merged[["order_id","name","total"]]
    merged = merged.rename(columns={"name":"user_name"})
    return merged
users_df = pd.DataFrame({
    "id": [1, 2],
    "name": ["John", "Alice"]
})
orders_df = pd.DataFrame({
    "order_id": [101, 102],
    "user_id": [1, 2],
    "total": [1200, 25]
})
print((users_df, orders_df))

#24
def filter_orders(df, value):
    return df[df["total"] > value]
df = pd.DataFrame({
    "order_id": [101, 102],
    "user_name": ["John", "Alice"],
    "total": [1200, 25]
})
print(filter_orders(df, 100))

#25
def group_orders(df):
    result =df.groupby("user_name")["total"].sum().reset_index()
    result = result.rename(columns={"total":"total_sum"})
    return result
df = pd.DataFrame({
    "order_id": [101, 102],
    "user_name": ["John", "Alice"],
    "total": [1200, 25]
})
print(group_orders(df))

#26
def average_orders(df):
    result =df.groupby("user_name")["total"].mean().reset_index()
    result = result.rename(columns={"total":"total_mean"})
    return result
print(average_orders(df))

#27
def count_orders(df):
    result = df.groupby("user_name")["order_id"].count().reset_index()
    result = result.rename(columns={"order_id":"count"})
    return result
print(count_orders(df))

#28
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Laptop", "Mouse", "Shirt"],
    "category": ["Electronics", "Electronics", "Clothing"],
    "price": [1200, 25, 20]
})
def category_mean_price(df):
    result =df.groupby("category")["price"].mean().reset_index()
    result = result.rename(columns={"price":"mean_price"})
    return result
print(category_mean_price(df))

#29
def add_discount(df):
    df["discount_price"] = df["price"] * 0.9
    return df
print(add_discount(df))

#30
def sort_products(df):
    return df.sort_values(by="price", ascending=False)
print(sort_products(df))