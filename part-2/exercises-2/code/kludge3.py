# Generate all (x, y, z) coordinates from three lists
xpoints = [1, 2, -1]
ypoints = [8, 4, 3, 0]
zpoints = [0, -1]
points = []
for x in xpoints:
  for y in ypoints:
    for z in zpoints:
      points.append((x, y, z))

