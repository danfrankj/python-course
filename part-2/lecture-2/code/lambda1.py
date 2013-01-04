def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def operate(f, y):
    return f(y)

print operate(square, 4) # prints '16'
print operate(cube, 4) # prints '64'
