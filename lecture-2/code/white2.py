vals1 = [1, 3, 5, 7, 9]
vals2 = [2, 4, 6, 8]

for v1 in vals1:
  for v2 in vals2:
    if not v1 % 3 and not v2 % 3:
      j = 0
      while(j < v1 + v2):
        print j
        j += 1
  print v1
