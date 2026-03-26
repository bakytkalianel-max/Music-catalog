#1
class Player:
    def __init__(self,_id,name,hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp>=0  else 0
    def __str__(self):
        return f"Player(id={self._id},name={self._name},hp={self._hp})"
    def __del__(self):
        print(f"Player {self._name} удалён")

p = Player(1, " john ", 120)
print(p)

#2
class Player:
    def __init__(self,_id,name,hp):
        self._id = _id
        self._name = name.strip().title()
        self._hp = hp if hp>=0  else 0
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

p = Player.from_string("2, alice , 90")
print(p)

#3
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
i = Item(1, " Sword ", 50)
print(i)

#4
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
inv = Inventory()

i1 = Item(1, "Sword", 50)
i2 = Item(2, "Shield", 30)
i3 = Item(1, "Sword", 50)

inv.add_item(i1)
inv.add_item(i2)
inv.add_item(i3)
print(len(inv.get_items()))

#5
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
    def get_strong_items(self,min_power):
        return list(filter(lambda item: item.power>=min_power, self.items))

inv = Inventory()

inv.add_item(Item(id=1, name = "Sword",power = 50))
inv.add_item(Item(id=2, name="Shield", power=30))
inv.add_item(Item(id=3, name="Axe",power= 70))

print(inv.get_strong_items(50))