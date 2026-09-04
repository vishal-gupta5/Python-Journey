# Basic Syntex

print("Hello World!") # Print Hello World
print("Hello World ", "With Python") # Concate string with Space
print("Vishal \nGupta") # Print in Next line

#! Variables

name = "Vishal"
age = 23
PI = 3.14

print("My name is:", name)
print("My age is:", age)
print("The value of PI is:", PI)


#! Data Types

city_name = "Bareilly"  # String Value
price = 10 # Integer value
isTrue = True # Boolean Value


print(type(city_name))
print(type(price))
print(type(isTrue))


#! Style Guide

tot_price = 100 # snake_case
totPrice = 200 # camel_case
TotPrice = 300 # pascal_case


#! Operators

# Assigement Operators (=, +=, -=, *=, /=)
a = 10
b = 5

# Arithemtic Operators (+, -, *, /, %, **)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)


# Relational / Comparison Operators (>, >=, <, <=, ==, !=)

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

# Logical Operators (not, and, or)

print((5 > 2) and (1 < 3)) # True
print((5 < 2) or (1 > 3)) # False


#! Type Conversion

ans1 = int(5 + 10.0) # Casting
ans2 = 5 + 10.0 # Conversion

print(ans1, type(ans1))
print(ans2, type(ans2))