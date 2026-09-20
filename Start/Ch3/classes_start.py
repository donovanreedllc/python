# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class vehicle:
    def __init__(self, body_style):
        self.body_style = body_style
        
    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed

class car(vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 2
        self.engine = engine_type
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "car at", self.speed)

class motorcyle(vehicle):
    def __init__(self, engine_type, has_side_car):
        super().__init__("Motorcyle")
        
        if(has_side_car):
            self.wheels = 3
        else:
            self.wheels = 2
            
        self.doors = 0
        self.engine = engine_type   
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "motorcycle at", self.speed)    



car1 = car("Gas")
car2 = car("Electric")
mc1 = motorcyle("Gas", True)

print(mc1.wheels)
print(car1.engine)
print(car2.doors)

car1.drive(30)
car2.drive(55)
mc1.drive(70)

