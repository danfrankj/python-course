import math
# first 20 k-digit approximations of pi
approximations = []
i = 1
while i <= 20:
  approx = round(math.pi, i)
  approximations.append(approx)
  i += 1


