#11
import numpy as np

def price_array(products):
    prices = [product.price for product in products]
    return np.array(prices)
#12
def get_price_array(prices):
    mean_price = float(np.mean(prices))
    median_price = float(np.median(prices))
    return (mean_price, median_price)
prices= np.array([1200.0, 25.0, 450.0])
a=get_price_array(prices)
print(a)
#13
def norm_prices(prices):
    min_p= np.min(prices)
    max_p= np.max(prices)
    return (prices - min_p) / (max_p - min_p)
prices= np.array([1200.0, 25.0, 450.0])
a=norm_prices(prices)
print(a)

#14
import numpy as np

class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
def get_categories(products):
    categories = [product.category for product in products]
    return np.array(categories)
products = [
    Product(1,"Laptop",1200.0,"Electronics"),
    Product(2,"T-Shirt",20.0,"Clothing")
]
print(get_categories(products))

#15
def unique_categories(categories):
    return len(set(categories))
#16
def expensive_prices(products, prices):
    mean_price = float(np.mean(prices))
    return [product for product in products if product.price > mean_price]

#17
def apply_disconut(prices):
    return prices * 0.9
a=np.array([1200.0, 25.0, 450.0])
print(apply_disconut(a))

#18
def orders_array(orders):
    result = []
    for order in orders:
        total = sum(product.price for product in order.products)
        result.append([total])
    return np.array(result)
#19
def average_order(orders_array):
    return np.mean(orders_array)
#20
def get_expensive_prices(prices):
    return np.where(prices > 1000)[0]