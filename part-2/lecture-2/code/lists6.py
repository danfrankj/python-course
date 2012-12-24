squares = [0, 1, 4, 9, 16, 25]

for i, val in enumerate(squares):
    print i, val

# cleaner and more concise than:
i = 0
for val in squares:
  print i, val
  i = i + 1

