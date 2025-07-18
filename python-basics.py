# variables 
name = "Pepper" #string 
age = 7 #integer
weight = 19.5 #float
is_dog = True #boolean

# input & output
name = input("What is your name? ")
print("Hello, " + name + "!")


# lists 
toys = ["ball", "monster", "racoon"]
print(toys [0]) # prints the first item in the list
toys.append("squirrel") # adds a new item to the list
toys.remove("monster") # removes an item from the list
print(len(toys)) # prints the number of items in the list

# if statements 
if age < 3:
    print("You are a puppy.")
elif age > 10:
    print("You are a senior.")
else: 
    print("You are an adult.")

# for loops
toys = ["ball", "monster", "racoon"]
for toy in toys:
    print(toy)

# while loops
secret_bark_count = 3
guess = 0

while guess != secret_bark_count:
    guess = int(input("Guess the secret bark count (0-5): "))
    if guess < secret_bark_count:
        print("Too low!")
    elif guess > secret_bark_count:
        print("Too high!")
    else:
        print("Correct! You guessed the secret bark count.")

# functions
def greet(name):
    print("Hello, " + name + "!")
greet("Pepper")

# functions with return
def add(a, b):
    return a + b
result = add(5, 3)
print(result) # prints 8 

