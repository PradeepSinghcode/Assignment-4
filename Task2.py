# Task 2: Write and Append Data to a File

f1 = 'output.txt'
a = input("Enter the to write to the file:")
file= open(f1,'w')
file.write(a+'\n')
print(f"Data successfully written to {f1}.\n")

b = input("Enter additional text to append:")
file = open(f1,'a')
file.write(b+'\n')
print(f"Data successfully apended.\n")

file = open(f1,'r')
print(f'Final content of {f1} is:')
for i in file:
    print(i.strip())