import json

stations = {}
with open('stations.json', 'r') as f:
    stations = json.load(f)

def get(chinesename):
    return stations.get(chinesename)
# print(stations.get("北京"))