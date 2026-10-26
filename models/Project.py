from templates.Project_template import Project_template
import json


class Project(Project_template):

    _projects = {}

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
    def create_project(cls):
        title, description, due_date = cls.get_project_details()
        project = cls(title, description, due_date)
        cls._projects[title] = project
        return project

    

    def list_projects(args):
        print("Here are your projects:")
        print(Project._projects)

    def delete_project(args):
        with open("data/Project_data.json", "r") as file:
            data = json.load(file)
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

    # @staticmethod
    # def get_project_details():
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

    def __repr__(self):
        return f"Project({self.title!r}, {self.description!r}, {self.due_date!r})"
