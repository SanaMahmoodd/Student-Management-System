import pytest
from students.manager import (
    register_student,
    add_grade,
    calculate_average,
    top_students,
    update_grade,
)


def test_register_student():
    students = {}
    register_student(students, "1", "Sana", "sana@mail.com")
    assert "1" in students


def test_duplicate_student():
    students = {"1": {"name": "Sana", "email": "x", "grades": []}}
    with pytest.raises(ValueError):
        register_student(students, "1", "Aya", "Aya@mail.com")


def test_add_grade():
    students = {"1": {"name": "Sana", "email": "x", "grades": []}}
    add_grade(students, "1", 90)
    assert students["1"]["grades"] == [90]


def test_average():
    avg = calculate_average([80, 100])
    assert avg == 90


def test_top_students():
    students = {
        "1": {"name": "A", "email": "x", "grades": [100]},
        "2": {"name": "B", "email": "x", "grades": [50]},
    }
    top = top_students(students, limit=1)
    assert top[0][0] == "1"


def test_update_grade():
    students = {"1": {"name": "Sana", "email": "x", "grades": [80, 90]}}

    update_grade(students, "1", 0, 100)
    assert students["1"]["grades"][0] == 100


def test_update_grade_student_not_found():
    students = {}

    with pytest.raises(ValueError):
        update_grade(students, "1", 0, 90)


def test_update_grade_invalid_index():
    students = {"1": {"name": "Sana", "email": "x", "grades": [80]}}

    with pytest.raises(IndexError):
        update_grade(students, "1", 5, 90)


def test_average_empty():
    assert calculate_average([]) == 0
