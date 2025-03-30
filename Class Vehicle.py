class Vehicle:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(358, 83)

print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)