def integer_generator(maxval=float('inf')):
    # generate integers up to maxval
    i = 0
    while i < maxval:
        yield i
        i += 1