#!/usr/bin/python3

from collections import Counter
from random import randrange

myCounter = Counter()
for i in range(100):
    random_number = randrange(10)
    myCounter[random_number] += 1
for i in range(10):
    print(i, myCounter[i])
