# Python CLI Project Management System

## 1. Project Overview

The Python CLI Project Management System is a command-line application developed using Python. It allows users to manage users, projects, and project tasks through commands entered in the terminal.

The application uses Object-Oriented Programming (OOP) to organise its code into classes and stores user and project information in a JSON file.

The system is designed to simplify project organisation by allowing users to create accounts, view registered users, create projects, assign projects to users, and add tasks to projects.

## 2. Features

- **Add Users:** Register users using their names and email addresses.
- **List Users:** Display all registered users.
- **Create Projects:** Create projects with a title, description, and due date.
- **Assign Projects:** Select an existing user to associate with a project.
- **Create Tasks:** Add tasks to existing projects.
- **List Projects:** Display project information available through the application's in-memory project collection.
- **JSON Storage:** Save user and project information in `data/Project_data.json`.
- **Input Validation:** Validate numeric selections when assigning projects and adding tasks.
- **Empty Input Handling:** Prevent task creation when the task title is empty.

## 3. Technologies Used

- **Python 3:** Main programming language.
- **argparse:** Creates and manages command-line arguments and subcommands.
- **json:** Reads and writes application data in JSON format.
- **Object-Oriented Programming:** Organises the application into `User`, `Project`, and `Task` classes.

The application uses Python's standard library and does not require third-party packages for the functionality shown.

## 4. Project Structure

The project follows this general structure:

```text
project-management-system/
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
├── data/
│   └── Project_data.json
│
└── README.md
```

- `main.py` contains the command-line interface and functions for managing users, projects, and tasks.
- `models/User.py` defines the `User` class.
- `models/Project.py` defines the `Project` class.
- `models/Task.py` defines the `Task` class.
- `templates/Project_template.py` provides the project template inherited by the `Project` class.
- `data/Project_data.json` stores user and project information.
- `README.md` documents the application and how to use it.

## 5. Installation and Setup

### Prerequisites

Install Python 3 on your computer.

Verify the installation by running:

```bash
python --version
```

### Clone the Repository

Clone the repository from GitHub:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd project-management-system
```

### Prepare the Data File

Ensure that `data/Project_data.json` exists and contains the required top-level keys.

Example:

```json
{
    "Users": {},
    "Projects": {}
}
```

The application expects these keys when adding users, assigning projects, and creating tasks.

### Run the Application

Run the main Python file:

```bash
python main.py
```

The application uses `argparse` to process commands. A command must be supplied because the subparsers are configured with `required=True`.

## 6. Available Commands

The application defines the following command-line subcommands.

### 6.1 Add a User

Creates a user with a name and email address and saves the user to the JSON file.

**Syntax:**

```bash
python main.py add-user <name> <email>
```

**Example:**

```bash
python main.py add-user Hope hope@example.com
```

**Expected output:**

```text
User created: Hope
Email: hope@example.com
```

The new user is stored under the `Users` key in `Project_data.json`.

### 6.2 List Users

Displays the names of all registered users.

**Command:**

```bash
python main.py list-users
```

**Example output:**

```text
List of users:
Hope
Kathomi
Marveline
```

The command reads user records directly from `Project_data.json`.

### 6.3 Create a Project

Creates a project using its title, description, and due date. The application then displays the registered users and prompts you to select a user for the project.

**Syntax:**

```bash
python main.py create-project <title> <description> <due_date>
```

**Example:**

```bash
python main.py create-project Roads "Road construction project" 30-12-2026
```

The application displays the project details and prompts:

```text
New project:
Title: Roads
Description: Road construction project
Due_date: 30-12-2026

