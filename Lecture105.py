class Vehicle:
    LicenseCode = ""
    seriaCode = ""
    face = ""
    def turnONAirConditioner(self):
        print("Turn On : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass
car1 = Car()
car1.turnONAirConditioner()
car1.sayHello()

pickup1 = PickUp()
pickup1.turnONAirConditioner()

van1 = Van()
van1.turnONAirConditioner()

estatecar1 = EstateCar()
estatecar1.turnONAirConditioner()