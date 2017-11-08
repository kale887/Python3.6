# useful for counting (like a bag

# how import statements works in python :
# The import key words searches the packages in cache and look for previously imported stuff,
# step 2 is from statements which acts like finder in those packages and pulls up the modules
# nd then goes on to import the next identifier,
from collections import defaultdict
s = 'mississippiee'
d = defaultdict(list)
for k in s:
    d[k] = []
sorted(d.items())
print(d)