Select a user to assign to this project:
1. Hope
2. Kathomi
3. Marveline
Enter the number of the user:
```

Enter the number corresponding to the user you want to assign.

The selected user's `projects` list is updated, and the project information is saved in the `Projects` section of the JSON file.

**Note:** The description should be enclosed in quotation marks when it contains spaces. In the current implementation, the project is saved in JSON by `assign_project_to_user()`.

### 6.4 Create a Task

Adds a task to an existing project.

**Syntax:**

```bash
python main.py Create-task <title> <status> <assigned_to>
```

**Example:**

```bash
python main.py Create-task "Prepare budget" Pending Hope
```

The current implementation prompts the user to select a project and enter a task title.

**Example interaction:**

```text
Available Projects:
1. Roads
2. Water Supply
Select a project number: 1
Enter the task title: Prepare budget
```

**Expected output:**

```text
Task 'Prepare budget' successfully added to 'Roads'.
```

The task title is added to the selected project's `tasks` list in the JSON file.

**Important:** Although the command accepts `title`, `status`, and `assigned_to`, the current `create_tasks_for_projects()` function does not use these arguments. It asks for the task title interactively and stores only that title in the selected project's task list.

### 6.5 List Projects

**Command:**

```bash
python main.py list-projects
```

This command currently prints the `Project._projects` dictionary.

However, the projects created through the command-line function are saved in the JSON file rather than being added to `Project._projects`. Consequently, this command may display an empty dictionary even when projects exist in the JSON file.

To list saved projects correctly, the function should read the `Projects` key from `Project_data.json`.

## 7. JSON Data Storage

The application uses the `json` module to read and write data.

### Example Data Structure

```json
{
    "Users": {
        "Hope": {
            "name": "Hope",
            "email": "hope@example.com",
            "projects": [
                "Roads"
            ]
        }
    },
    "Projects": {
        "Roads": {
            "title": "Roads",
            "name": "Road construction project",
            "due_date": "30-12-2026",
            "tasks": [
                "Prepare budget"
            ]
        }
    }
}
```

The `Users` section stores user details and the project titles associated with each user.

The `Projects` section stores project details and the tasks added to each project.

**Note:** In the current code, the project's description is saved under the key `name`, rather than `description`. Also, the `tasks` list stores task titles as strings, not complete task objects.

## 8. Object-Oriented Programming

The application uses three main classes.

### User Class

Represents registered users and includes methods for creating users, managing their project lists, and converting user data into dictionaries.

### Project Class

Represents projects, including their titles, descriptions, due dates, assigned users, and tasks. It inherits from `Project_template`.

### Task Class

Represents tasks using a title, status, and assigned person. Its `to_dict()` method converts task information into a dictionary.

The current command-line task creation function does not instantiate the `Task` class; it stores task titles directly in the JSON file.

## 9. Input Validation and Error Handling

The application includes basic validation for project and task selection:

- Checks whether any users exist before assigning a project.
- Checks whether any projects exist before creating a task.
- Rejects selections outside the available numbered options.
- Handles non-numeric selections using `try` and `except ValueError`.
- Prevents empty task titles from being saved.

Further validation could be added to prevent duplicate project titles, duplicate task entries, invalid email addresses, and incorrectly formatted due dates.

## 10. Current Limitations and Future Improvements

The following improvements would make the application more complete:

1. Update `list_projects()` to read saved projects from `Project_data.json`.
2. Use the `description` key consistently instead of storing the project description under `name`.
3. Implement `get_users_projects()` to display projects associated with a particular user.
4. Update task creation to use the supplied title, status, and assigned person, or revise the command to match the interactive workflow.
5. Store complete task records, including title, status, and assigned person.
6. Prevent duplicate project titles and duplicate task entries.
7. Validate project due dates and user email addresses.
8. Improve error handling for missing or invalid JSON files.
9. Add automated tests using `pytest`.
10. Ensure that the `Project`, `User`, and `Task` class methods are consistent with the command-line functions.

## 11. Conclusion

The Python CLI Project Management System provides a foundation for managing users, projects, and tasks through terminal commands. It combines Python's `argparse` and `json` modules with Object-Oriented Programming to organise data and support basic project management workflows.

Future enhancements, including improved validation, consistent data structures, project listing, and more complete task management, can make the application more reliable and easier to maintain.
