# Activity 1
# Constructor
class smartphone:
    def __init__(self, ram, rom, battery):
        self.ram = ram
        self.rom = rom
        if battery < 0:
            print("Your phone battery cannot be negative")
            self.battery = 0
        elif battery > 100:
            print("Your phone battery cannot be greater than 100")
            self.battery = 100
        else:
            self.battery = battery
    def recharge(pcnt):
        if pcnt < 0 | pcnt > 100:
            print(f"{pcnt} is not valid charging percentage!")
        elif self.battery + pcnt > 100:
            print("You cannot charge battery beyond 100%")
            self.battery = 100
        else:
            self.battery += pcnt

myphone = smartphone(8, 256, 50)
myphone.battery

# Inheritance
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}. My power is {self.power}.")

    def fight(self):
        print(f"{self.name} fights crime using {self.power}!")

# Inheritance + Polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fight(self):
        # Polymorphism: overrides fight()
        print(f"{self.name} zooms through the sky at {self.flight_speed} km/h and defeats villains with {self.power}!")


hero1 = Superhero("Shadow Ninja", "Invisibility", "Tokyo")
hero2 = FlyingSuperhero("Sky Falcon", "Wind Blades", "Cloud City", 500)

hero1.introduce()
hero1.fight()

hero2.introduce()
hero2.fight()

# Activity 2
class Vehicle:
    def move(self):
        print("This vehicle moves.")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
