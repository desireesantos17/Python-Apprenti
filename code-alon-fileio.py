import os


file_path = 'data.csv'

print(file_path)

file = open(file_path, 'r')
file = open(file_path, 'w')
file = open(file_path, 'a')
file = open(file_path, 'r+')

#write function will create a new file OR overwrite an existing file
file = open("example.txt", 'w')
file.write("Hello, world!\n")
file.write("This is line two!\n")
file.close()

with open("example-with.txt", "w") as file:
    file.write("We wrote this using the with statement!\n")
    file.write("This is line two.\n")
    file.write("This is line three.\n")
    

# use for loop to read lines from a file    

with open("example-with.txt", "r") as file:
    for line in file:
        print(line.strip())

#Append to a file

with open("example-with.txt", "a") as file:
    file.write("This is an appended line.\n")


# delete a file
if os.path.exists("example-with2.txt"):
    os.remove("example-with2.txt")
    print("File deleted successfully.")
else:
    print("The file does not exist.")