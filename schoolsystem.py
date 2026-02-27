#School Management System

class Staff:
    def __init__(self, name, age, salary, department, years_worked):
        self.name = name
        self.age = age 
        self.salary = salary
        self.department = department
        self.years_worked = years_worked

    #to return a friendly description of the staff member
    def __str__(self):
        return f"{self.name} is a member of the {self.department}"
    
    #to return the number of years they have worked (add years_worked as an attribute)
    def __len__(self):
        return self.years_worked
    
    #to compare two staff members as equal if they have the same name and department
    def __eq__ (self, other):
        if isinstance(other, Staff):
            if(other.name == self.name and other.department == self.department):
                return True
            return False
        

class Teacher(Staff):
    def __init__(self, name, age, salary, department, years_worked, subject):
        self.subject = subject
        super().__init__(name, age, salary, department, years_worked)

    def do_work(self):
        print (f"{self.name} teaches {self.subject}")

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Subject: {self.subject}"
    
class Librarian(Staff):
    def __init__(self, name, age, salary, department, years_worked, books_managed):
        self.books_managed = books_managed
        super().__init__(name, age, salary, department, years_worked)

    def do_work(self):
        return (f"{self.name} teaches {self.books_managed}")

    def __str__(self):
        return f"{self.name}, Age: {self.age}, books: {self.books_managed}"
    

class Coach(Staff):
    def __init__(self, name, age, salary, department, years_worked, sport):
        self.sport = sport
        super().__init__(name, age, salary, department, years_worked)

    def do_work(self):
        return (f"{self.name} teaches {self.sport}")

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Subject: {self.sport}"
    
class School:
    def __init__(self, name):
        self.name = name
        self.staff = [] #to store staff, cosider this correction
    
    def __getitem__(self, index):
        return self.staff[index]
    
     def hire(self, staff):
        self.staff.append(staff)
        print(f"{staff.name} hired at {self.name}")

    def fire(self, staff):
        if staff in self.staff:
            self.staff.remove(staff)
            print(f"{staff.name} has been let go")
        else:
            print(f"{staff.name} not found")

    def __len__(self):
        return self.staff
    
    for x in items:
        print x

teacher1 = Teacher("Alice", age = 40, salary = 50000, subject= "Math", department="Sciences", years_worked = 20)
librarian1 = Librarian("Tanya", age = 30, salary = 60000, books_managed= 600000, department="boks", years_worked = 5)
coach1 = Coach("Ivy", age = 20, salary = 70000, sport= "track", department="sports", years_worked = 7)

print(teacher1)
teacher1.do_work()