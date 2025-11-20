import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return str((self.x, self.y))
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def distance_from_origin(self):
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )