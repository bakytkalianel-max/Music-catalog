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