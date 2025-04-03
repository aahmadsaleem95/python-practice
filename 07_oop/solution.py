class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        # self.total_car +=1
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

# print(safari.total_car)
print(Car.total_car)

# my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.full_name())
# print(my_new_car.model)
# print(my_new_car.brand)