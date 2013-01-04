import math
x = 7.0
lower = 0.0
upper = x
guess = (upper + lower) / 2
while (math.fabs(x - guess * guess) > 0.1):
    if guess * guess > x:
        upper = guess
    else:
        lower = guess
    guess = (upper + lower) / 2
