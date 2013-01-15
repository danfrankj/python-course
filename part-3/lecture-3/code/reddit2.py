from reddit_data import *

with open('reddit2.txt', 'w') as f:
  for i, point in enumerate(data):
    data = 'Post #%d\n' % i
    data += '\t%s\n' % point['title'][0:20]
    data += '\t\t%s (%d)\n' % (point['sub'],
                               point['comments'])
    f.write(data)

