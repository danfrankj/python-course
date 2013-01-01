dict1 = {'apples': 3, 'oranges': 2}
dict2 = dict1
dict2['bananas'] = 5
if 'bananas' in dict1:
    print 'bananas is there!'
else:
    print 'no bananas'
