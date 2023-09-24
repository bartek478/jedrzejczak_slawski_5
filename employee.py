class Employee:
    def __init__(self, id, name, surname, age, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, SETsalary):
        self.salary = SETsalary
