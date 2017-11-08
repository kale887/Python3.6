#!/usr/bin/python3
from functools import reduce

list_sum = [[2, 55, 4], [5, 6], [7, 8], [9, 10]]
print(reduce(lambda x,y: x+y,list_sum))
