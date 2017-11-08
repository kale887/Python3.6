#!/usr/bin/python
# most common type, iteration on objects
# def main():
#     fh = open('lines.txt')
#     for line in enumerate(fh):
#         print(line, end='')
#
# if __name__ == '__main__':
#     main()

# def main():
#      s = "I love the continue statement in python"
#      for i in enumerate(s):
#          if i == 't': continue
#          print(i, end='')


def main():
    p = "Movies are the best things to save time"
    count = 0
    while (count < len(p)):
        print(p[count], end='')
        count += 1
    else:
        print("cool")
if __name__ == '__main__':
    main()
