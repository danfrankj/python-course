#  create an array, write to file, read from file
arr = np.array([[1, 2, 3], [4, 5, 6]])

#  save to a text file
#  creates a space delimited file by default
np.savetxt(fname='array_out.txt', X=arr)

#  load text file
loaded_arr = np.loadtxt(fname='array_out.txt')

np.all(arr == loaded_arr)  # True
