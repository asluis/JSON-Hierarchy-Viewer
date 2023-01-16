import requests
import argparse

"""
This miniscript calls an API (which it expects will return JSON formatted data) and outputs the hierarchy of the JSON structure. No values are outputted, 
only the keys in the json are included in the hierarchy.
"""

parser = argparse.ArgumentParser()
parser.add_argument('--equalLists', dest='equal_lists', type=str, help='Determines whether all lists in the json object will have the same embedded JSON hierarchy. fetch,py will assume all lists are the same by default. To change this, specify any nonzero number to this parameter.')

args = parser.parse_args()
equal_lists = args.equal_lists or 0


api = "https://reddit.com/r/popular.json?sort=top"

""" Done so to change default user agent. Since none is defined, requests library uses its own,
which Reddit API interprets as one user for everyone trying to use default user agent and
rate limits it. User agent can be changed to anything."""
headers = {'User-agent': 'JSON_Hierarchy_Viewer/0.0.1'}

def get_data():
    response = requests.get(api, headers=headers)

    if response.status_code == 200:
        print("Successfully fetched some data.")
        return response.json()
    else:
        print(f"Error fetching data. Response code is {response.status_code}")
        return {"nothing":"nothing"}


def simple_print(data, indents):
    if not isinstance(data, (list, dict)):
        return
     
    out = ""
    for _ in range(0, indents):
         out = out + "  "

    if type(data) is dict:
       for k in data:
            layer = out + k
            print(layer)

            simple_print(data[k], indents + 1)
    else:
        for val in data:
            if type(val) is dict:
                simple_print(data[0], indents + 1)
            # Ensures only one element from list is processed since they're all the same if equal_lists == 0
            if equal_lists == 0:
                return
        

data = get_data()

print(f"Number of elements in data: {len(data)}")
print("==========Below are items in dataset========")

simple_print(data, 0)
