compounds = {}
with open('compounds.txt', 'r') as f:
    for line in f:
        compounds[line.split(':')[0]] = \
          line.split(':')[1].strip()

