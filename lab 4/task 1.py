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

