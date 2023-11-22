# JSON-Hierarchy-Viewer
This mini-script calls an API (which it expects will return JSON formatted data) and outputs the hierarchy of the JSON structure. No values are outputted, 
only the keys in the json are included in the hierarchy.


The datasource will need to be manually modified (associated API keys / auth will need to be added too).

# Example

If the json structure is as follows:
{<br/>
  "kind": "Listing",<br/>
  "data": {<br/>
    "after": "t3_10901qv",<br/>
    "dist": 25,<br/>
    "modhash": "45sg4a8umpae36e46cb95325bd3ec86322e98010df4eb1a646",<br/>
    "geo_filter": "",<br/>
    "children": [<br/>
      {"kind": "t3"}.<br/>
      {"kind":"t4"},<br/>
      {"loop":"t"}<br/>
    ],<br/>
    {"test":"true"}<br/>
  }<br/>
}<br/>

# How to Use

1) Clone repo
2) Install requirements: pip install -r /path/to/requirements.txt
    2.1) Note, it is recommended to use a virtual environment prior to installing requirements.
3) Run the python script to view its sample output: python3 fetch.py
4) Read the help options for an understanding of the parameters you can use: python3 fetch.py -h

### The output from this script will be:

kind<br/>
data<br/>
  after<br/>
  dist<br/>
  modhash<br/>
  geo_filter<br/>
  children<br/>
    kind<br/>
    kind<br/>
    loop<br/>
  test<br/>
  
  
  
