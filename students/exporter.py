import csv
import json

# export to json


def export_to_json(filename, students):
    with open(filename, "w") as f:
        json.dump(students, f, indent=2)


# export to csv


def export_to_csv(filename, students):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Average"])

        for sid, data in students.items():
            grades = data["grades"]
            avg = sum(grades) / len(grades) if grades else 0

            writer.writerow([sid, data["name"], data["email"], avg])
