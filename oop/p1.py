# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def print_spmi(self):
        print("max_speed:",self.max_speed,"mileage:",self.mileage)
v1=Vehicle(100,50)
v1.print_spmi()