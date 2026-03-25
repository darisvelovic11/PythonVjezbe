class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self , temp):
        if temp >= -2713.15:
            self._celsius=temp 
        else:
           print("Temp cannot be that low!") 
    @property
    def fahrenheit(self):
        return (self._celsius* 9/5)+32
    
    @staticmethod 
    def is_freezing(celsius):
        return celsius<=0
    
    @classmethod
    def from_fahrenheit(cls, f):
        celsius= (f - 32) * 5/9
        return cls(celsius)
t1 = Temperature(100)
print(t1.celsius)        # 100
print(t1.fahrenheit)     # 212.0

t2 = Temperature.from_fahrenheit(32)
print(t2.celsius)        # 0.0

print(Temperature.is_freezing(-5))   # True
print(Temperature.is_freezing(20))   # False

t1.celsius = -300        # should print a rejection message
