import httplib2
import json
from pprint import pprint

"""json in memory python objects to serilaize json representation"""


def get_geocode_location(input):
    api_key = "AIzaSyA_E6CJ_c7aq7sW_jvtF0wtDJ9ffUivqmM"
    location_string = input.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %
           (location_string, api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    print("response header: %s \n \n" % response)
    result = json.loads(content)
    pprint(result)
    return result

""" to run this function as module use import sys
    sys.path.append(/path/to/folder/) and then use file and module name
    example from geocode-api import get_geocode_location and use this function
    """
