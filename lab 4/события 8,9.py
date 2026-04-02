#8,9
from flask import Flask, jsonify
from flasgger import Swagger
from datetime import datetime

app = Flask(__name__)
swagger = Swagger(app)

class Event:
    def __init__(self, type, data, timestamp=None):
        self.type = type
        self.data = data
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"Event(type={self.type},data={self.data},timestamp={self.timestamp})"

class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name

class Logger:
    @staticmethod
    def log(event: Event, player: Player, filename: str):
        with open(filename, "a", encoding="utf-8") as f:
            line = f"{event.timestamp};{player.player_id};{event.type};{event.data}\n"
            f.write(line)
    @staticmethod
    def read_logs(filename: str):
        events = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(";")
                    if len(parts) != 4:
                        continue
                    timestamp = datetime.fromisoformat(parts[0])
                    player_id = int(parts[1])
                    event_type = parts[2]
                    data = eval(parts[3])  # преобразуем строку в dict

                    event = Event(event_type, data, timestamp)
                    events.append(event)
        except FileNotFoundError:
            pass
        return events

player = Player(1, "Hero")
filename = "logs.txt"

@app.route('/')
def home():
    return "Logger работает"

@app.route('/log')
def log_event():
    event = Event("ATTACK", {"damage": 25})
    Logger.log(event, player, filename)
    return "Событие записано"

@app.route('/logs')
def get_logs():
    events = Logger.read_logs(filename)
    return jsonify([str(e) for e in events])

if __name__ == '__main__':
    app.run(port=9100)