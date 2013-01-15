from reddit_data import *

with open('reddit1.txt', 'w') as f:
    for point in data:
        f.write(str(point) + '\n')

