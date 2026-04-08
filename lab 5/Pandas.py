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