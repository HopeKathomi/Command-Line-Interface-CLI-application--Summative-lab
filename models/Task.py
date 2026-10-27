import argparse
from utils.data_util import load_data, save_data
from rich.console import Console

class Task:
    _tasks ={}
    console = Console()

    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project = None

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
        }

    @classmethod
    def create_task(cls):
        title, status, assigned_to = cls.get_task_details()
        task = cls(title, status, assigned_to)
        cls._tasks[title] = task
        return task

    def create_tasks_for_projects(args):
        data = load_data()

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
                Task.console.print("Invalid selection.", style="red")
                return

        except ValueError:
            Task.console.print("Please enter a valid number.", style="red")
            return

        selected_project_title = project_list[choice - 1]
        selected_project = projects[selected_project_title]

        task_title = input("Enter the task title: ").strip()
        task_status = input("Enter task status: ").strip()
        Task.console.print("Assign to: ", style="purple")

        users = data.get("Users",{})

        users_list = list(users.keys())
        for index, user in enumerate(users_list, start=1):
            Task.console.print(f"{index}. {user}", style="blue")

        try:
            assignee_index = int(input("Select person responsible: "))

            if assignee_index < 1 or assignee_index > len(users_list):
                Task.console.print("Invalid selection.", style="red")
                return

        except ValueError:
            Task.console.print("Please enter a valid number.", style="red")
            return

        assignee = users_list[assignee_index - 1]

        selected_project["tasks"].append(task_title)

        data["Tasks"][task_title]={
            "title": task_title,
            "status": task_status,
            "assigned_to": assignee
        }

        save_data(data)

        print(
            f"Task '{task_title}' successfully added to "
            f"'{selected_project_title}'."
        )
    # @staticmethod
    # def get_task_details():
    #     while True:
    #         parser = argparse.ArgumentParser()
    #         parser.add_argument("project", nargs="?")
    #         args = parser.parse_args()

    #         if args.project:
    #             return args.project
    #         else:
    #             title = input("Enter task title: ")
    #             status = input("Enter task status: ")
    #             asigned_to = input("Enter person responsible: ")
    #             return title, status, asigned_to

    def __repr__(self):
            return f"Task({self.title!r}, {self.status!r}, {self.assigned_to!r})"