from urllib.request import urlopen
import requests
import json


def get_some_data():
    url = "http://api.scb.se/OV0104/v1/doris/sv/ssd/START/MI/MI0307/MI0307T1"
    page = urlopen(url)
    string = page.read().decode('utf-8')
    json_obj = json.loads(string)
    for things in json_obj['variables']:
        try:
            print(things)
        except:
            pass

    return json_obj
