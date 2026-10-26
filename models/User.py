import json
from utils.data_util import load_data, save_data

class User:

    _users_list = {}
    _next_id = 1000

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

        print(f"User created: {user.name}")
        print(f"Email: {user.email}")
        data = load_data()
        data["Users"][user.name] = user.to_dict()

        with open("data/Project_data.json", "w") as file:
            json.dump(data, file, indent=4)

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