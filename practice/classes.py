class Bike:
    def __init__(self, color, frame):
        self.color = color
        self.frame = frame 

    def brake(self):
        print("braking")


dugatti = Bike("red", "titanium")          

print(dugatti.color)
print(dugatti.brake())