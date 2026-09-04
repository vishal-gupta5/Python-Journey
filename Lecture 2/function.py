# Function in Python

def hello(): # Function Definitionn
    print("Hello Guys!")
hello() # Function call or invocation


# Sum of two numbers 

def sum(a, b):
    s = a + b
    return s

ans = sum(4, 5)
print(ans)


#! Types of functions in Python
# There are various types of function
    # 1. Built-in function
    # 2. User Defined function
    # 3. Lambda function 
    
# Lambda function
sum = lambda a, b: a + b
print(sum(5, 7))