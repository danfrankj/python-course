def operate(f, y):
  return f(y)

print operate(lambda(x): x ** 2, 4) # prints '16'
print operate(lambda(x): x ** 3, 4) # prints '64'

square_plus_cube = lambda(x): x ** 2 + x ** 3
print operate(square_plus_cube, 4) # prints '80'
