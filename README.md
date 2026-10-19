# CLI Project Management App

A command-line project management application built with Python. The application allows users to create user profiles, manage projects, and record tasks associated with their projects.

## Features

- **User Management:** Create users with a name and email address.
- **Project Management:** Create projects with a title, description, and due date.
- **Task Management:** Create tasks with a title, status, and assigned person.
- **Object-Oriented Design:** Uses Python classes to represent users, projects, and tasks.
- **JSON Data Persistence:** Stores application data in a JSON file.
- **Dictionary-Based Storage:** Maintains collections of users, projects, and tasks using class-level dictionaries.

## Technologies Used

- Python 3
- `argparse` — for handling command-line arguments.
- `json` — for reading and writing JSON data.
- Object-Oriented Programming (OOP) — for structuring the application.

## Project Structure

```text
project-management-app/
│
├── main.py
│
├── models/
│   ├── User.py
│   ├── Project.py
│   └── Task.py
│
├── templates/
│   └── Project_template.py
│
└── data/
    └── Project_data.json
```

**Note:** The structure above is an example based on the imports in the application. Adjust the filenames and directories to match your actual project.

## How It Works

### 1. User Class

The `User` class represents an individual user.

Each user has:
- A name
- An email address
- A list of projects

The class also maintains a shared dictionary, `_users_list`, to keep track of created users.

Example:

```python
user = User("Hope", "hope@email.com")
```

The `add_projects()` method associates a project entry with the user.

### 2. Project Class

The `Project` class inherits from `Project_template` and represents a project.

Each project has:
- A title
- A description
- A due date
- A user reference
- A list of tasks

The class maintains a dictionary, `_projects`, containing created project objects.

Example:

```python
project = Project(
    "AI Application",
    "Build an AI application",
    "2026-12-01"
)
```

### 3. Task Class

The `Task` class represents a task.

Each task has:
- A title
- A status
- An assigned person

The class maintains a dictionary, `_tasks`, containing created task objects.

Example:

```python
task = Task(
    "Design database",
    "In Progress",
    "Hope"
)
```

### 4. JSON Data Storage

The application uses `data/Project_data.json` to store application records.

The JSON file is expected to contain three top-level dictionaries:

```json
{
    "Users": {},
    "Projects": {},
    "Tasks": {}
}
```

The application converts objects into dictionaries through their `to_dict()` methods and writes the data to the JSON file.

Example user record:

```json
{
    "name": "Hope",
    "email": "hope@email.com",
    "projects": ["AI Application"]
}
```

## Installation and Setup

### Prerequisites

Install Python 3.10 or later. The application uses Python's standard library for argument parsing and JSON operations.

### 1. Clone the repository

If the project is hosted on GitHub:

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd project-management-app
```

### 3. Run the application

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

Follow the prompts to enter user, project, and task details.

## Data Persistence

The application reads existing JSON data and updates the `Users`, `Projects`, and `Tasks` dictionaries before writing the updated data back to the file.

Ensure that `data/Project_data.json` exists and contains valid JSON before running the current implementation.

Example initial file:

```json
{
    "Users": {},
    "Projects": {},
    "Tasks": {}
}
```

## Learning Objectives

This project provides practice with:

- Defining classes and creating instances.
- Using instance attributes and class attributes.
- Working with class methods and static methods.
- Passing objects between methods.
- Managing relationships between users, projects, and tasks.
- Converting objects into dictionaries with `to_dict()`.
- Reading and writing JSON files.
- Organizing Python code into modules and packages.

## Future Improvements

Potential enhancements include:

- User authentication and login.
- Assigning projects to their owners.
- Associating tasks directly with projects.
- Validating project due dates and task statuses.
- Preventing duplicate usernames, project titles, and task titles.
- Automatically creating the JSON data file if it does not exist.
- Separating the CLI interface from application logic.
- Adding automated tests with `pytest`.
- Adding project editing, deletion, and listing functionality.

## License
MIT

~
## Author

Hope Kathomi


