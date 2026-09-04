# Condional Statements (if, elif, else)

age = int(input("Enter the age: "))

if age >= 18:
    print("You are eligible!")
else:
    print("You are not eligible!")
    
    
    
#! Traffic Light program

colour= input("Enter the colour: ")

if (colour == "red"):
    print("Stop!")
elif (colour == "yellow"):
    print("Ready to go!")
elif (colour == "green"):
    print("Go!")
else: 
    print("Please Enter the valid colour!")
    
    
#! Match Case

color = input("Enter the value of color for Match-Case: ")

match color:
    case "green":
        print("Go!")
    case "red":
        print("Stop!")
    case "yellow":
        print("Look")
    case _:
        print("Please enter the valid input!")