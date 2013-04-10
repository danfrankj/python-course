l = [2, 4, 6, 8]

print l[0:2] # prints [2, 4]
l[1:3] = [7, 7] # l is now [2, 7, 7, 8]
print l[2:] # prints [7, 8]

l *= 2
print l[3:6] # prints [8, 2, 7]
