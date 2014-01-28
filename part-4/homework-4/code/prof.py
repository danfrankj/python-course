import timeit
import numpy as np

# Compute the first 50 powers of two starting at 0 and exclusive of 50
# for each function return the same list which should have length 50
# the main method at the end shows you how to run these tests so you can 
# see the difference in how long they take

def empty_list():
    # append  to an initially empty list 
    return []

def preallocated_list():
    # create an list of zeros of size 50 and assign elements sequentially 
    return [] 

def lst_comp():
    # use a list comprehension
    return []

def map_twos():
    # use the python map function in
    return []

def twos_numpy():
    # use vectorization (NumPy)
    return []


def main():
    N = 100000
    print 'empty_list() took %f seconds' % timeit.timeit('empty_list()', 
        setup = 'from prof import empty_list', number=N)
    print 'preallocated_list() took %f seconds' % timeit.timeit('preallocated_list()', 
        setup = 'from prof import preallocated_list', number=N)
    print 'lst_comp() took %f seconds' % timeit.timeit('lst_comp()', 
        setup = 'from prof import lst_comp', number=N)
    print 'map_twos() took %f seconds' % timeit.timeit('map_twos()', 
        setup = 'from prof import map_twos', number=N)
    print 'twos_numpy() took %f seconds' % timeit.timeit('twos_numpy()', 
        setup = 'from prof import twos_numpy', number=N)

if __name__ == "__main__":
    import sys
    sys.exit(main())
