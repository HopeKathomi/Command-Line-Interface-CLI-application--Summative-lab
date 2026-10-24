import json
import argparse
from models.Project import Project
from models.User import User
from models.Task import Task


def add_user(args):
    user = User.create_user(args.name, args.email)
    user.add_user_to_list(user)

    print(f"User created: {user.name}")
    print(f"Email: {user.email}")

    with open("data/Project_data.json", "r") as file:
        data = json.load(file)
        data["Users"][user.name] = user.to_dict()

    with open("data/Project_data.json", "w") as file:
        json.dump(data, file, indent=4)



def list_users(args):
    print("List of users:")
    with open("data/Project_data.json", "r") as file:
        data = json.load(file)

        for user_name in data.get("Users", {}).keys():
            print(user_name)

    # with open("data/Project_data.json", "w") as file:
    #     json.dump(data, file, indent=4)

def add_project_to_user(args):
    pass

def list_projects(args):
    print("Here are your projects:")

    print(Project._projects)


parser = argparse.ArgumentParser(description="My CLI project manager")
subparsers = parser.add_subparsers(dest="command", required=True)

add_user_parser = subparsers.add_parser("add-user", help="Create user")
add_user_parser.add_argument("name")
add_user_parser.add_argument("email")
add_user_parser.set_defaults(func=add_user)

list_users_parser = subparsers.add_parser("list-users", help="List all users")
list_users_parser.set_defaults(func=list_users)

list_projects_parser = subparsers.add_parser(
    "list-projects", help="Lis all projects")
list_projects_parser.set_defaults(func=list_projects)


args = parser.parse_args()
args.func(args)

# with open("data/Project_data.json", "r") as file:
#     data = json.load(file)

#     for user_name, user in User._users_list.items():
#         data["Users"][user_name] = user.to_dict()

#     # for project_title, project in Project._projects.items():
#     #     data["Projects"][project_title] = project.to_dict()

#     # for title, task in Task._tasks.items():
#     #     data["Tasks"][title] = task.to_dict()

# with open("data/Project_data.json", "w") as file:
#     json.dump(data, file, indent=4)
