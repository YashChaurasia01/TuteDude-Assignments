# Task 1: Read a File and Handle Errors.

file_n = 'sample.txt'
try:
    with open(file_n, 'rt') as file_name:
        print("Reading file content: ")
        l = 1
        for line in file_name.readlines():
            print(f"Line {l}: {line.strip('\n')}")
            l+=1
except FileNotFoundError:
    raise FileNotFoundError(f"Error: The file '{file_n}' was not found.")

"""
Output Sample:

If file exist:

    - Reading file content: 
      Line 1: This is a sample text file.
      Line 2: It contains multiple lines.

If file does't exist:

    - FileNotFoundError: Error: The file 'sample.txt' was not found.
"""