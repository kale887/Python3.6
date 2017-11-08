from collections import defaultdict
#The parameter to the defaultdict constructor is the function
# which will be called for building new elements. So let's use a lambda !
d = defaultdict(lambda : Counter())
# The argument to defaultdict needs to be callable and lambda is callable
#lamda returns lists
print(d)
