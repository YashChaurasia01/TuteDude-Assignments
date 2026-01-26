# Task 2: Write and Append Data to a File

file_n = 'output.txt'

text_input = input("Enter text to write to the file: ")

with open(file_n, 'w') as file_name:
    file_name.write(text_input + "\n")
    print(f"Data successfully written to {file_n}.")


additional_text = input("\nEnter additional text to append: ")

with open(file_n, "a") as file_name:
    file_name.write(additional_text + "\n")
    print("Data successfully appended.")

print(f"\nFinal content of {file_n}:")

with open(file_n, "r") as file_name:
    print(file_name.read())



"""
Output Sample:

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file Handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file Handling in Python.

"""