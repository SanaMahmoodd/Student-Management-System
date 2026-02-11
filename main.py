from students.manager import register_student, add_grade, top_students
from students.storage import load_students, save_students
from students.exporter import export_to_json, export_to_csv


def main():
    students = load_students("students.json")

    while True:
        print("\n--- Student Management System ---")
        print("1) Register student")
        print("2) Add grade")
        print("3) Show top students")
        print("4) Export to JSON")
        print("5) Export to CSV")
        print("0) Exit")

        choice = input("Choose: ")

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

        elif choice == "2":
            sid = input("ID: ")
            try:
                grade = float(input("Grade: "))
                add_grade(students, sid, grade)
                save_students("students.json", students)
                print("Grade added.")
            except Exception as e:
                print(e)

        elif choice == "3":
            top = top_students(students)
            for sid, data in top:
                print(f"{sid} - {data['name']}")

        elif choice == "4":
            export_to_json("exported_students.json", students)
            print("Exported to JSON.")

        elif choice == "5":
            export_to_csv("exported_students.csv", students)
            print("Exported to CSV.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
