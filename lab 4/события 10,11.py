#10,11
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
        return f"Event(type={self.type},data={self.data})"

class EventIterator:
    def __init__(self, events):
        self.events = events
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.events):
            raise StopIteration
        event = self.events[self.index]
        self.index += 1
        return event

def damage_stream(events):
    for event in events:
        if event.type == "ATTACK":
            yield event.data.get("damage", 0)

events = [
    Event("ATTACK", {"damage": 20}),
    Event("HEAL", {"heal": 10}),
    Event("ATTACK", {"damage": 35}),
    Event("LOOT", {"item": "Sword"})
]

@app.route('/')
def home():
    return "сервер работает"
#10
@app.route('/events/iterate')
def iterate_events():
    iterator = EventIterator(events)
    result = [str(e) for e in iterator]
    return jsonify(result)
#11
@app.route('/events/damage')
def get_damage():
    damages = list(damage_stream(events))
    return jsonify(damages)

if __name__ == '__main__':
    app.run(port=9200)
    