#12,13
from flask import Flask, jsonify
from flasgger import Swagger
from datetime import datetime
import random

app = Flask(__name__)
swagger = Swagger(app)

class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Event(type={self.type}, data={self.data})"

    def to_dict(self):
        return {
            "type": self.type,
            "data": self.data
        }

class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name
        self.power = power
#12
def generate_events(players, items, n):
    events = []

    choose_type = lambda: random.choice(["ATTACK", "HEAL", "LOOT"])

    for player in players:
        for _ in range(n):
            t = choose_type()

            if t == "ATTACK":
                e = Event("ATTACK", {
                    "player_id": player.player_id,
                    "damage": random.randint(10, 50)
                })

            elif t == "HEAL":
                e = Event("HEAL", {
                    "player_id": player.player_id,
                    "heal": random.randint(5, 30)
                })

            else:
                item = random.choice(items)
                e = Event("LOOT", {
                    "player_id": player.player_id,
                    "item": item.name
                })
            events.append(e)
    return events
#13
def analyze_logs(events):
    total_damage = sum(
        e.data.get("damage", 0)
        for e in events if e.type == "ATTACK"
    )
    damage_by_player = {}
    for e in events:
        if e.type == "ATTACK":
            pid = e.data.get("player_id")
            damage_by_player[pid] = damage_by_player.get(pid, 0) + e.data.get("damage", 0)

    top_player = max(damage_by_player, key=damage_by_player.get) if damage_by_player else None

    event_count = {}
    for e in events:
        event_count[e.type] = event_count.get(e.type, 0) + 1

    most_common_event = max(event_count, key=event_count.get) if event_count else None
    return {
        "total_damage": total_damage,
        "top_player": top_player,
        "most_common_event": most_common_event
    }

players = [
    Player(1, "Hero"),
    Player(2, "Warrior"),
    Player(3, "Mage")
]

items = [
    Item(1, "Sword", 50),
    Item(2, "Shield", 30),
    Item(3, "Axe", 70)
]

events_data = []

@app.route('/')
def home():
    return "сервер работает"

@app.route('/events/generate')
def create_events():
    global events_data
    events_data = generate_events(players, items, 3)
    return jsonify([e.to_dict() for e in events_data])

@app.route('/events/analyze')
def analyze():
    if not events_data:
        return jsonify({"error": "сначала сгенерируй события"})
    return jsonify(analyze_logs(events_data))

if __name__ == '__main__':
    app.run(port=9400)