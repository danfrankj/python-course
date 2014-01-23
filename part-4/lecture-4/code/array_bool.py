arr = np.arange(-100, 50)

arr[arr > 0] # extracts positive part of the array 

arr[arr > 0] = 0 # sets positive part of array to 0

# combined!
arr[arr > 0] = np.random.random_integers(low=0, 
                                         high=10,
                                         size=len(arr[arr > 0])) 
