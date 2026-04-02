from flask import Flask, jsonify
from flasgger import Swagger
from datetime import datetime
import random
import json

app = Flask(__name__)
swagger = Swagger(app)

class Event:
    def __init__(self, type, data, timestamp=None):
        self.type = type
        self.data = data
        self.timestamp = timestamp if timestamp else datetime.now()
    def __str__(self):
        return f"Event(type={self.type}, data={self.data}, timestamp={self.timestamp})"
    def to_dict(self):
        return {
            "type": self.type,
            "data": self.data,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
class Item:
    def __init__(self, item_id, name, power):
        self.id = item_id
        self.name = name
        self.power = power
    def __str__(self):
        return f"Item(id={self.id}, name={self.name}, power={self.power})"
    def __eq__(self, other):
        return isinstance(other, Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "power": self.power
        }
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
        return self.items
    def __iter__(self):
        return iter(self.items)
    def strong_items(self, min_power):
        return [item for item in self.items if item.power >= min_power]
    def __len__(self):
        return len(self.items)

class Player:
    def __init__(self, player_id, name, hp):
        self.player_id = player_id
        self.name = name
        self._hp = hp
        self._inventory = Inventory()
        self.total_damage_taken = 0
    @property
    def hp(self):
        return self._hp
    @property
    def inventory(self):
        return self._inventory
    def add_item(self, item):
        self._inventory.add_item(item)
    def heal(self, value):
        self._hp += value
    def take_damage(self, value):
        self._hp -= value
        self.total_damage_taken += value
        if self._hp < 0:
            self._hp = 0
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.take_damage(damage)
        elif event.type == "HEAL":
            heal_value = event.data.get("heal", 0)
            self.heal(heal_value)
        elif event.type == "LOOT":
            item_data = event.data.get("item")
            if item_data:
                self.add_item(item_data)
    def __str__(self):
        items = [str(i) for i in self._inventory]
        return f"Player(id={self.player_id}, name={self.name}, hp={self._hp}, inventory={items})"
    def __del__(self):
        print(f"Player {self.name} удалён")
    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "hp": self.hp,
            "inventory": [item.to_dict() for item in self.inventory],
            "total_damage_taken": self.total_damage_taken
        }
class Warrior(Player):
    def take_damage(self, value):
        reduced_damage = value * 0.9
        self._hp -= reduced_damage
        self.total_damage_taken += reduced_damage
        if self._hp < 0:
            self._hp = 0

class Mage(Player):
    def add_item(self, item):
        boosted_item = Item(item.id, item.name, item.power * 1.1)
        self._inventory.add_item(boosted_item)

class Logger:
    @staticmethod
    def log(event, player, filename):
        line = {
            "timestamp": event.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "player_id": player.player_id,
            "event_type": event.type,
            "data": event.data if not isinstance(event.data.get("item"), Item) else {
                **event.data,
                "item": event.data["item"].to_dict()
            }
        }
        with open(filename, "a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    @staticmethod
    def read_logs(filename):
        events = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line.strip())
                    data = obj["data"]
                    if "item" in data and isinstance(data["item"], dict):
                        item_info = data["item"]
                        data["item"] = Item(
                            item_info["id"],
                            item_info["name"],
                            item_info["power"]
                        )
                    timestamp = datetime.strptime(obj["timestamp"], "%Y-%m-%d %H:%M:%S")
                    event = Event(obj["event_type"], data, timestamp)
                    events.append(event)
        except FileNotFoundError:
            pass
        return events

def generate_events(players, items, n):
    events = []
    choose_type = lambda: random.choice(["ATTACK", "HEAL", "LOOT"])
    for player in players:
        for _ in range(n):
            event_type = choose_type()
            if event_type == "ATTACK":
                event = Event("ATTACK", {
                    "player_id": player.player_id,
                    "damage": random.randint(10, 40)
                })
            elif event_type == "HEAL":
                event = Event("HEAL", {
                    "player_id": player.player_id,
                    "heal": random.randint(5, 25)
                })
            else:
                item = random.choice(items)
                event = Event("LOOT", {
                    "player_id": player.player_id,
                    "item": Item(item.id, item.name, item.power)
                })
            events.append(event)
    return events

def analyze_logs(events):
    total_damage = sum(
        e.data.get("damage", 0)
        for e in events if e.type == "ATTACK"
    )
    damage_by_player = {}
    event_count = {}
    for e in events:
        event_count[e.type] = event_count.get(e.type, 0) + 1
        if e.type == "ATTACK":
            pid = e.data.get("player_id")
            damage_by_player[pid] = damage_by_player.get(pid, 0) + e.data.get("damage", 0)

    top_player = max(damage_by_player, key=damage_by_player.get) if damage_by_player else None
    most_common_event = max(event_count, key=event_count.get) if event_count else None
    return {
        "total_damage": total_damage,
        "top_player": top_player,
        "most_common_event": most_common_event
    }
#19
def analyze_inventory(inventories):
    unique_items = set()
    for inventory in inventories:
        for item in inventory:
            unique_items.add(item)
    top_power = None
    for item in unique_items:
        if top_power is None or item.power > top_power.power:
            top_power = item
    return {
        "unique_items": {str(item) for item in unique_items},
        "top_power": str(top_power) if top_power else None
    }
#20
def main():
    filename = "final_logs.txt"

    open(filename, "w", encoding="utf-8").close()

    items = [
        Item(1, "Sword", 50),
        Item(2, "Shield", 30),
        Item(3, "Axe", 70),
        Item(4, "Staff", 60)
    ]
    players = [
        Player(1, "Hero", 100),
        Warrior(2, "Warrior", 120),
        Mage(3, "Mage", 90)
    ]
    events = generate_events(players, items, 4)
    player_map = {player.player_id: player for player in players}
    for event in events:
        pid = event.data.get("player_id")
        player = player_map.get(pid)
        if player:
            player.handle_event(event)
            Logger.log(event, player, filename)

    loaded_events = Logger.read_logs(filename)
    damage_leader = max(players, key=lambda p: p.total_damage_taken)
    loot_leader = max(players, key=lambda p: len(p.inventory))

    inventory_stats = analyze_inventory([player.inventory for player in players])
    event_stats = analyze_logs(loaded_events)
    return {
        "players": [player.to_dict() for player in players],
        "events_generated": [event.to_dict() for event in events],
        "events_loaded_from_file": [event.to_dict() for event in loaded_events],
        "top_damage_player": damage_leader.name,
        "top_loot_player": loot_leader.name,
        "event_stats": event_stats,
        "inventory_stats": {
            "unique_items": list(inventory_stats["unique_items"]),
            "top_power": inventory_stats["top_power"]
        }
    }

@app.route('/')
def home():
    return "сервер работает"

@app.route('/inventory/analyze')
def inventory_analyze():
    inv1 = Inventory()
    inv2 = Inventory()

    inv1.add_item(Item(1, "Sword", 50))
    inv1.add_item(Item(2, "Shield", 30))
    inv2.add_item(Item(3, "Axe", 70))
    inv2.add_item(Item(1, "Sword", 50))
    result = analyze_inventory([inv1, inv2])
    return jsonify({
        "unique_items": list(result["unique_items"]),
        "top_power": result["top_power"]
    })

@app.route('/simulate')
def simulate():
    return jsonify(main())

if __name__ == '__main__':
    app.run(port=9700)