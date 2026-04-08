#11
import numpy as np
def price_array(products):
    prices = [product.price for product in products]
    return np.array(prices, dtype=float)
