from employee import Employee

class Main:
    def __init__(self):
        self._id = 0
        self.list = {}
    def menu(self):
        menuon = True
        while(menuon == True):
            print("What would you like to do?")
            print("1 - Add employee")
            print("2 - Remove employee")
            print("3 - Salary operations")
            print("4 - Show all employees")
            print("e - Exit")

            userchoice = str(input("choice: "))
            if userchoice == "1":
                self.add_employee()
            elif userchoice == "2":
                self.remove_employee()
            elif userchoice == "4":
                self.show_employees()
            elif userchoice == "3":
                self.salary()
            elif userchoice == "e":
                menuon = False
            else:
                print("error")
    def IDcounter(self):
        self._id += 1
        return self._id
    def add_employee(self):
        name = input("Name of the employee: ")
        surname = input("Surname of the employee: ")
        age = int(input("Age of the employee: "))
        salary = int(input("Salary of the employee: "))
        
        employee_id = self.IDcounter()
        employee = Employee(employee_id, name, surname, age, salary)

        self.list[employee_id] = employee

        print("Employee " + name +" "+ surname + " added")
    def remove_employee(self):
        for emp in self.list:
            print(str(emp) +" "+ str(self.list[emp].name))
        which = int(input("Which employee do you want to remove (by id): "))
        if which in self.list:
            self.list.pop(which)
        else:
            print("invalid id")
    def show_employees(self):
        for emp in self.list:
            print(str(emp) +" "+ str(self.list[emp].name)+" "+ str(self.list[emp].surname)+" "+ str(self.list[emp].age)+" "+ str(self.list[emp].salary))
    def salary(self):
        idemp = int(input("Write id of an employee: "))
        if idemp in self.list:
            emp = self.list[idemp]
            print("Salary of this employee: " + str(emp.get_salary())) 
            oper = input("Do you want to change it? (y/n): ")
            if oper == "y":
                newsalary = input("How much: ")
                emp.set_salary(newsalary)
                print("New salary of this employee: " + str(emp.get_salary())) 
        else:
            print("invalid id")



M = Main()
M.menu()