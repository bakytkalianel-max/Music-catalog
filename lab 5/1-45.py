#1
class User:
    def __init__(self,id: int, name: str, email: str):
        self._id = id
        self._name = name.strip().title()
        email = email.strip().lower()
        if "@" not in email:
            raise ValueError("Invalid email address")
        self._email = email
    def __str__(self):
        return f"User(id={self._id}, name={self._name}, email={self._email})"
    def __del__(self):
        print(f"User {self._name} deleted")
#2
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Invalid data format")
        id_str, name, email = parts
        return cls(int(id_str.strip()), name.strip(), email.strip())
u = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u)

#3
class Product:
    def __init__(self, id: int, name: str, price: float, category: str):
        self._id = id
        self._name = name
        self._price = price
        self._category = category
    def __str__(self):
        return f"Product(id={self._id}, name='{self._name}', price={self._price}, category='{self._category}')"
    def __eq__(self, other): #сравнение
        if not isinstance(other, Product):
            return False
        return self._id == other._id
    def __hash__(self):
        return hash(self._id)
    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "category": self._category
        }
#4
class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        for x in self.products:
            if x._id == product._id:
                return
        self.products.append(product)
    def remove_product(self, product_id: int):
        self.products =[x for x in self.products if x._id != product_id]
    def get_product(self, product_id: int):
        for x in self.products:
            if x._id == product_id:
                return x
        return None
    def get_all_products(self):
        return self.products
    def unique_products(self):
        return set(self.products)
    def to_dict(self):
        return {x.id: x for x in self.products}
#5
    def filter_by_price(self, min_price: float):
        return [p for p in self.products if p.price >= min_price]

#6
from datetime import datetime

class Logger:
    def log_action(user: User, action: str, product: Product, filename: str):
        timestamp = datetime.now()
        log_line = f"{timestamp};{user_id};{action};{product_id}\n"
        with open(filename, "a", encoding="utf-8") as f:
            f.write(log_line)
    def read_log(self, filename: str):
        logs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")

                if len(parts) != 4:
                    continue
                log = {
                    "timestamp": parts[0],
                    "user_id": parts[1],
                    "action": parts[2],
                    "product_id": parts[3]
                }
                logs.append(log)
        return logs

#7
class Order:
    def __init__(self,id: int, user, products=None):
        self._id = id
        self.user=user
        self.products = products if products else []
    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product_id: int):
        self.products = [x for x in self.products if x.id != product_id]
    def total_price(self):
        return sum(p.price for p in self.products)
    def __str__(self):
        return f"Order(id={self._id}, user={self.user}, products={self.products})"
#8
    def most_expensive_products(self, n: int)
        sorted_products = sorted(self.products, key=lambda p: p.price, reverse=True)
        return sorted_products[:n]
#9
    def price_stream(products):
        for p in products:
            yield p.price

