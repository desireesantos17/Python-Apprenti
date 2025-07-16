string1 = "This is a valid string"
string2 = 'This is also a valid string'

palindrome ="Go hang a salami, I'm a lasagna hog"

# Using a quote inside string 

string3 = "'Always look at the bright side of life'- Monty Python"

#Use escape characters to include quotes in strings 

string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

#len() function

print(len(string4))


# strip () function

name = "      Desiree       "
print(len(name))
print(name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print("Hello " + name_no_spaces)


#split()

filepath = "/var/Desiree/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

# print(names): ['Desiree', 'Santos']
firstname = name [0]
lastname = name [1]
print ("First name: " + firstname)
print ("Last Name: " + lastname)

# join

windowsPath = "\\".join(folders)
print(windowsPath)

# find()

reservation_name = "Pepper, Corgi"
char_to_find = "X"
# Where is the comma? 

char_location = reservation_name.find(char_to_find)
print(char_location)

# index()
if char_to_find in reservation_name:
    char_location = reservation_name.index(char_to_find)
    print(char_location)

# transformations

print(reservation_name.upper())


#f-strings

name = "Desiree"
age = 30 

print(f"My name is {name} and I am {age} years old")

a = 3
b = 9 
print(f'We can count to {b} by {a}: {a} {a*2} {a*3}')

#replacing

name = "Desirae Santos"
name = name.replace("Desirae", "Desiree")
print(name)