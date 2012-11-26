courseinfo = ('CME192', 'ICME', 2)

courseinfo[2] = 3 # error!

print courseinfo[2] # prints '2'

# unpacking
course, department, lecture = courseinfo
print course # prints 'CME192'
