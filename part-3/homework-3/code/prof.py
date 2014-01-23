import timeit
import numpy as np

# Compute the first 100 powers of two starting at 0 and exclusive of 100
# for each function return the same list which should have length 100
# the main method at the end shows you how to run these tests so you can 
# see the difference in how long they take

def empty_list():
    # append  to an initially empty list 
    return []

def preallocated_list():
    # create an list of zeros of size 100 and assign elements sequentially 
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
    N = 1000000
    print 'empty_list() took %f' % timeit.timeit('empty_list()', number=N)
    print 'preallocated_list() took %f' % timeit.timeit('preallocated_list()', number=N)
    print 'lst_comp() took %f' % timeit.timeit('lst_comp()', number=N)
    print 'map_twos() took %f' % timeit.timeit('empty_list()', number=N)
    print 'twos_numpy() took %f' % timeit.timeit('empty_list()', number=N)

if __name__ == "__main__":
    import sys
    sys.exit(main())
