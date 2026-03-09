# Task 2: Demonstrate List Slicing.

numbers = list(range(1, 11))

extracted = numbers[:5]

reversed_list = extracted[::-1]

print(f"Original list: {numbers}")
print(f"Extracted first five elements: {extracted}")
print(f"Reversed extrected elements: {reversed_list}")

"""

Output Sample:

Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extrected elements: [5, 4, 3, 2, 1]

"""