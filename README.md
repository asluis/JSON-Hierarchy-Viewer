# JSON-Hierarchy-Viewer
This mini-script calls an API (which it expects will return JSON formatted data) and outputs the hierarchy of the JSON structure. No values are outputted, 
only the keys in the json are included in the hierarchy.


The datasource will need to be manually modified (associated API keys / auth will need to be added too).

# Example

If the json structure is as follows:
{
  "kind": "Listing",
  "data": {
    "after": "t3_10901qv",
    "dist": 25,
    "modhash": "45sg4a8umpae36e46cb95325bd3ec86322e98010df4eb1a646",
    "geo_filter": "",
    "children": [
      {"kind": "t3"}.
      {"kind":"t4"},
      {"loop":"t"}
    ],
    {"test":"true"}
  }
}

###The output from this script will be:

kind
data
  after
  dist
  modhash
  geo_filter
  children
    kind
    kind
    loop
  test
  
  
  
