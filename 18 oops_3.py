class vehical():
    def __init__(self,name,vehicalType,speed,milage,capacity) -> None:
        self.name = name
        self.vehicalType = vehicalType
        self.speed = speed
        self.milage = milage
        self.capacity = capacity
    
    def carInfo(self):
        return print(f'Vehical Name: {self.name}\nvehical Type: {self.vehicalType}\nThe speed is: {self.speed}\nThe mileage is: {self.milage}\ncapacity: {self.capacity}')

    
class bus(vehical):
    pass

school_bus = bus("VOLVO","Bus" ,"50km/hour", "100km/hour",70)
car =vehical("VERNA","Car(sedan)","210km/hour","20km/Litres",5)

print("\t\t\t\tPYTHON TOURS AND TRAVELS")

a = input("enter vehical name: ")
if a == "car":
    car.carInfo()
elif a == "school_bus":
    school_bus.carInfo()


