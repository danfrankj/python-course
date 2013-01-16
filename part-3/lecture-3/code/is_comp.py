arr1 = [9, 7, 5, 3]
arr2 = arr1
arr3 = [9, 7, 5, 3]

print arr1 == arr2 and arr1 is arr2 # True
print arr1 == arr3 # True
print arr1 is arr3 # False
