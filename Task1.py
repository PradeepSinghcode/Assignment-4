# Task 1: Read a File and Handle Errors 
a = 'sample.txt'
try:
    file =  open(a, 'r')
    print("Reading file content:")
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{a}' was not found")
