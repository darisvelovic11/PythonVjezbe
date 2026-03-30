class Circle():
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def get_radius(self, radius):
        if self._radius>=0:
            print("Radius must be bigger than 0")
        else:
             self._radius = radius

    @property
    def area(self):
        return 3.14*self._radius**2
    
    @staticmethod
    def compare(r1, r2):
        if r1 > r2:
            return f"first"
        elif r1 < r2:
            return f"second"
        else:
            return f"equal"
        
c = Circle(10)