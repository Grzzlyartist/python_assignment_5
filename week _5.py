class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, brand, model, year, max_speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self._mileage = 0  # Encapsulated attribute
    
    def move(self):
        """Base move method - should be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement move() method")
    
    def get_mileage(self):
        """Getter method for encapsulated attribute"""
        return self._mileage
    
    def add_mileage(self, distance):
        """Method to update mileage with validation"""
        if distance > 0:
            self._mileage += distance
        else:
            print("Distance must be positive!")
    
    def display_info(self):
        """Display vehicle information"""
        return f"{self.year} {self.brand} {self.model} | Max Speed: {self.max_speed} km/h | Mileage: {self._mileage} km"


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, max_speed, fuel_type, doors):
        super().__init__(brand, model, year, max_speed)
        self.fuel_type = fuel_type
        self.doors = doors
        self._engine_status = "off"  # Encapsulated
    
    def move(self):
        """Polymorphic implementation for Car"""
        return "Driving 🚗"
    
    def start_engine(self):
        """Car-specific method"""
        self._engine_status = "on"
        return "Engine started! Vroom vroom! 🏁"
    
    def stop_engine(self):
        """Car-specific method"""
        self._engine_status = "off"
        return "Engine stopped ⛔"
    
    def get_engine_status(self):
        """Getter for encapsulated engine status"""
        return self._engine_status


class Airplane(Vehicle):
    """Airplane class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, max_speed, wingspan, capacity):
        super().__init__(brand, model, year, max_speed)
        self.wingspan = wingspan
        self.capacity = capacity
        self._altitude = 0  # Encapsulated
    
    def move(self):
        """Polymorphic implementation for Airplane"""
        return "Flying ✈️"
    
    def take_off(self):
        """Airplane-specific method"""
        self._altitude = 10000
        return "Taking off! 🛫"
    
    def land(self):
        """Airplane-specific method"""
        self._altitude = 0
        return "Landing! 🛬"
    
    def get_altitude(self):
        """Getter for encapsulated altitude"""
        return f"{self._altitude} feet"


class Boat(Vehicle):
    """Boat class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, max_speed, boat_type, displacement):
        super().__init__(brand, model, year, max_speed)
        self.boat_type = boat_type
        self.displacement = displacement
        self._is_docked = True  # Encapsulated
    
    def move(self):
        """Polymorphic implementation for Boat"""
        return "Sailing ⛵"
    
    def dock(self):
        """Boat-specific method"""
        self._is_docked = True
        return "Docked at the harbor! ⚓"
    
    def set_sail(self):
        """Boat-specific method"""
        self._is_docked = False
        return "Setting sail! 🌊"
    
    def is_docked(self):
        """Getter for dock status"""
        return self._is_docked


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle"""
    
    def __init__(self, brand, model, year, max_speed, engine_size, bike_type):
        super().__init__(brand, model, year, max_speed)
        self.engine_size = engine_size
        self.bike_type = bike_type
        self._is_standing = False  # Encapsulated
    
    def move(self):
        """Polymorphic implementation for Motorcycle"""
        return "Riding 🏍️"
    
    def do_wheelie(self):
        """Motorcycle-specific method"""
        self._is_standing = True
        return "Doing a wheelie! 🤘"
    
    def land_wheelie(self):
        """Motorcycle-specific method"""
        self._is_standing = False
        return "Wheelie landed! 👍"


# Demonstration of polymorphism and inheritance
def demonstrate_vehicles():
    """Function to demonstrate all vehicle types and their polymorphic behavior"""
    
    # Create different vehicle objects
    vehicles = [
        Car("Toyota", "Camry", 2023, 180, "Gasoline", 4),
        Airplane("Boeing", "737", 2020, 946, 35.8, 215),
        Boat("Beneteau", "Oceanis", 2022, 25, "Sailboat", 12000),
        Motorcycle("Harley-Davidson", "Sportster", 2023, 180, 1200, "Cruiser")
    ]
    
    print("🚗 VEHICLE POLYMORPHISM DEMONSTRATION 🚗")
    print("=" * 50)
    
    # Demonstrate polymorphic move() method
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")
        print(vehicle.display_info())
        
        # Add some mileage to each vehicle
        vehicle.add_mileage(150)
        print(f"Added 150 km: New mileage: {vehicle.get_mileage()} km")
        
        # Demonstrate class-specific methods
        if isinstance(vehicle, Car):
            print(vehicle.start_engine())
        elif isinstance(vehicle, Airplane):
            print(vehicle.take_off())
        elif isinstance(vehicle, Boat):
            print(vehicle.set_sail())
        elif isinstance(vehicle, Motorcycle):
            print(vehicle.do_wheelie())
        
        print("-" * 30)
    
    # Additional demonstration of encapsulation
    print("\n🔒 ENCAPSULATION DEMONSTRATION 🔒")
    print("=" * 40)
    
    my_car = Car("Tesla", "Model S", 2023, 250, "Electric", 4)
    print(f"Car engine status: {my_car.get_engine_status()}")
    print(my_car.start_engine())
    print(f"Car engine status: {my_car.get_engine_status()}")
    
    # Try to access encapsulated attribute directly (will work but should be avoided)
    print(f"Direct access (not recommended): {my_car._engine_status}")


# Run the demonstration
if __name__ == "__main__":
    demonstrate_vehicles()