# multiplication by a scalar
arr = np.random.random((4, 5))
arr * 5  # multiply each element of the array by 5

# scales the first column by 0.
# scales the second column by 1., etc.
arr * np.arange(5)
