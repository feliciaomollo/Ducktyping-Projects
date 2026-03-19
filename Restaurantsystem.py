class Employee:
    def __init__(self, name, age, years_worked, salary, department):
        self.name = name
        self.age = age
        self.years_worked = years_worked
        self.__salary = salary #introducing encapsulation
        self.__department = department 

    def __str__ (self):
        return f"The employee's name is {name}, {age} and has worked for {years_worked}"
    
    def __eq__(self):
