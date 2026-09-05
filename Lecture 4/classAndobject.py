# Create a Class in python
class Student:
    def __init__(self, name, cgpa): # Define Constuctor
        self.name = name
        self.cgpa = cgpa
    
    def get_cgpa(self):
        return self.cgpa

std1 = Student("Vishal", "Bareilly") # Object
std2 = Student("Urvashi", "Delhi")

print(f"{std1.name} has cgpa = {std1.get_cgpa()}")