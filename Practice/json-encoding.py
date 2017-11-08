#!/usr/bin/python3
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

MyEncoder().encode()

def talk():

    # You can define a function on the fly in "talk" ...
    def whisper(word="yes"):
        return word.lower()+"..."

    # ... and use it right away!
    print(whisper())

# You call "talk", that defines "whisper" EVERY TIME you call it, then
# "whisper" is called in "talk".
talk()
# outputs:
# "yes..."

# But "whisper" DOES NOT EXIST outside "talk":
#you can assign function to variable like any other objects
cool = talk
print(cool())
try:
    print(whisper())
except NameError, e:
    print(e)
    #outputs : "name 'whisper' is not defined"*
    #Python's functions are objects
