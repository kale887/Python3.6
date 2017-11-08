# List can be loop over collection and multiple collections.
# we can use if statements to put conditions on the lists

# List = [1,2,3,4,"abc",3.14]
#
# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test1> and <test2>]
# [expr for val1 in collection1 and val2 in collection2]
#
# Examples : List of square of fist 100 postive integer

squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)
"""this is something cool"""

squares2 = [i**2 for i in range(1, 101)] # complex list comp in single line
