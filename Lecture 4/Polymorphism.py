# Polymorphism in Python

# Function Overriding 
class Employee:
    def get_degination(self):
        print("Degination = Employee")


class Teacher(Employee):
    def get_degination(self):
        print("Degination = Teacher")

t1 = Teacher();
t1.get_degination()



class Student:
    def home_work(self):
        print("Home Work")

class WorkingProfessionals:
    def home_work(self):
        print("Complete your office work at home!")

s = Student();
s.home_work();

w = WorkingProfessionals();
w.home_work();