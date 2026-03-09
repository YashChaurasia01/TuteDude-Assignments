# Task 1: Create a Dictionary of Student Marks

students = {
    "Yash": 85,
    "Ashu": 92,
    "Utkarsh": 78,
    "Rahul": 88,
    "Priya": 95,
    "Amit": 70,
}

name = input("Enter the student's name: ").strip()

marks = students.get(name)

if marks:
    print(f"{name}'s marks : {marks}")
else:
    print(f"Student not found.")


"""

Output Sample:

If student exist in dictionary:

Enter the student's name: Yash
Yash's marks : 85

If student doesn't exist in dictionary:

Enter the student's name: Hani
Student not found.

"""