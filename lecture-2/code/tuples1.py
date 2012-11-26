p1 = ('start', 1.2, -3.0, 17.222)
p2 = ('end', -7.3, 0.0, -0.0001)

p1[3] = 17.2 # error!

print p2[2] # prints '0.0'

# unpacking
type1, x1, y1, z1 = p1
type2, x2, y2, z2 = p2

print x1 - x2 # prints '8.5'
