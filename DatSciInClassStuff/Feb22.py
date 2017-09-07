from __future__ import print_function


# Classes
class Rectangle:  # Can import Feb22 then access Feb22.Rectangle()
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self,):
        return self.h * self.w

    def __str__(self):
        return "Height: " + str(self.h) + ", Width: " + str(self.w)

r = Rectangle(10, 12)

print(r.area())
print(r.__str__())
