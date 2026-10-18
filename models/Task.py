import argparse
class Task:
    _tasks ={}
    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

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

    @staticmethod
    def get_task_details():
        while True:
            parser = argparse.ArgumentParser()
            parser.add_argument("project", nargs="?")
            args = parser.parse_args()

            if args.project:
                return args.project
            else:
                title = input("Enter task title: ")
                status = input("Enter task status: ")
                asigned_to = input("Enter person responsible: ")
                return title, status, asigned_to

    def __repr__(self):
            return f"Task({self.title!r}, {self.status!r}, {self.assigned_to!r})"