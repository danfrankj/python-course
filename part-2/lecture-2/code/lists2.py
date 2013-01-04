arr = [2, 4, 6, 8]

print arr[0:2] # prints [2, 4]
arr[1:3] = [7, 7] # arr is now [2, 7, 7, 8]
print arr[2:] # prints [7, 8]

arr *= 2
print arr[3:6] # prints [8, 2, 7]
