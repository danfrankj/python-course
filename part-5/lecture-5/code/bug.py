import numpy as np

def some_buggy_function():
    A = np.arange(1, 10)
    #import ipdb; ipdb.set_trace() # BREAKPOINT
    # n (next)
    # ENTER (repeat previous)
    # q (quit)
    # p variable (print value)
    # c (continue)
    # unt (continue until the next line is reacheds)
    # l (list where you are)
    # s (step into subroutine)
    # r (continue till the end of the subroutine)
    # plus anything you can normally do at a python terminal
    
    B
    # A.a_doesnothavethismehtod()
    #A /= 2. # A = A / 2.
    A = A / 2.
    
    output = np.sum(5 / A)
    return output


def some_not_buggy_function():
	a = 0
	import ipdb; ipdb.set_trace()
	for i in xrange(1000):
		# use unt to get past
		a += 1
	some_buggy_function()
	print 'made it past the bug'
	return None
