import json
from pathlib import Path
from models.Project import Project
from models.User import User
from models.Task import Task

print(f"{User.welcome_message}")

hope = User.create_user()

print(User._users_list)

Road = Project.create_project()
# # print(Road.title)

# hope.add_projects(Road)
# print("HI")
# print(hope.projects)

# print(hope)

filename = "Project_data.json"
def save_data():
    
    data = {
        "Users": {
            # user_name: user.to_dict()
            # for user_name, user in User._users_list.items()
        },
        "Projects": {
            # project_title: project.to_dict()
            # for project_title, project in Project._projects.items()
        }
    }
    with open(f"data/{filename}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# save_data()
# def load_data():
#     stored_data = Path("data/Project_data.json")

#     if not stored_data.exists():
#         return

#     with open(stored_data, "r", encoding="utf-8") as file:
#         data = json.load(file)
#         print(data)
#         for user_data in data.get("Users", {}).values():
#             user = User(user_data["name"],user_data["email"])
#             user.projects = user_data.get("projects", [])
#             User._users_list[user.name] = user

with open("data/Project_data.json", "r") as file:
    data = json.load(file)
    # print(data)

    for user_name, user in User._users_list.items():
        data["Users"][user_name] = user.to_dict()
    # print(data)

    for project_title, project in Project._projects.items():
        data["Projects"][project_title] = project.to_dict()

with open("data/Project_data.json", "w") as file:
    json.dump(data, file, indent =4)
# load_data()


