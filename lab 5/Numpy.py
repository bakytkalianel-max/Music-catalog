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