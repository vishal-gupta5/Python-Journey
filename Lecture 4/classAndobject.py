# Create a Class in python
class Student:
    def __init__(self, name, city): # Define Constuctor
        self.name = name
        self.city = city

std1 = Student("Vishal", "Bareilly") # Object
std2 = Student("Urvashi", "Delhi")

print(std1.name)
print(std1.city)