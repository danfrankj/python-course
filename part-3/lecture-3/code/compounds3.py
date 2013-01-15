f = open('compounds.txt', 'r')
for i, line in enumerate(f):
    print '(Line #' + str(i + 1) + ') ' + line
