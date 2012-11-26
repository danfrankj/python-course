arr = [2, 4, 6, 8]

print arr[3] # prints '8'
print arr[-1] # prints '8'

print arr[4] # error
arr.append(10)
print arr[4] # prints '10'

arr2 = [3, 5]
arr += arr2 # arr is now [2, 4, 6, 8, 10, 3, 5]

arr.pop() # removes 5
