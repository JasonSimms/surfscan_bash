#!/usr/bin/env python3
import requests, json, os

def get_surfline():
    
    url = 'https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a77087f9'
    resp= requests.get(url)
    data = resp.json()
    return data

surf_report = get_surfline()
# print(surf_report)
current_condition = surf_report['forecast']['conditions']['value']
# print(surf_report['forecast']['conditions']['value'])
print('Current Conditions are: ', current_condition)
