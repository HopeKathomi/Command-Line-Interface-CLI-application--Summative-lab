import json
from models.Project import Project
from models.User import User
from models.Task import Task

print(f"{User.welcome_message}")

hope = User.create_user()
print(User._users_list)

# Road = Project.create_project()
# # print(Road.title)

# hope.add_projects(Road)
# print("HI")
# print(hope.projects)

# print(hope)

def save_data():
    filename = "Project_data.json"
    data = {
        "Users": {
            user_name : user.to_dict()
            for user_name, user in User._users_list.items()
        },
    }
    with open(f"data/{filename}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
save_data()