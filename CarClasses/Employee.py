from CarClasses.Person import Person

class Employee(Person):
    def __init__(self, name, age, contactNumber, Employee_id, Position, Salary):
        Person.__init__(self, name, age, contactNumber)
        self.Employee_id = Employee_id
        self.Position = Position
        self.Salary = Salary

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | contact Number: {self.contactNumber} | ID: {self.Employee_id} | Position: {self.Position} | Salary: {self.Salary}"
