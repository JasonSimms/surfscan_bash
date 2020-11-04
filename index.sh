#!/bin/bash
echo 'GogoCode!'
curl -s -X GET https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a77087f9 -H "Accept: application/json" | \
    # python3 -c "import sys, json; print(json.load(sys.stdin)['report']['timestamp']);"
    python3 -c "import sys, json; obj=json.load(sys.stdin); print(obj['forecast']['conditions']['value']); print(obj['forecast']['wind']['speed']); print(obj['forecast']['waterTemp']['min']); print(obj['forecast']['conditions']['value']); print(obj['forecast']['waveHeight'])"
echo 'All Done here!'