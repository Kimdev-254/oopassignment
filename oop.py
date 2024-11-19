# Parent class for all vehicles
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print(f"{self.brand} {self.model}'s engine is starting...")
    
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def move(self):
        print(f"{self.brand} {self.model} is driving on the road")
    
    def honk(self):
        print("Beep beep!")

class Plane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude
    
    def move(self):
        print(f"✈️ {self.brand} {self.model} is flying in the sky")
    
    def take_off(self):
        print("Preparing for take-off!")

class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)
        self.boat_type = boat_type
    
    def move(self):
        print(f"{self.brand} {self.model} is sailing on the water")
    
    def anchor(self):
        print("Dropping anchor!")

def demonstrate_vehicles():
    print("🚦 Vehicle Polymorphism Demonstration 🚦")
    
    # Create different vehicles
    toyota_car = Car("Toyota", "Camry", 2022, 4)
    boeing_plane = Plane("Boeing", "747", 2020, 40000)
    yacht = Boat("Luxury Yachts", "Ocean Breeze", 2023, "Yacht")
    

    vehicles = [toyota_car, boeing_plane, yacht]
    
    for vehicle in vehicles:
        vehicle.start_engine()
        vehicle.move()
        print("---")

if __name__ == "__main__":
    demonstrate_vehicles()