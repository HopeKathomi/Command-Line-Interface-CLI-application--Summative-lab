import json

def load_data():
    with open("data/Project_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Ensure both sections exist.
    data.setdefault("Users", {})
    data.setdefault("Projects", {})

    return data


def save_data(data):
    with open("data/Project_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
