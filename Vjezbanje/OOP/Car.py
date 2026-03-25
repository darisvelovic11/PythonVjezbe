class brm:
    def __init__(self,make,model,age,color):
        self.make = make
        self.model = model
        self.age = age
        self.color = color
    
    def drive(self):
        print(f"Car: {self.make} {self.model} is driving...")

    def stop(self):
        print(f"Car: {self.make} {self.model} turned off")