from CarClasses.Employee import Employee
from CarClasses.Supplier import Supplier

class Manager(Employee, Supplier):
    def __init__(self, name, age, contactNumber, Employee_id, Position, Salary, Company_name, Supply_type, CarStock):
        Employee.__init__(self, name, age, contactNumber, Employee_id, Position, Salary)
        Supplier.__init__(self, name, age, contactNumber, Company_name, Supply_type, CarStock)

    def DataPrint(self):
        super().DataPrint()
        print(self.Company_name)