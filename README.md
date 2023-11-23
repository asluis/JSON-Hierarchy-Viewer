# JSON-Hierarchy-Viewer
This mini-script calls an API (which it expects will return JSON formatted data) and outputs the hierarchy of the JSON structure. No values are outputted, 
only the keys in the json are included in the hierarchy.


The datasource API endpoint can be defined using the --api parameter.

# How to Use

1) Clone repo: `git clone https://github.com/asluis/JSON-Hierarchy-Viewer.git`
2) Install requirements: `pip3 install -r /path/to/requirements.txt`

    2.1) Note, it is recommended to use a virtual environment.
3) Run the python script to view its sample output: `python3 fetch.py`
4) Read the help options for an understanding of the parameters you can use: `python3 fetch.py -h`

# Example

If the json structure is as follows:
```{
  "kind": "Listing",
  "data": {
    "after": "t3_10901qv",
    "dist": 25,
    "modhash": "45sg4a8umpae36e46cb95325bd3ec86322e98010df4eb1a646",
    "geo_filter": "",
    "children": [
      {"kind": "t3"},
      {"kind":"t4"},
      {"loop":"t"}
    ],
    {"test":"true"}
  }
}
```


### The output from this script will be:
```
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
  ```
Notice how the spacing indicates the level/depth of each individual field.
  
  
