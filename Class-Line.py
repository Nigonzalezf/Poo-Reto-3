import math
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)
    
    def compute_slope(self):
         return degrees(atan2(abs(self.end.y - self.start.y), abs(self.end.x-self.start.x)))
    
    def compute_vertical_cross(self):
        if self.start.x > 0 and self.end.x < 0 or self.start.x < 0 and self.end.x > 0:
            print("Corta con el eje y")
        else:
            print("No corta con el eje y")

    def compute_horizontal_cross(self):
        if self.start.y > 0 and self.end.y < 0 or self.start.y < 0 and self.end.y > 0:
            print("Corta con el eje x")
        else:
            print("No corta con el eje x")


class Rectangle:
    def __init__(self, line1, line2, line3, line4):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4   

    def compute_area(self):
        return ((self.line1.end.y - self.line1.start.x) * (self.line3.end.y - self.line3.x))

    def compute_perimeter(self):
        return 2 * ((self.line1.end.y - self.line1.start.x) * (self.line3.end.y - self.line3.x))    
