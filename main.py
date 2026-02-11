from students.manager import (
    register_student,
    add_grade,
    top_students,
    calculate_average,
    update_grade,
)
from students.storage import load_students, save_students
from students.exporter import export_to_json, export_to_csv


def main():
    students = load_students("students.json")

    while True:
        print("\n--- Student Management System ---")
        print("1) Register student")
        print("2) Add grade")
        print("3) Update grade")
        print("4) Show student average")
        print("5) Show top students")
        print("6) Export to JSON")
        print("7) Export to CSV")
        print("0) Exit")

        choice = input("Choose: ")

        # Register
        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            email = input("Email: ")

            try:
                register_student(students, sid, name, email)
                save_students("students.json", students)
                print("Student registered.")
            except ValueError as e:
                print(e)

        # Add grade
        elif choice == "2":
            sid = input("ID: ")
            try:
                grade = float(input("Grade: "))
                add_grade(students, sid, grade)
                save_students("students.json", students)
                print("Grade added.")
            except Exception as e:
                print(e)

        # Update grade
        elif choice == "3":
            sid = input("ID: ")

            try:
                grades = students[sid]["grades"]

                if not grades:
                    print("No grades found.")
                    continue

                print("Current grades:")
                for i, g in enumerate(grades):
                    print(f"{i}) {g}")

                index = int(input("Enter grade index to update: "))
                new_grade = float(input("Enter new grade: "))

                update_grade(students, sid, index, new_grade)
                save_students("students.json", students)

                print("Grade updated successfully.")

            except Exception as e:
                print(e)

        # Show average
        elif choice == "4":
            sid = input("ID: ")

            try:
                grades = students[sid]["grades"]
                avg = calculate_average(grades)
                print(f"Average: {avg:.2f}")
            except KeyError:
                print("Student not found")

        # Show top students
        elif choice == "5":
            top = top_students(students)

            if not top:
                print("No students found.")
            else:
                for sid, data in top:
                    avg = calculate_average(data["grades"])
                    print(f"{sid} - {data['name']} (Average: {avg:.2f})")

        # Export JSON
        elif choice == "6":
            export_to_json("exported_students.json", students)
            print("Exported to JSON.")

        # Export CSV
        elif choice == "7":
            export_to_csv("exported_students.csv", students)
            print("Exported to CSV.")

        # Exit
        elif choice == "0":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
