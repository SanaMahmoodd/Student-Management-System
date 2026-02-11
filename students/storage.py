import json

# load from JSON


def load_students(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


# save to JSON


def save_students(filename, students):
    with open(filename, "w") as f:
        json.dump(students, f, indent=2)
