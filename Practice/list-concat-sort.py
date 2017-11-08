#!/usr/bin/python3

""" Concat or join 2 different list and make a new list without
 changing the copy of the original using + operator
  don't get confused with append() as it only adds item to the end of the lists
  ones with modification on original lists and sort lists """

shortList = [0, 11, 33, 21, 9]

longList = [4, 55, 61, 72]

concatList = shortList + longList

print(concatList)

shortList.sort()

list_sum = [[2, 55, 4], [5, 6], [7, 8], [9, 10]]

# use sum() to flatten the 2d lists

p = sum(list_sum, [])
print(p)

print([item for sublist in list_sum for item in sublist])

