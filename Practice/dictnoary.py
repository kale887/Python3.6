import operator
from operator import itemgetter
bucket = {}
ice = {}


ice.update({'raw 1': 'ice bucket challange'})
ice['raw 1']
print(ice['raw 1'])
bucket['item 1'] = 'sugar'
bucket.update({'item 2': 'ice cream', 'item 3': 'soda', 'item 4': 'lemons'})
# item returns a sequence of tuples
# tuple unpacking 
for key, value in bucket.items():
    print (bucket)
newlist = sorted(ice.items(),key=operator.itemgetter(0))
print(newlist)