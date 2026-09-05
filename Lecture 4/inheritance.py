# Inheritance in Python

class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time
    
    
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
    
    
class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
        
t1 = Teacher("Physics")
print(t1.subject, t1.start_time, t1.end_time)

a1 = AdminStaff("Manager")
a1.change_time("5am")

print(a1.role, a1.start_time, a1.end_time)
        
        
