names = []

names.append({ 'first': 'Dam', 'last': 'yelo', 'suffix': '22'})
names.append({'fist': 'jane'})

for name in names:
    x = name.get('first')
    y = name.get('last')
    z = name.get('suffix')
    print(x,y,z)
    lelanddict = {
        "name": {
            "first": "Leland",
            "middle": "Dewitt",
            "last": "Stanford",
            "suffix": "Jr.",
            "title": "Mr."
        }
        "birth": {
            "date": 1868 - 05 - 14,
            "place": {
                "city": "Sacramento",
                "state": "California",
                "country": "United States"
            },
            "death": {
                "date": "1884-03-13",
                "place": {
                    "city": "Florence",
                    "country": "Italy"
                }
            }
        }
    }