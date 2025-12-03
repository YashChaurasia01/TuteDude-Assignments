# Assignment 1 – Basic Python Programs

This assignment contains two simple Python programs that practice:

- Taking input from the user
- Performing basic arithmetic operations
- Working with strings and formatted output   

---

## Files Included

- `tuteDA1Q1.py` – Arithmetic operations on two numbers  
- `tuteDA1Q2.py` – Greeting the user using their first and last name  

---

## 📐1. `tuteDA1Q1.py` – Basic Arithmetic Calculator

This program:

- Asks the user to enter **two integers**
- Performs the following operations on them:
  - Addition  
  - Subtraction  
  - Multiplication  
  - Division  
- Prints each result with a label in a clear format :contentReference[oaicite:1]{index=1}  

### How It Works

1. The program uses `input()` to read two numbers from the user.
2. Converts them to integers using `int()`.
3. Performs `+`, `-`, `*`, and `/` operations.
4. Displays the results using formatted print statements (`f-strings`).

### ▶Example Usage

```text
Enter the first number: 5
Enter the second number: 10

Addition: 15
Subtraction: -5
Multiplication: 50
Division: 0.5
```

## 😀 2. `tuteDA1Q2.py` – Name Greeting Program

This program:

- Prompts the user to enter their **first name** and **second/last name**
- Formats both names properly
- Displays a personalized welcome message  
- Uses string methods and f-strings for clean output  :contentReference[oaicite:0]{index=0}

---

### 🛠 How It Works

1. The program uses `input()` to collect the user's first name and second name.  
2. It applies the `.title()` method to ensure the first letter of each name is capitalized.  
3. Combines the names with a space to form a full name.  
4. Prints a greeting using an f-string in a clean, readable format.  

---

### ▶ Example Usage

```text
Enter your first name: Yash
Enter your second name: Chaurasia

Hello, Yash Chaurasia! Welcome to the Python program.
```


