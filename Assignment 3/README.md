# Assignment – Functions and Math Module in Python 🐍

This assignment contains two Python programs that practice:

- Defining and using **functions**
- Implementing **loop control structures**
- Performing **factorial calculations**
- Using Python’s built-in **math module**
- Working with user input and formatted output  

---

## 📂 Files Included

- `tuteDA3Q1.py` – Calculate the factorial of a number  
- `tuteDA3Q2.py` – Square root, logarithm, and sine calculations  

---

## 🔢 1. `tuteDA3Q1.py` – Calculate the Factorial of a Number

This program:

- Asks the user to enter an **integer number**
- Uses a **user-defined function**
- Implements a `for` loop for factorial calculation
- Prints the factorial in a readable format  

### 🛠 How It Works

1. The program defines a function named `factorial(num)`.
2. A variable `fact` is initialized with the value `1`.
3. A `for` loop runs to multiply numbers in descending order.
4. The function returns the final factorial value.
5. The result is printed using an f-string.

### ▶ Example Usage

```text
EX1:
Enter a number: 5
Factorial of 5 is: 120

EX2:
Enter a number: 8
Factorial of 8 is: 40320
```

## 📐 2. `tuteDA3Q2.py` – Using the Math Module for Calculations

This program:

- Uses Python’s built-in **math module**
- Takes a number as input from the user
- Calculates the **square root**, **logarithm**, and **sine**
- Displays the calculated results in a readable format  

### 🛠 How It Works

1. The program imports the math module using `import math as mt`.
2. The user enters a number using `input()`.
3. The value is converted into an integer using `int()`.
4. `mt.sqrt(num)` calculates the square root of the number.
5. `mt.log(num)` calculates the natural logarithm (base *e*).
6. `mt.sin(num)` calculates the sine of the number (input is treated as radians).
7. The results are printed using formatted strings.

### ▶ Example Usage

```text
Enter a number: 25
Square root: 5.0
Logarithm: 3.2188758248682006
Sine: -0.13235175009777303
```
