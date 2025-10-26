class Car:
    def __init__(self, Brand, Model, Year, Price, Availability, Color):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Availability = Availability
        self.Color = Color
    
    def __str__(self):
        return f"\033[38;5;208mBrand: {self.Brand}\033[0m | Model: {self.Model} | Year: {self.Year} | Price: \033[32m{self.Price}\033[0m | Availabilit: {self.Availability} | Color: {self.Color}"