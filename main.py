import my_module
import math 

print(math.sqrt(16))

#Using a function from the module
print(my_module.greet("Alice"))

# Using a class from the module 
greeter = my_module.Greeter("Bob")
print(greeter.greet())

#Accessing a variable from the module 
print(my_module.my_variable)
