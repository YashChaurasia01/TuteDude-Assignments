# Assignment 2 – Control Structures in Python 🐍

This assignment contains two Python programs that practice:

- Using conditional statements (`if–else`)
- Applying arithmetic operations with conditions
- Implementing loop control structures
- Working with variables and formatted output  

---

## 📂 Files Included

- `tuteDA2Q1.py` – Check if a number is Even or Odd  
- `tuteDA2Q2.py` – Sum of integers from 1 to 50  

---

## 🔢 1. `tuteDA2Q1.py` – Check if a Number is Even or Odd

This program:

- Asks the user to enter an **integer number**
- Uses an `if–else` conditional statement
- Checks whether the number is **even or odd**
- Prints the result in a clear and readable format  

### 🛠 How It Works

1. The program uses `input()` to take a number from the user.
2. Converts the input value to an integer using `int()`.
3. Uses the modulus operator (`%`) to check divisibility by 2.
4. If the remainder is `0`, the number is even; otherwise, it is odd.
5. Displays the result using an f-string.

### ▶ Example Usage

```text
EX1:
Enter an number: 7
7 is an odd number.

EX2:
Enter an number: 12
12 is an even number.

## ➕ 2. `tuteDA2Q2.py` – Sum of Integers from 1 to 50

This program:

- Calculates the **sum of integers from 1 to 50**
- Uses a `for` loop to iterate through the range
- Stores the cumulative result in a variable
- Prints the final sum in a clear format  

### 🛠 How It Works

1. The program initializes a variable `sum` with the value `0`.
2. A `for` loop runs from `1` to `50` using `range(1, 51)`.
3. Each number in the loop is added to the `sum` variable.
4. The loop continues until all numbers are processed.
5. The final result is displayed using an f-string.

### ▶ Example Usage

```text
The sum of numbers from 1 to 50 is: 1275
