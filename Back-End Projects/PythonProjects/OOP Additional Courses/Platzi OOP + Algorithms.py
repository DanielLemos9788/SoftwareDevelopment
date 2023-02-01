"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce_itself(self, other_person_name):
        print(f"Hi {other_person_name}, my name is {self.name}")

jon_snow = Person("Jon Snow", 38)
jon_snow.introduce_itself("Margott")

class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self,another_dir):
        x_diff = (self.x - another_dir.x)**2
        y_diff = (self.y - another_dir.y)**2

        return (x_diff + y_diff **0.5)

dir_1 = Direction(10,20)
dir_2 = Direction(0,0)
print(dir_1.distance(dir_2))
"""
"""
class Car:
    def __int__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = solor
        self.status = "Still"
        self.engine = Engine(horse_power=250)
    def accelerate(self, type="slow"):
        if type == "fast":
            self.engine.pump_gas(20)
        elif type == "slow":
            self.engine.pump_gas(5)

        self.status = "Moving"


class Engine:
    def __init__(self,horse_power,type="Gasoline"):
        self.horse_power = horse_power
        self.type = type
    def pump_gas(self, amount):
        pass
"""
"""
class WashingMachine:
    def __init__(self):
        pass
    def wash(self, temperature = "hot"):
        self._fill_tank(temperature)
        self._add_soap()
        self._wash()
        self._spin_dry()
    def _fill_tank(self, temperature):
        print(f"Filling the tank with {temperature} water")
    def _add_soap(self):
        print("Adding soap")
    def _wash(self):
        print("Washing")
    def _spin_dry(self):
        print("Centrifuging")


nexun = WashingMachine()
nexun.wash("hot")

"""
"""
class Miles():
    def __init__(self, distance=0):
        self.distance = distance
    def to_km(self):
        return (self.distance * 1.609344)
    #Getter Method
    def get_distance(self):
        return self.distance
    #Setter Method
    def define_distance(self, value):
        if value < 0:
            raise ValueError("The distance cannot be a negative number")
        self.distance = value
    #Delete Method
    def delete_distance(self):
        del self.distance


airplane = Miles(20)

print(airplane.distance)
print(airplane.to_km())
print(airplane.get_distance())
print(airplane.define_distance(150))
print(airplane.get_distance())
print(airplane.delete_distance())
"""



