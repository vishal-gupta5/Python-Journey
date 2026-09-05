
class Student:
    def __init__(self): #Defualt Constructor
        print("Object is being constructed!")
    
    def __init__(self, name, city): #Parameterized Constructor
        self.name = name
        self.city = city
            
    def get_cgpa(self):
        return self.city

stu = Student("Vishal", "Bareilly")
print(f"{stu.name} lives in {stu.get_cgpa()}") 