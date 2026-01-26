# Assignment – File Handling and Exception Handling in Python 🐍

This assignment contains two Python programs that practice:

- Working with **file handling**
- Reading and writing text files
- Appending data to existing files
- Implementing **exception handling**
- Using `try`–`except` blocks
- Working with user input and formatted output  

---

## 📂 Files Included

- `tuteDA4Q1.py` – Read a file and handle file-related errors  
- `tuteDA4Q2.py` – Write and append data to a file  

---

## 🗃️ 1. `tuteDA4Q1.py` – Read a File and Handle Errors

This program:

- Tries to open a text file named **`sample.txt`**
- Reads and displays the file content line by line
- Prints line numbers along with each line
- Handles the error if the file does not exist
- Raises a custom `FileNotFoundError` with a clear message  

---

### 🛠 How It Works

1. The filename is stored in a variable named `file_n`.
2. The program attempts to open the file in **read text mode (`'rt'`)**.
3. A message `"Reading file content:"` is printed.
4. A counter variable is initialized to track line numbers.
5. Each line of the file is read using a `for` loop.
6. Lines are printed with their respective line numbers.
7. If the file does not exist, a `FileNotFoundError` is raised with a custom error message.

---

### ▶ Example Usage

```text
If file exists:

Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

---

## 📝 2. `tuteDA4Q2.py` – Write and Append Data to a File

This program:

- Takes text input from the user
- Writes the input to a file named **`output.txt`**
- Appends additional text to the same file
- Displays the final content of the file
- Demonstrates the use of **write (`'w'`)**, **append (`'a'`)**, and **read (`'r'`)** file modes  

---

### 🛠 How It Works

1. The filename is stored in the variable `file_n`.
2. The user enters text to write to the file.
3. The file is opened in **write mode (`'w'`)**, which creates or overwrites the file.
4. The entered text is written to the file followed by a newline.
5. The user enters additional text to append.
6. The file is opened in **append mode (`'a'`)** to add new content without deleting existing data.
7. Finally, the file is opened in **read mode (`'r'`)** to display the complete content of the file.

---

### ▶ Example Usage

```text
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file Handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file Handling in Python.
```