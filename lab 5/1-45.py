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
u = User(1, " john doe ", "John@Example.COM")
print(u)

