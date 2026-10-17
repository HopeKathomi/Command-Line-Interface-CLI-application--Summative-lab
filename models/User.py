import argparse

class User:

    _users_list = {}
    _next_id = 1000
    welcome_message = "\n✨ Welcome to the most powerful project management tool. ✨\n"

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self._user_id
        self.projects = []

    @classmethod
    def create_user(cls):
        name = cls.get_name()
        email = f"{name}@email.com"
        obj = cls(name, email)
        obj.add_user_to_list()
        return obj

    def add_user_to_list(self):
       User._users_list[self.name] = self.email

    # @staticmethod
    # def generate_id():
    #     User._next_id +=1
    #     id =f"USER{User._next_id}"
    #     return id

    @staticmethod
    def get_name():
        parser = argparse.ArgumentParser()
        parser.add_argument("name", nargs = "?")
        args = parser.parse_args()
        if args.name:
            return args.name
        else:
            return input("👤 Enter User's name: ")

    def __repr__(self):
        return f"User({self.name!r}, {self.email!r})"
