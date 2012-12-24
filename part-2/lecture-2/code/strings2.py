vec = '[12.4, 3, 4, 7.22]'

# strip away the brackets
vec = vec.lstrip('[')
vec = vec.rstrip(']')

# form an array by splitting on comma
nums = vec.split(',')

# go from string to floating point
nums = [float(n) for n in nums]


