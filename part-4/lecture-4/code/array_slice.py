arr = np.arange(20).reshape((4, 5))

# slicing (like lists for each dimension)
arr[0:4, 3:5]  # all rows and last two columns
arr[:4,  3:5]  # equivalent - can leave off start if 0
arr[:, 3:]     # equivalent - can leave off end if size of axis
arr[slice(None), slice(3, None)]  # equivalent - can use slice()

# integer indices
arr[[1, 2], :]  # rows one and two, all columns
arr[np.array([1, 2]), :]  # equivalent
arr[[1, 2], [1, 2, 3]] # ERROR

# boolean indices
arr[np.array([False, True, True, False]), :]  # equivalent
arr[[False, True, True, False], :]  
# NOT equivalent - boolean treated as 1, 0
