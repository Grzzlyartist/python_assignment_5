# python_assignment_5
# Vehicle Polymorphism Demo 🚗✈️⛵🏍️

A Python program demonstrating object-oriented programming concepts with a vehicle class hierarchy!

## 🎯 Features

- **Inheritance** 📦: Base `Vehicle` class with specialized subclasses
- **Polymorphism** 🎭: Each vehicle implements `move()` differently
- **Encapsulation** 🔒: Protected attributes with getter methods
- **Constructors** 🏗️: Unique initialization for each vehicle type

## 🚀 Vehicle Types

- **Car** 🚗 - Drives on roads
- **Airplane** ✈️ - Flies in the sky  
- **Boat** ⛵ - Sails on water
- **Motorcycle** 🏍️ - Rides on two wheels

## 💻 Usage

```python
# Create vehicles
car = Car("Toyota", "Camry", 2023, 180, "Gasoline", 4)
plane = Airplane("Boeing", "737", 2020, 946, 35.8, 215)

# Polymorphic behavior
print(car.move())    # Output: Driving 🚗
print(plane.move())  # Output: Flying ✈️
