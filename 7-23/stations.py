import requests
import json

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"

r = requests.get(url,verify=False).text.split("'")[1]

station_names = r.split('@')[1:]


def parse_station_name (station_name):
    """parse station name and return a dict which value is the code"""
    try:
        _,chinese_name,code,full_pinyin,short_pinyin = station_name.split('|')
    except ValueError:
        # print(station_name)
        _,chinese_name,code,full_pinyin,short_pinyin,_ = station_name.split('|')
    return {chinese_name:code,full_pinyin:code,short_pinyin:code}


stations = {}
for station_name in station_names:
    stations.update(parse_station_name(station_name))

# 写入 JSON 数据wi
with open('stations.json', 'w+', encoding="utf-8") as f:
    json.dump(stations, f)