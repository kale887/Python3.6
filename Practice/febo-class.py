#!/usr/bin/python3
class Febonacci():
    """docstring for Febonacci."""
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
f = Febonacci(0, 1)
for number in f.series():
    if number > 100: break
    print (number, end='   ')
