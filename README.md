# Student Management System

A Command-Line Student Management System built with Python.

This project allows you to manage students, update grades, export data, and ensure code quality using testing and CI tools.

------------------------------------------------------------------------

## Features

-   Register students (Name, ID, Email, Grades)
-   Update student grades
-   List top students based on average grade
-   Export student data to JSON and CSV
-   Input validation with proper exception handling
-   Unit tested with pytest
-   Linted with flake8
-   Formatted with black
-   CI pipeline using GitHub Actions

------------------------------------------------------------------------

## 📂 Project Structure

```
Student-Management-System/
│
├── students/
│   ├── __init__.py
│   ├── manager.py        # Core business logic (CRUD + top students)
│   ├── storage.py        # JSON persistence (load/save)
│   └── exporter.py       # Export to JSON / CSV
│
├── tests/
│   ├── __init__.py
│   └── test_manager.py   # Unit tests (pytest)
│
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI pipeline
│
├── students.json         # Data storage file
├── main.py               # CLI entry point
├── README.md
├── requirements.txt
└── .flake8
```

------------------------------------------------------------------------

##  Installation

Clone the repository:

    git clone https://github.com/SanaMahmoodd/Student-Management-System.git

Create virtual environment:

    python -m venv venv
    source venv/bin/activate  (Linux/Mac)
    venv\Scripts\activate     (Windows)

Install dependencies:

    pip install pytest flake8 black

------------------------------------------------------------------------

##  How to Run

Run the application:

    python main.py

Run tests:

    python -m pytest

Run linting:

    flake8 .

Check formatting:

    black --check .

------------------------------------------------------------------------

## Testing

This project includes at least 5 unit tests covering:

-   Student registration
-   Duplicate student validation
-   Grade updates
-   Average calculation
-   Top student selection

------------------------------------------------------------------------

## CI Pipeline

GitHub Actions automatically runs:

-   flake8
-   black --check
-   pytest

On every push and pull request to the main branch.

------------------------------------------------------------------------

## Technologies Used

-   Python 3.11
-   Pytest
-   Flake8
-   Black
-   GitHub Actions

------------------------------------------------------------------------

##  Author

Sana Saleh :) 

Built for training and practice to strengthen backend development fundamentals.