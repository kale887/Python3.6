import json
import requests
from pprint import pprint


"""url = 'https://api.foursquare.com/v2/venues/explore'
    Foursquare API Endpoint to explore the venues
    pprint nice way to print json from python objects, 
    request helps to re-direct URL's """

url = 'https://api.foursquare.com/v2/venues/search'


params = dict(
    client_id='RAY02SGAJWPT41O5VJB0421YPQ0MGFYKFNTSJDES4KWVF5UN',
    client_secret='BN0K1CJ24WT3BBOYE2JYO5JSIHMZHENAXUNJPZGGANZ4MQ0K',
    v='20170801',
    ll='37.392971,-122.076044',
    query='Salad',
    address='Mountain View, California'
)
"""Note: use json.loads instead of json.load. In Python 3, 
json.loads takes a string parameter. json.load takes a file-like object parameter.
 data_file.read() returns a string object."""

resp = requests.get(url=url, params=params)
data = resp.json()
# pp = pprint.PrettyPrinter(indent=3)
pprint(data)
"""Function to pretty print JSON if its a string or dict

  def pp_json(json_thing, sort=True, indents=2):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None
google_api_key = "AIzaSyA_E6CJ_c7aq7sW_jvtF0wtDJ9ffUivqmM"
pp_json(data)"""