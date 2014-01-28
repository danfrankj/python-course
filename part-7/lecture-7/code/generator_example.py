from integer_generator import integer_generator

gen = integer_generator(2)
for i in gen:  # prints 0, 1
    print i

gen = integer_generator(2)
print gen.next()  # prints 0
print gen.next()  # prints 1
print gen.next()  # StopIteration error

gen = integer_generator()
for i in gen:
    # never terminates... prints all integers
    print i
