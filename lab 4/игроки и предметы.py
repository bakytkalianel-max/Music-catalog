#1,2,3,4,5
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
class Player:
    def __init__(self, _id, name, hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp >= 0 else 0

    def __str__(self):
        return f"Player(id={self._id},name={self._name},hp={self._hp})"

    def __del__(self):
        print(f"Player {self._name} удалён")

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        parts = [x.strip() for x in parts]
        if len(parts) != 3:
            raise ValueError("Нужно 3 значения")

        return cls(int(parts[0]), parts[1], int(parts[2]))
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name
        self.power = power

    def __str__(self):
        return f"Item(id={self.id},name={self.name},power={self.power})"

    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.id == item.id:
                return
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [i for i in self.items if i.id != item_id]

    def get_items(self):
        return self.items

    def unique_items(self):
        return set(self.items)

    def to_dict(self):
        return {item.id: str(item) for item in self.items}

    def get_strong_items(self, min_power):
        return [item for item in self.items if item.power >= min_power]
p = None
inv = Inventory()
i = Item(1, "Sword", 50)
i2 = Item(1, "Axe", 70)

inv.add_item(Item(1, "Sword", 50))
inv.add_item(Item(2, "Shield", 30))
inv.add_item(Item(3, "Axe", 70))

@app.route('/')
def home():
    return "сервер работает"
#Player
@app.route('/create')
def create_player():
    global p
    p = Player(1, " john ", 120)
    return "Игрок создан"

@app.route('/create_from_string')
def create_from_string():
    global p
    p = Player.from_string("2, alice , 90")
    return str(p)

@app.route('/show')
def show_player():
    if p:
        return str(p)
    return "Игрок не создан"

@app.route('/delete')
def delete_player():
    global p
    if p:
        del p
        p = None
        return "Игрок удалён"
    return "Игрока нет"

#Item
@app.route('/item')
def show_item():
    return str(i)

@app.route('/item/compare')
def compare_items():
    return jsonify({"equal": i == i2})

@app.route('/item/hash')
def hash_item():
    return jsonify({"hash": hash(i)})

#Inventory
@app.route('/inventory')
def get_inventory():
    return jsonify([str(item) for item in inv.get_items()])

@app.route('/inventory/unique')
def unique_items():
    return jsonify([str(item) for item in inv.unique_items()])

@app.route('/inventory/dict')
def inventory_dict():
    return jsonify(inv.to_dict())

@app.route('/inventory/strong')
def strong_items():
    return jsonify([str(item) for item in inv.get_strong_items(50)])

@app.route('/inventory/delete/<int:item_id>')
def delete_item(item_id):
    inv.remove_item(item_id)
    return "Удалено"

if __name__ == '__main__':
    app.run(port=7000)