class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day

    def display_details(self):
        print("VEHICLE ID: ", self.vehicle_id, "\nBRAND: ", self.brand, "\nRENT/DAY: ", self.rent_per_day, end="\n\n")

    def calculate_rent(self, days):
        return self.rent_per_day * days

vehicle1 = Vehicle(101, "Toyota", 11.5)
vehicle2 = Vehicle(102, "Suzuki", 7.5)

vehicle1.display_details()
vehicle2.display_details()

print("VEHICLE 1 | 9 DAYS: ", vehicle1.calculate_rent(9))
print("VEHICLE 2 | 3 DAYS: ", vehicle2.calculate_rent(3))
