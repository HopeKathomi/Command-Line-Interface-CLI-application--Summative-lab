from templates.Project_template import Project_template
from utils.data_util import load_data, save_data
import json
from rich.console import Console


class Project(Project_template):

    _projects = {}
    console = Console()

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = None
        self.tasks = []

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": self.tasks
        }

    def assign_user(self, user):
        self.user = user
        user.add_project(self)

    @classmethod
    def create_project(cls, args=None):
        title, description, due_date = cls.get_project_details(args)
        project = cls(title, description, due_date)
        cls._projects[title] = project.to_dict()
        return project

    @staticmethod
    def list_projects(args=None):
        Project.console.print("List of all projects:", style="green")

        data = load_data()
        project_data = data["Projects"]
        if not project_data:
            Project.console.print("No projects found.", style="red")
            return

        for index, title in enumerate(project_data, start=1):
            Project.console.print(f"{index}. [bold]{title}[/bold]" ,style="blue")
            # Project.console.print(f"Description: {details['description']}")
            # Project.console.print(f"Due date: {details['due_date']}")

    @staticmethod
    def delete_project(args):
        data = load_data()
        projects = data.get("Projects")

        for index, value in enumerate(projects, start=1):
            print(f"{index}. {value}")

        if args.title in projects:
            del projects[args.title]
            with open("data/Project_data.json", "w") as file:
                json.dump(data, file, indent=4)

            print(f"Project '{args.title}' deleted successfully.")
        else:
            print(f"Project '{args.title}' not found.")

    @staticmethod
    def get_project_details(args):
        #     parser = argparse.ArgumentParser()
        #     parser.add_argument("project", nargs="?")
        #     args = parser.parse_args()

        #     if args.project:
        #         return args.project
        #     else:
        #         title = input("Enter project name: ")
        #         description = input("Enter project description: ")
        #         due_date = input("Enter due date: ")
        #         return title, description, due_date
        print("New project:")
        print("Title: ", args.title)
        print("Description: ", args.description)
        print("Due_date: ", args.due_date)

        title = args.title
        description = args.description
        due_date = args.due_date
        return title, description, due_date

    def __repr__(self):
        return f"Project({self.title!r}, {self.description!r}, {self.due_date!r})"
