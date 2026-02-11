# function to register student


def register_student(students, student_id, name, email):
    if student_id in students:
        raise ValueError("Student ID already exists")

    students[student_id] = {"name": name, "email": email, "grades": []}


# function to add grade


def add_grade(students, student_id, grade):
    if student_id not in students:
        raise ValueError("Student not found")

    if grade < 0 or grade > 100:
        raise ValueError("Invalid grade")

    students[student_id]["grades"].append(grade)


# function to calculate average


def calculate_average(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


# function to return top students using : lambda, sorted, default argument


def top_students(students, limit=3):
    sorted_list = sorted(
        students.items(),
        key=lambda item: calculate_average(item[1]["grades"]),
        reverse=True,
    )

    return sorted_list[:limit]


# function to update grade by index


def update_grade(students, student_id, index, new_grade):
    if student_id not in students:
        raise ValueError("Student not found")

    if new_grade < 0 or new_grade > 100:
        raise ValueError("Invalid grade")

    grades = students[student_id]["grades"]

    if index < 0 or index >= len(grades):
        raise ValueError("Invalid grade index")

    grades[index] = new_grade
