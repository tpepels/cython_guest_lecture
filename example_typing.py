# Example of dynamic typing in Python

# Variables can change types dynamically
x = 5  # Initially an integer
print(f"x is of type {type(x)} and has value {x}")

x = "Hello, dynamic typing!"  # Now a string
print(f"x is of type {type(x)} and has value {x}")

x = [1, 2, 3]  # Now a list
print(f"x is of type {type(x)} and has value {x}")


# Function demonstrating dynamic typing in parameters
def dynamic_function(a):
    print(f"Parameter 'a' is of type {type(a)} and has value {a}")


# Passing different types to the same function
dynamic_function(10)  # Integer
dynamic_function("Dynamic!")  # String
dynamic_function([4, 5, 6])  # List


# Benefit: Same code can handle different types
# without modification
def add(a, b):
    return a + b


# Using the same 'add' function with different types
print(add(3, 4))  # Works with integers
print(add("Hello, ", "world!"))  # Works with strings
print(add([1, 2], [3, 4]))  # Works with lists


# Capability: Python's dynamic typing allows duck typing
class Duck:
    def quack(self):
        return "Quack!"


class Dog:
    def quack(self):
        return "Bark that sounds like a quack!"


def make_it_quack(animal):
    print(animal.quack())


# Duck typing in action: if it quacks like a duck, it must be a duck
duck = Duck()
dog = Dog()
make_it_quack(duck)  # Quack!
make_it_quack(dog)  # Bark that sounds like a quack!

import sys

# Define variables of different types
int_var = 10
float_var = 10.0
string_var = "Hello"
list_var = [1, 2, 3]

# Show how Python stores and resolves these types dynamically
print(f"Integer (int_var): {int_var}")
print(f"Type of int_var: {type(int_var)}")
print(f"Memory size of int_var: {sys.getsizeof(int_var)} bytes")
print(f"Memory address of int_var: {id(int_var)}\n")

print(f"Float (float_var): {float_var}")
print(f"Type of float_var: {type(float_var)}")
print(f"Memory size of float_var: {sys.getsizeof(float_var)} bytes")
print(f"Memory address of float_var: {id(float_var)}\n")

print(f"String (string_var): {string_var}")
print(f"Type of string_var: {type(string_var)}")
print(f"Memory size of string_var: {sys.getsizeof(string_var)} bytes")
print(f"Memory address of string_var: {id(string_var)}\n")

print(f"List (list_var): {list_var}")
print(f"Type of list_var: {type(list_var)}")
print(f"Memory size of list_var: {sys.getsizeof(list_var)} bytes")
print(f"Memory address of list_var: {id(list_var)}\n")

a = 5
b = 10
c = a + b


