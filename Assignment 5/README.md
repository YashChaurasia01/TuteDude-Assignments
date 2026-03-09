# Assignment – Dictionary and List Operations in Python 🐍

This assignment contains two Python programs that practice:

- Working with **dictionaries**
- Storing and retrieving key-value pairs
- Handling missing keys gracefully
- Implementing **list slicing**
- Extracting elements from a list
- Reversing lists using slicing techniques
- Using **user input** and **formatted output**

---

## 📂 Files Included

- `tuteDA5Q1.py` – Create a dictionary of student marks and retrieve them by name
- `tuteDA5Q2.py` – Demonstrate list slicing and reversal

---

## 📖 1. `tuteDA5Q1.py` – Dictionary of Student Marks

This program:

- Creates a **dictionary** where student names are keys and their marks are values
- Asks the user to input a student's name
- Retrieves and displays the corresponding marks
- Handles the case where the student's name is **not found** in the dictionary

---

### 🛠 How It Works

1. A dictionary named `students` is created with student names as keys and marks as values.
2. The user is prompted to enter a student's name using `input()`.
3. `.strip()` is used to remove any accidental leading or trailing spaces from the input.
4. `students.get(name)` is used to safely retrieve the marks without raising a `KeyError`.
5. If the name exists, the marks are displayed using an f-string.
6. If the name is not found, an appropriate message is displayed.

---

### ▶ Example Usage

```text
If student exists in dictionary:

Enter the student's name: Yash
Yash's marks : 85

If student doesn't exist in dictionary:

Enter the student's name: Hani
Student not found.
```

---

## 📝 2. `tuteDA5Q2.py` – List Slicing Demonstration

This program:

- Creates a list of numbers from **1 to 10**
- Extracts the **first five elements** using list slicing
- **Reverses** the extracted elements using slice notation
- Displays the original list, extracted list, and reversed list
- Demonstrates the use of **`range()`**, **list slicing (`[:]`)**, and **reverse slicing (`[::-1]`)**

---

### 🛠 How It Works

1. `range(1, 11)` generates numbers from 1 to 10.
2. `list()` converts the range object into a list.
3. `numbers[:5]` slices the first five elements from the list.
4. `extracted[::-1]` reverses the extracted list using a step of `-1`.
5. All three lists — original, extracted, and reversed — are printed using f-strings.

---

### ▶ Example Usage

```text
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```
