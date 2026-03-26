#6
from datetime import datetime

class Event:
    def __init__(self,type,data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type},data={self.data},timestamp={self.timestamp})"
e = Event("ATTACK", {"damage": 20})
print(e)