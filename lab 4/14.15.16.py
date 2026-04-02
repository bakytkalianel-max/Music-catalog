#14,15,16
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
        return f"Event(type={self.type}, data={self.data}, timestamp={self.timestamp})"
class Item:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def __str__(self):
        return f"{self.name}({self.power})"
class Player:
    def __init__(self, player_id, name, hp):
        self.player_id = player_id
        self.name = name
        self._hp = hp
        self._inventory = []
    @property
    def hp(self):
        return self._hp
    @property
    def inventory(self):
        return self._inventory
    def add_item(self, item):
        self._inventory.append(item)
    def heal(self, value):
        self._hp += value
    def take_damage(self, value):
        self._hp -= value
        if self._hp < 0:
            self._hp = 0
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.take_damage(damage)
        elif event.type == "HEAL":
            value = event.data.get("heal", 0)
            self.heal(value)
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.add_item(item)
    def __str__(self):
        items = [str(i) for i in self._inventory]
        return f"Player(id={self.player_id}, name={self.name}, hp={self._hp}, inventory={items})"

class Warrior(Player):
    def take_damage(self, value):
        reduced_damage = value * 0.9
        self._hp -= reduced_damage
        if self._hp < 0:
            self._hp = 0

class Mage(Player):
    def add_item(self, item):
        boosted_item = Item(item.name, item.power * 1.1)
        self._inventory.append(boosted_item)
#14
decide_action = lambda player: (
    "HEAL" if player.hp < 30
    else "LOOT" if len(player.inventory) == 0
    else "ATTACK"
)
p = Player(1, "Hero", 100)
w = Warrior(2, "Warrior", 100)
m = Mage(3, "Mage", 100)

@app.route('/')
def home():
    return "сервер работает"
@app.route('/players')
def show_players():
    return jsonify({
        "Player": str(p),
        "Warrior": str(w),
        "Mage": str(m)
    })
@app.route('/action')
def action():
    return jsonify({
        "Player": decide_action(p),
        "Warrior": decide_action(w),
        "Mage": decide_action(m)
    })
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
    p.handle_event(Event("LOOT", {"item": Item("Sword", 50)}))
    w.handle_event(Event("LOOT", {"item": Item("Sword", 50)}))
    m.handle_event(Event("LOOT", {"item": Item("Sword", 50)}))
    return jsonify({
        "Player": str(p),
        "Warrior": str(w),
        "Mage": str(m)
    })

if __name__ == '__main__':
    app.run(port=9500)