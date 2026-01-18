# Task 1: To calculate the factorial

def factorial(num):
    fact = 1
    for i in range(num):
        fact *= num
        num -= 1

    return fact


num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")

"""
Output Sample:

EX1:
Enter a number: 5
Factorial of 5 is: 120

EX2:
Enter a number: 8
Factorial of 8 is: 40320
"""
    