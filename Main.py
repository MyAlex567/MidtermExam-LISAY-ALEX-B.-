from CarClasses.Employee import Employee
from CarClasses.Manager import Manager
from CarClasses.Supplier import Supplier
from CarClasses.Car import Car
from CarClasses.Inventory import Inventory

def RedLine():
    print("\033[31m-------------------------------------------------------------------------------------------------------------\033[0m")

def GreenLine():
    print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")

def DisplayList(List):
    for data in List:
        print(data)

def DisplayEmployees(List):
    for data in List:
        print(f"Name: {data.name} | ID: {data.Employee_id}")

def UserIdentity():
    temp = ""
    while True:
        print()
        enter = str(input("Enter Your Role (\033[38;5;208mManager\033[0m | \033[36mSupplier\033[0m): "))

        if enter.lower() == "manager":
            temp = "manager"
            break
        elif enter.lower() == "supplier":
            temp = "supplier"
            break
        else:
            print("Invalid Input Please Try Again")
    return temp

def CheckManagerId(Manager):
    attempt = 3
    check = False

    while True:
        try:
            InputId = int(input("\033[32mPlease Enter Your ID:\033[0m "))
            if InputId == Manager.Employee_id:
                check = True
                break
            else:
                attempt-=1
                print(f"\033[31mWrong ID Please Try Again\033[0m (Current remaining Attempt {attempt})")
                if attempt == 0:
                    break
        except:
                attempt-=1
                print(f"\033[31mInvalid Input\033[0m (Current remaining Attempt {attempt})")
                if attempt == 0:
                    break
    
    return check

def InputUserChoice():
    rest = None

    while True:
        enter = input("Enter Your Choice: ")
        if enter.isdigit():
            rest = enter
            break
        else:
            print("Invalid Input Please Try Again")

    return int(rest)

def isStr(askingInput):
    temp = ""
    while True:
        userInput = input(f"Please Enter the {askingInput}: ")

        if isinstance(userInput, str):
            temp = userInput
            break
        else:
            print("Invalid Input Please Try Again")
    return temp

def isInt(askingInput):
    temp = 0
    while True:
        userInput = int(input(f"Please Enter the {askingInput}: "))

        if isinstance(userInput, int):
            temp = userInput
            break
        else:
            print("Invalid Input Please Try Again")
    return temp

InventoryList = [
    Car("Toyota", "Vios", 2022, 950000, "In stock", "Silver"),
    Car("Honda", "Civic", 2023, 1500000, "Out of Stock", "Red"),
    Car("Mitsubishi", "Xpander", 2021, 1100000, "In stock", "White")
    ]

Employeers = [
    Employee("Steve Job", 28, 9462918849, 102, "Mechanic", 25000),
    Employee("John Smith", 28, 96745324561, 103, "Sales Assistant", 20000),
    Employee("Emily Johnson", 33, 99765442319, 104, "Cashier", 21000)
]

SupplierCarList = [
    Car("Ford", "Ranger XLT", 2024, 1650000, "Sold Out", "Black")
]
Supplier1 = Supplier("Carlos Forteza", 38, 9878234567, "AutoParts Philippines", "Cars", SupplierCarList)

newManager = Manager("James Webs", 35, 9171234567, 101, "Operations Manager", 65000, "AutoPrime Motors", "Car Units", SupplierCarList)
newInventory = Inventory(InventoryList)

while True:
    newInventory.DisplayAllCar()
    User = UserIdentity()

    if User == "manager":
        IdManager = CheckManagerId(newManager)

        while True:
            if IdManager:
                RedLine()
                print("\033[38;5;208m                                           MANAGER DASHBOARD\033[0m")
                print("1. Remove a Car")
                print("2. Add a Car")
                print("3. View Supplier Stock")
                print("4. View Employess")
                print("5. Exit")
                Mchoice = InputUserChoice()
                
                match Mchoice:
                    case 1:
                        RedLine()
                        newInventory.RemoveCar()
                        RedLine()
                        newInventory.DisplayAllCar()
                    case 2:
                        RedLine()
                        Supplier1.DisplayStock()
                        RedLine()
                        while True:

                            try:
                                add = int(input("Enter the Code of the Car You want to Add: "))
                                RedLine()
                                print(Supplier1.CarStock[add])
                                RedLine()
                                Confirmation = input("Are You Sure You Want to Add this Car? (Y/N): ")
                                
                                if Confirmation.lower() == "y":
                                    newInventory + Supplier1.CarStock[add]
                                    newInventory.DisplayAllCar()
                                    askUser = input("Add another Car? (Y/N): ")
                                    if askUser.lower() == "y":
                                        continue
                                    else: 
                                        break
                                else:
                                    print("Cancelled")
                            except:
                                print("Invalid Input")
                    case 3:
                        RedLine()
                        print("\033[38;5;208m                                             SUPPLIER STOCK\033[0m")
                        RedLine()
                        DisplayList(SupplierCarList)
                        RedLine()
                    case 4:
                        
                        while True:

                            try:
                                RedLine()
                                print("\033[38;5;208m                                           EMPLOYEES DASHBOARD\033[0m")
                                RedLine()

                                try:
                                    RedLine()
                                    DisplayEmployees(Employeers)
                                    RedLine()
                                    toViewEmployeeData = int(input("Enter Employee's ID to view (0 - exit): "))


                                    if toViewEmployeeData == 0:
                                        break
                                    else:
                                        for em in Employeers:
                                            if em.Employee_id == toViewEmployeeData:
                                                GreenLine()
                                                print("                                    PERSONAL INFORMATION")
                                                print()
                                                print(em)
                                                GreenLine()
                                                break
                                        else:
                                            print("\033[31mInvalid Employee's ID Try Again\033[0m")
                                    askAgain = input("View Another Employee's? (Y/N): ")
                                    if askAgain.lower() == "y":
                                        continue
                                    else:
                                        break
                                except:
                                    print("Invalid Input")
                            except:
                                print("Invalid Input")
                    case 5:
                        break
                    case _:
                        print("\033[31mInvalid Choice\033[0m")
            else:
                print("Wrong Id Please Try Again Later")
                continue
    elif User == "supplier":

        while True:
            try:
                RedLine()
                print("\033[38;5;208m                                           CURRENT STOCK\033[0m")
                RedLine()
                Supplier1.DisplayStock()
                RedLine()
                print("1. Add Car Stock")
                print("2. Exit")
                toDo = int(input("Enter Your Choice: "))

                match toDo:
                    case 1:
                        carBrand = isStr("Brand")
                        carModel = isStr("Model")
                        carYear = isInt("Year")
                        carPrice = isInt("Price")
                        carAvail = isStr("Availability")
                        carColor = isStr("Color")

                        while True:
                            check = input("Are you Sure You Want to add this Car? (Y/N): ")
                            if check.lower() == "y":
                                Supplier1 + Car(carBrand, carModel, carYear, carPrice, carAvail, carColor)
                                print("\033[38;5;208m                                           CURRENT STOCK\033[0m")
                                RedLine()
                                Supplier1.DisplayStock()
                                RedLine()
                                break
                            else:
                                print("Adding Car Cancelled")
                    case _:
                        break 
            except ValueError as E:
                print(E)
                continue






