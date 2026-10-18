from models.Project import Project
from models.User import User
from models.Task import Task

print(f"{User.welcome_message}")

# print(User.create_user())
# print(User._users_list)

Road = Project.create_project()
print(Road.title)
