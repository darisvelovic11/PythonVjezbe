from abc import ABC, abstractmethod

class Shape (ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetar(self):
        pass
    
    @abstractmethod
    def describe(self):
        pass

    def summary(self):
        print(f"Shape: {self.describe()} | Color: {self.color} | Area: {self.area()} | Perimetar: {self.perimetar()}")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width=width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimetar(self):
        return 2*(self.width + self.height)
    def describe(self):
        return f"Rectangle (width={self.width}, height={self.height})"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    def perimetar(self):
        return 2*( 3.14 * self.radius)
    def describe(self):
        return f"Circle(radius={self.radius})"
    
class Triangle(Shape):
    def __init__(self, color,a,b,c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a +self.b + self.c) / 2
        area = (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5
        return area
    def perimetar(self):
        return self.a +self.b + self.c
    def describe(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
    
r = Rectangle("red", 5, 3)
c = Circle("blue", 7)
t = Triangle("green", 3, 4, 5)

shapes = [r, c, t]

for shape in shapes:
    shape.summary()

print("---")
biggest = max(shapes, key=lambda s: s.area())
print(f"Biggest shape: {biggest.describe()}")





