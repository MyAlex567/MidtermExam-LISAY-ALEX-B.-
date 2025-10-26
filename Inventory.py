from CarClasses.Car import Car

class Inventory:
    def __init__(self, CarList):
        self.CarList = CarList

    def UpdatatingCar(self):
        for data in self.CarList:
            print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
            print(f"Code: ({self.CarList.index(data)})")
            print(data)
        print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")

    def DisplayAllCar(self):
        print()
        print("\033[31m-------------------------------------------------------------------------------------------------------------\033[0m")
        print("                                              CARS INFORMATION")
        print("\033[31m-------------------------------------------------------------------------------------------------------------\033[0m")
        self.UpdatatingCar()
        print("\033[31m-------------------------------------------------------------------------------------------------------------\033[0m")

    def RemoveCar(self):

        while True:
                try:
                    while True:
                        print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                        print("                                            CURRENT CAR STOCK")
                        print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                        self.UpdatatingCar()
                        Code = int(input("Enter the code: "))
                        print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                        print(self.CarList[Code])
                        print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                        Confirmation = str(input("Are you Sure You Want to Remove this Car? (Y/N): "))
                        print()
                        if Confirmation.lower() == "y":
                            print("Succesfully Remove the Car")
                            del self.CarList[Code]
                            print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                            print("                                            UPDATED LIST")
                            print("\033[32m-------------------------------------------------------------------------------------------------------------\033[0m")
                            self.UpdatatingCar()
                            ask = str(input("Remove A car Again? (Y/N): "))
                            if ask.lower() == "y":
                                continue
                            else:
                                break
                        else:
                            print("Removing Car Canceled")
                            break
                    break
                except:
                    print("Invalid Code")

    def __add__(self, other):
        self.CarList.append(other)
        return self
        
