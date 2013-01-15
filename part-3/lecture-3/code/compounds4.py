f = open('compounds.txt', 'r')
compounds = {}
for line in f:
    split_line = line.split(':')
    name = split_line[0]
    formula = split_line[1]
    formula = formula.strip()
    compounds[name] = formula

f.close()
