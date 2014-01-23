arr = np.random.random((2, 5))

arr.sum() # sum of all elements in array 
np.sum(arr) # equivalent
np.sum(arr, axis=0) # column sum
np.sum(arr, axis=1) # row sum

np.apply_along_axis(np.sum, 0, arr) # column sum

arr3d = np.random.random((2, 3, 4))
np.sum(arr3d, axis=2) # returns a (2, 3) array