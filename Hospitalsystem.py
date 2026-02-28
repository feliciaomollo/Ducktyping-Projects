#hospital management system


class MedicalStaff:
    def __init__(self, name, age, salary, department, years_worked):
        self.name = name
        self.age = age
        self.__salary = salary #encapsulation
        self.__department = department
        self.years_worked = years_worked

    def __len__(self):
        return {self.years_worked} 
    
    def __str__(self):
        return (f"{self.name} has worked in this company for {self.years_worked}")

    def __eq__(self, other):
        if isinstance(other, MedicalStaff):
            if (other.name == self.name and other.department == self.__department):
                return True
            return False

    #safely read private salary  
    def get_salary(self):
        return self.__salary
    
    # safely read private department
    def get_department(self):
        return self.__department
        
class Doctor(MedicalStaff):
    def __init__(self, name, age, salary, department, years_worked, specialization):
        super().__init__(name, age, salary, department, years_worked)
        self.specialization = specialization

    def do_work(self):
        return f"{self.name} works in {self.specialization}"

class Nurse(MedicalStaff):
    def __init__(self, name, age, salary, department, years_worked, ward):
        super().__init__(name, age, salary, department, years_worked)
        self.ward = ward

    def do_work(self):
        return f"{self.name} works in {self.ward}"

class Surgeon(MedicalStaff):
    def __init__(self, name, age, salary, department, years_worked, surgery_type):
        super().__init__(name, age, salary, department, years_worked)
        self.surgery_type = surgery_type

    def do_work(self):
        return f"{self.name} works in {self.surgery_type}"


doctor1 = Doctor("Dr. Amy", age=45, salary=90000, department="Cardiology", years_worked=15, specialization="Heart")
nurse1 = Nurse("Nurse John", age=30, salary=50000, department="ICU", years_worked=5, ward="Intensive Care")
surgeon1 = Surgeon("Dr. Eve", age=50, salary=120000, department="Surgery", years_worked=20, surgery_type="Neurosurgery")

class Hospital:
    def __init__(self, name):
        self.name = name
        self.staff = [] #always remember to store staff in an empty list
         
    def add_staff(self):
        self.staff.append()


    