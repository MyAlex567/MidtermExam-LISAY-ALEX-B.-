from CarClasses.Person import Person

class Supplier(Person):
    def __init__(self, name, age, contactNumber, Company_name, Supply_type, CarsStock):
        Person.__init__(self, name, age, contactNumber)
        self.Company_name = Company_name
        self.Supply_type = Supply_type 
        self.CarStock = CarsStock

    def DisplayStock(self):
        for stock in self.CarStock:
            print(f"Code: ({self.CarStock.index(stock)})")
            print(stock)

    def __add__(self, other):
        self.CarStock.append(other)
        return self
