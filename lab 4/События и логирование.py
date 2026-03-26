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

#7
class Player:
    def __init__(self,_id,name,hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp>=0  else 0
        self.inventory = Inventory()
    def __str__(self):
        return f"Player(id={self._id},name={self._name},hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удалён")

    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        parts = [x.strip() for x in parts]
        if len(parts) != 3:
            raise ValueError

        _id = int(parts[0])
        name = parts[1]
        hp = int(parts[2])

        return cls(_id, name, hp)
    def handle_event(self,event):
        if event.type == "ATTACK":
            damage = event.data.get("damage",0)
            self._hp -= damage
        elif event.type == "HEAL":
            value = event.data.get("value",0)
            self._hp += value
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.inventory.add_item(item)
class Item:
    def __init__(self,id,name,power):
        self.id = id
        self.name = name
        self.power = power
    def __str__(self):
        return f"Item(id={self.id},name={self.name},power={self.power})"
    def __eq__(self, other):
        return isinstance(other,Item) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        for i in self.items:
            if i.id==item.id:
                return
        self.items.append(item)
    def remove_item(self,item_id):
        self.items = [i for i in self.items if i.id==item_id]
    def get_items(self):
        return self.items
    def unique_items(self):
        return set(self.items)
    def to_dict(self):
        return {item.id: item for item in self.items}
class Event:
    def __init__(self,type,data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now()
    def __str__(self):
        return f"Event(type={self.type},data={self.data},timestamp={self.timestamp})"

class Warrior(Player):
    def handle_event(self, event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            reduced_damage = int(damage * 0.9)
            self._hp -= reduced_damage
        else:
            super().handle_event(event)

class Mage(Player):
    def handle_event(self, event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                boosted_item = Item(item.id, item.name, int(item.power * 1.1))
                self.inventory.add_item(boosted_item)
        else:
            super().handle_event(event)

warrior = Warrior(3, "max", 100)
mage = Mage(4, "luna", 100)

attack_event = Event("ATTACK", {"damage": 50})
heal_event = Event("HEAL", {"value": 30})
loot_event = Event("LOOT", {"item": Item(5, "Staff", 40)})

warrior.handle_event(attack_event)
warrior.handle_event(heal_event)
warrior.handle_event(loot_event)

mage.handle_event(attack_event)
mage.handle_event(loot_event)

print(warrior)
for item in warrior.inventory.get_items():
    print(item)

print(mage)
for item in mage.inventory.get_items():
    print(item)

