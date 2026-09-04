# User Authentication
username = input("Enter the username: ")
password = input("Enter the password: ")

if (username == "admin" and password == "pass"):
    print("Login Successfully!")
elif (username != "admin"):
    print("Wrong Username!")
else: 
    print("Wrong Password")
    
    
# Check number is multiple of 5 or not

n = int(input("Enter the value of n: "))

if (n % 5 == 0): 
    print(n, " is a multiple of 5")
else:
    print(n, " is not a multiple of 5")
    
    
# Check the number is even or odd

value = int(input("Enter the value: "))

if (value % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")