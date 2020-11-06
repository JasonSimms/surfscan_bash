#!/usr/bin/env python3

def get_surfline():
    import requests, json
    
    url = 'https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a77087f9'
    resp= requests.get(url)
    data = resp.json()
    return data

surf_report = get_surfline()
# print(surf_report)
print(surf_report['forecast']['conditions']['value'])