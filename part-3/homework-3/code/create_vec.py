import random

n = 1000
for name in ['a.txt', 'b.txt']:
  with open(name, 'w') as f:
    for j in xrange(n):
      f.write('%f\n' % random.random())
