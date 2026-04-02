#6,7
from flask import Flask, jsonify
from flasgger import Swagger
from datetime import datetime

app = Flask(__name__)
swagger = Swagger(app)

class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type},data={self.data},timestamp={self.timestamp})"
    def to_dict(self):
        return {
            "type": self.type,
            "data": self.data,
            "timestamp": str(self.timestamp)
        }

class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name}({self.power})"

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []

    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.hp -= damage

        elif event.type == "HEAL":
            heal = event.data.get("heal", 0)
            self.hp += heal

        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.inventory.append(item)

    def __str__(self):
        items = [str(i) for i in self.inventory]
        return f"{self.name}: hp={self.hp}, items={items}"

class Warrior(Player):
    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            damage *= 0.9
            self.hp -= damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event: Event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power *= 1.1
                self.inventory.append(item)
        else:
            super().handle_event(event)

e = None
p = Player("Hero", 100)
w = Warrior("Warrior", 100)
m = Mage("Mage", 100)

@app.route('/')
def home():
    return "сервер работает"
@app.route('/event/create')
def create_event():
    global e
    e = Event("ATTACK", {"damage": 20})
    return "Событие создано"
@app.route('/event/show')
def show_event():
    if e:
        return str(e)
    return "Событие не создано"
@app.route('/event/json')
def show_event_json():
    if e:
        return jsonify(e.to_dict())
    return jsonify({"error": "Событие не создано"})

@app.route('/event/attack')
def attack():
    event = Event("ATTACK", {"damage": 20})
    p.handle_event(event)
    w.handle_event(event)
    m.handle_event(event)
    return jsonify({
        "Player": str(p),
        "Warrior": str(w),
        "Mage": str(m)
    })

@app.route('/event/heal')
def heal():
    event = Event("HEAL", {"heal": 15})
    p.handle_event(event)
    w.handle_event(event)
    m.handle_event(event)
    return jsonify({
        "Player": str(p),
        "Warrior": str(w),
        "Mage": str(m)
    })

@app.route('/event/loot')
def loot():
    item1 = Item("Sword", 50)
    item2 = Item("Sword", 50)
    item3 = Item("Sword", 50)
    p.handle_event(Event("LOOT", {"item": item1}))
    w.handle_event(Event("LOOT", {"item": item2}))
    m.handle_event(Event("LOOT", {"item": item3}))
    return jsonify({
        "Player": str(p),
        "Warrior": str(w),
        "Mage": str(m)
    })

if __name__ == '__main__':
    app.run(port=9000)