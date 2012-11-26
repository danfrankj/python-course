# access
magnitude = point['r']
x = point['rho'] # error!

# overwrite
point['r'] = 5.13

# print all keys
for key in point:
  print key

# check if a key is there
if 'theta' not in point:
  print 'missing theta!'
