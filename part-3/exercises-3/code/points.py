import math

class CartPoint:
  def __init__(self, coords):
    self.x, self.y, self.z = coords
  
  def magnitude(self):
    return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

p1 = CartPoint((1, 1, 0))
print p1.magnitude()

class CartPointTime(CartPoint):
  def __init__(self, coords):
    CartPoint.__init__(self, (coords[0], coords[1], coords[2]))
    self.t = coords[3]

  def magnitude_and_time(self):
    return (self.magnitude(), self.t)

p2 = CartPointTime((1, 1, 0, 0.5))
print p2.magnitude_and_time()
