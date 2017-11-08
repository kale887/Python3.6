from decimal import *
movies = ["Aditya Kale", "Aditya Kharbade", "Rishikesh Bhoyar", "Tom Cruise", "Zeng Tony", "Martin Rachel", "Ishana Raina"]

gmovies = []
for title in movies:
    if title.endswith("a"):
        gmovies.append(title)
print(gmovies)

## Easy loop using direct list comprehsions

gmovies2 = [ title for title in movies if title.startswith("A")]
print(gmovies2)

decimal = {}
width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")
