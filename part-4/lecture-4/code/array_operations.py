arr1 = np.arange(10).reshape((2, 5))
arr2 = np.random.random((2, 5))

# elementwise for basic and boolean operations
#   +, -, *, /, **, np.log, <, >=, ==
#   arrays are upcast, resulting in float or boolean arrays
arr1 + arr2  # elementwise sum
arr1 == arr2  # elementwise equality

# operations in place
arr1 += arr2

# matrix product
np.dot(arr1, arr2)

# similarly numpy ufunc's operate elementwise
np.sin(arr1)
np.sqrt(arr1)