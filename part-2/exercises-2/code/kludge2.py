import math
# first 14 k-digit approximations of pi
approximations = []
i = 1
while i <= 14:
  approx = round(math.pi, i)
  approximations.append(approx)
  i += 1


