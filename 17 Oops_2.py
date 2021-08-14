class Employee():
    increment = 1
    def __init__(self,name, lname, salary) -> None:
        self.name =name
        self.salary = salary
        self.lname = lname
    def increase(self):
             self.salary = int(self.increment*self.salary)
    
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    @classmethod                                 # Alternative constructor
    def from_str(cls, emp_string):
        name, lname, salary = emp_string.split("-")
        return cls(name, lname, salary)

#vikash = Employee("Vikash sharma", 20000)
vikash1 = Employee.from_str("vikash-sharma-23000")

print(vikash1.lname)

'''print(vikash.salary)
vikash.increase()
print(vikash.salary)
Employee.change_increment(3)
vikash.increase()
print(vikash.salary)'''
    