import json
from models.Project import Project
from models.User import User
from models.Task import Task

print(f"{User.welcome_message}")

User_obj = User.create_user()
proj_obj = Project.create_project()
task_obj = Task.create_task()

print(proj_obj)
User_obj.add_projects(proj_obj.title)

print("Hi")
print(type(User_obj.projects))

# hope.add_projects(Road)
# print("HI")
# print(hope.projects)

# print(hope)

with open("data/Project_data.json", "r") as file:
    data = json.load(file)

    for user_name, user in User._users_list.items():
        data["Users"][user_name] = user.to_dict()

    for project_title, project in Project._projects.items():
        data["Projects"][project_title] = project.to_dict()

    for title, task in Task._tasks.items():
        data["Tasks"][title] = task.to_dict()

with open("data/Project_data.json", "w") as file:
    json.dump(data, file, indent=4)
