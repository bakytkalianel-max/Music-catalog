#1
class User:
    def __init__(self,id: int, name: str, email: str):
        self._id = id
        self._name = name.strip().title()
        email = email.strip().lower()
        if "@" not in email:
            raise ValueError("Invalid email address")
        self._email = email
    def __str__(self):
        return f"User(id={self._id}, name={self._name}, email={self._email})"
    def __del__(self):
        print(f"User {self._name} deleted")
#2
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        if len(parts) != 3:
            raise ValueError("Invalid data format")
        id_str, name, email = parts
        return cls(int(id_str.strip()), name.strip(), email.strip())
u = User.from_string("2, Alice Wonderland , alice@wonder.com")
print(u)