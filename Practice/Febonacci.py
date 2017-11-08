#!/usr/bin/python3

# Write a simple Febonacci series in python

class Febonacci():
    ''' This is the doc string help us to give information about the
    class methods and functions. Lets start the Febonacci series writing
    functions def'''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
f = Febonacci(61, 61)
for number in f.series():
   if number > 60: break
   print (number, end= '   ')
