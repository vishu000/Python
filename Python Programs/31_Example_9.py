class Employee:
    
    def __init__(self):
        self._project = "NLP" # private class
    
    def show(self):
        print(self._project) #  # private members are accessible from a class

class student(Employee):
    
    def __init__(self, age):
        self.age = age
        Employee.__init__(self)
    
    def show1(self):
        print(self.age)
        print(self._project)
    
emp1 = student(12)   
#emp = Employee()
emp1.show1()
# Or
# direct access to private member using name mangling
#print(emp.name, emp._Employee__salary)
        