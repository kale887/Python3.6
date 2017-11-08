#!/usr/bin/python3
# range object is not inclusive

def isprime(n):
    if n == 1:
        return False
    for x in range(3, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
   while(True):
       if isprime(n): yield n
       n += 1

for n in primes():
    if n > 25: break
    print(n)

# yield returns each time the next item in iteration
# range start stop step
def main():
    print("This is function for range file")
    for i in inclusive_range():
        print(i, end = ' ')
def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least on argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive range expected at most 3 arguments, {}'.format(numargs))
    i = start
    while i <= stop:
         yield i
         i += step

if __name__ == '__main__':
    main()
    # turns function into generator, function is called :
#each time yield is run it returns object and if condition is true, execution picks up right after the yield and this turns the function into generator,
#which can be used as iteratir object
