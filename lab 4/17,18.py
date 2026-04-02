#17,18
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def __str__(self):
        return f"{self.name}({self.power})"
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def __iter__(self):  # итератор
        return iter(self.items)
    def strong_items(self, min_power):
        return [item for item in self.items if item.power >= min_power]

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
    def __del__(self):
        print(f"Player {self.name} удалён")
    def __str__(self):
        items = [str(i) for i in self.inventory]
        return f"{self.name}: {items}"
p = Player("Hero")
p.inventory.add_item(Item("Sword", 50))
p.inventory.add_item(Item("Shield", 30))
p.inventory.add_item(Item("Axe", 70))

@app.route('/')
def home():
    return "сервер работает"

@app.route('/inventory')
def show_inventory():
    return jsonify([str(item) for item in p.inventory])

@app.route('/inventory/strong')
def strong_items():
    strong = p.inventory.strong_items(50)
    return jsonify([str(item) for item in strong])

@app.route('/player/delete')
def delete_player():
    global p
    del p
    p = None
    return "Игрок удалён"

if __name__ == '__main__':
    app.run(port=9600)