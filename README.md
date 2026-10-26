# Python Project Management System

## 1. Project Overview

The **Python Project Management System** is a Python application designed to organise and manage users, projects, and tasks. It uses Object-Oriented Programming (OOP) to represent users, projects, and tasks as objects.

The application allows users to be created, projects to be managed, and tasks to be tracked. It also supports converting objects into dictionaries using Python's `to_dict()` methods, making the data easier to store in JSON format.

## 2. Features

- **User Management:** Create users with a name and email address.
- **Project Management:** Create projects with a title, description, and due date.
- **Task Management:** Create tasks with a title, status, and assigned person.
- **Project Assignment:** Associate projects with users.
- **Duplicate Prevention:** Prevent adding the same project more than once to a user's project list.
- **Data Serialization:** Convert user, project, and task objects into dictionaries using `to_dict()`.
- **Object Representation:** Use `__repr__()` methods to provide readable representations of objects.
- **Class-Level Storage:** Use class attributes to maintain collections of users, projects, and tasks in memory.

## 3. Technologies Used

- **Python 3** – Main programming language.
- **JSON** – Imported for working with JSON data.
- **argparse** – Imported in the task module for potential command-line argument handling.
- **Object-Oriented Programming (OOP)** – Used to structure the application into classes.

No third-party Python packages are required by the code shown.

## 4. Project Structure

The project can be organised as follows:

```text
project-management-system/
│
├── models/
│   ├── User.py
│   ├── Project.py
│   └── Task.py
│
├── templates/
│   └── Project_template.py
│
├── data/
│   └── Project_data.json
│
├── main.py
└── README.md
```

*Note: Adjust the filenames and folders to match your actual project structure.*

## 5. Classes and Their Responsibilities

### 5.1 User Class

The `User` class represents an individual user in the system.

**Attributes:**
- `name`: The user's name.
- `email`: The user's email address.
- `projects`: A list of projects associated with the user.
- `_users_list`: A class-level dictionary for storing users.
- `_next_id`: A class-level counter reserved for potential user ID generation.

**Methods:**
- `add_projects(project)`: Adds a project to the user's list if it is not already present.
- `add_user_to_list(object)`: Adds a user object to the class-level dictionary if the user's name is not already a key.
- `to_dict()`: Converts the user object into a dictionary.
- `create_user(name, email)`: Creates and registers a user object.
- `__repr__()`: Returns a readable representation of the user.

### 5.2 Project Class

The `Project` class represents a project and inherits from `Project_template`.

**Attributes:**
- `title`: The project's name.
- `description`: A description of the project.
- `due_date`: The project's deadline.
- `user`: The user assigned to the project, initially `None`.
- `tasks`: A list of tasks associated with the project.
- `_projects`: A class-level dictionary for storing project objects.

**Methods:**
- `to_dict()`: Converts the project object into a dictionary.
- `assign_user(user)`: Assigns a user to the project and attempts to add the project to that user's project list.
- `create_project()`: Retrieves project details through `get_project_details()`, creates a project, and stores it in the class-level dictionary.
- `__repr__()`: Returns a readable representation of the project.

**Dependency:** The class requires `Project_template` from `templates/Project_template.py`. The template must provide a compatible `get_project_details()` method for `create_project()` to work.

### 5.3 Task Class

The `Task` class represents an individual task within the project management system.

**Attributes:**
- `title`: The task's name.
- `status`: The current status of the task, such as `Pending` or `Completed`.
- `assigned_to`: The person responsible for the task.
- `_tasks`: A class-level dictionary for storing task objects.

**Methods:**
- `to_dict()`: Converts the task object into a dictionary.
- `create_task()`: Retrieves task details through `get_task_details()`, creates a task, and stores it in the class-level dictionary.
- `__repr__()`: Returns a readable representation of the task.

**Note:** The current `Task` class does not define `get_task_details()`. This method must be implemented before `create_task()` can work.

## 6. Installation and Setup

### Prerequisites

Ensure that Python 3 is installed on your computer.

Check your Python version by running:

```bash
python --version
```

### Clone the Repository

If the project is hosted on GitHub, clone it using:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd project-management-system
```

### Run the Application

If `main.py` contains the application's entry point, run:

```bash
python main.py
```

The actual commands available will depend on how the application is implemented in `main.py`.

## 7. Data Storage

The classes include `to_dict()` methods that convert Python objects into dictionaries. These dictionaries can be serialised into JSON using Python's `json` module.

For example:

```python
import json

user = User.create_user("Hope", "hope@example.com")

user_data = user.to_dict()

print(json.dumps(user_data, indent=4))
```

Example output:

```json
{
    "name": "Hope",
    "email": "hope@example.com",
    "projects": []
}
```

**Important:** The `