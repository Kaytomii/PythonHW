

class LoginMixin:
    def log(self, message):
        print(f"[LOG], {message}")


class User(LoginMixin):
    def __init__(self, name):
        self.name = name

    def login(self):
        self.log(f"User {self.name} log in")
        print(f"{self.name} увійшов у систему")

user = User("Alex")
user.login()