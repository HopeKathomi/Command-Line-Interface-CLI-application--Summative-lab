import json
from utils.data_util import load_data, save_data
from rich.console import Console

class User:

    _users_list = {}
    _next_id = 1000
    console = Console()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self._user_id
        self.projects = []
    
    def add_projects(self, project):
        if project not in self.projects:
            self.projects.append(project)

    def add_user_to_list(self, object):
        if self.name not in User._users_list:
            User._users_list[self.name] = object

    def to_dict(self):
        return {
            "name" : self.name,
            "email" : self.email,
            "projects": self.projects
        }

    @classmethod
    def create_user(cls, name, email):
        obj = cls(name, email)
        obj.add_user_to_list(obj)
        return obj

    def add_user(args):
        user = User.create_user(args.name, args.email)
        user.add_user_to_list(user)

        User.console.print(f"[bold]User created[/bold]: {user.name}", style="blue")
        User.console.print(f"[bold]Email[/bold]: {user.email}", style="blue")
        data = load_data()
        data["Users"][user.name] = user.to_dict()

        save_data(data)

    def list_users(args):
        data = load_data()

        User.console.print("List of users:", style="purple")
        for user_name in data.get("Users", {}).keys():
            User.console.print(user_name, style="blue")


    # @staticmethod
    # def generate_id():
    #     User._next_id +=1
    #     id =f"USER{User._next_id}"
    #     return id

    # @staticmethod
    # def get_name():
    #     while True:
    #         parser = argparse.ArgumentParser()
    #         parser.add_argument("name", nargs="?")
    #         args = parser.parse_args()
    #         if args.name:
    #             return args.name
    #         else:
    #             return input("👤 Enter User's name: ")

    
    def __repr__(self):
        return f"User({self.name!r}, {self.email!r})"