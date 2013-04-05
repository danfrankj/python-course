import math

p = (1.2, -40.0, 2*math.pi)

# Create dictionary with keys
point = {'x': p[0], 'y': p[1], 'z': p[2],
         'r': math.sqrt(sum([v ** 2 for v in p]))}
point['theta'] = math.acos(point['z'] / point['r'])
point['phi'] = math.atan(point['y'] / point['x'])
