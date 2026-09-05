# Multiple Interitance

class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
        
class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TA(Teacher, Student):
    def __init__(self, salary, cgpa, name):
        super().__init__(salary)
        Student.__init__(self, cgpa)
        self.name = name
        
s1 = TA(150000, 8.6, "Vishal")
print(s1.name, s1.cgpa, s1.salary)


        