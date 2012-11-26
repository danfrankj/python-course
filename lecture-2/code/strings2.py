str = '[12.4, 3, 4, 7.22]'
str2 = str.lstrip('[').rstrip(']')
nums = str2.split(',')
nums = [float(val) for val in nums]

# one-liner
nums = [float(val) for val in str.lstrip('[').rstrip(']').split(',')]
