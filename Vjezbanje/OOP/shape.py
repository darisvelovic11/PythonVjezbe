class Shape ():
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__()
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius**2)*3.14
    
shapes = [Rectangle(4,3), Circle(2)]

for shape in shapes:
    print(shape.area())
        
    
