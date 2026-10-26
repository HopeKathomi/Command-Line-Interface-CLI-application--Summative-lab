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


def get_users_projects(args):
    pass


def create_project(args):
    print("New project:")
    print("Title: ", args.title)
    print("Description: ", args.description)
    print("Due_date: ", args.due_date)
    print("\nSelect a user to assign to this project:")
    user = assign_project_to_user(args)


def assign_project_to_user(args):
    with open("data/Project_data.json", "r") as file:
        data = json.load(file)

        users = data.get("Users")
        if not users:
            print("No users found. Please create a user first.")
            return
        users = list(users)
        for index, name in enumerate(users, start=1):
            print(f"{index}. {name}")

        try:
            choice = int(input("Enter the number of the user: "))

            if choice < 1 or choice > len(users):
                print("Invalid selection.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return
        choice = choice-1
        selected_user = users[choice]
        data["Users"][selected_user]["projects"].append(args.title)
        data["Projects"][args.title]=(
            {"title": args.title, "name": args.description,"due_date":args.due_date})
        with open("data/Project_data.json", "w") as file:
            json.dump(data, file, indent=4)


def create_tasks_for_projects(args):
    with open("data/Project_data.json", "r") as file:
        data = json.load(file)

    projects = data.get("Projects", [])

    if not projects:
        print("No projects found. Please create a project first.")
        return

    print("\nAvailable Projects:")

    project_list = list(projects.keys())

    for index, project_title in enumerate(project_list, start=1):
        print(f"{index}. {project_title}")

    try:
        choice = int(input("Select a project number: "))

        if choice < 1 or choice > len(project_list):
            print("Invalid selection.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    selected_project_title = project_list[choice - 1]
    selected_project = projects[selected_project_title]

    task_title = input("Enter the task title: ").strip()

    if not task_title:
        print("Task title cannot be empty.")
        return

    selected_project.setdefault("tasks", [])

    selected_project["tasks"].append(task_title)

    with open("data/Project_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print(
        f"Task '{task_title}' successfully added to "
        f"'{selected_project_title}'."
    )


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

create_project_parser = subparsers.add_parser(
    "create-project", help="Create a project")
create_project_parser.add_argument("title")
create_project_parser.add_argument("description")
create_project_parser.add_argument("due_date")
create_project_parser.set_defaults(func=create_project)

create_task_parser = subparsers.add_parser(
    "Create-task", help="Create a task(s) for a project")
create_task_parser.add_argument("title")
create_task_parser.add_argument("status")
create_task_parser.add_argument("assigned_to")
create_task_parser.set_defaults(func=create_tasks_for_projects)

args = parser.parse_args()
args.func(args)
