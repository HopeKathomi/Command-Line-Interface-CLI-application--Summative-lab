class Project_template:

    _projects = {}

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = None
        self.tasks = []

    def to_dict(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "due_date" : self.due_date,
            "tasks" :self.tasks
        }

    @classmethod
    def create_project(cls):
       pass

    @staticmethod
    def get_project_details():
        pass