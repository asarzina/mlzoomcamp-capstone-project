#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://localhost:8080/classification'

data = {
  "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/UK_traffic_sign_601.1.svg/2048px-UK_traffic_sign_601.1.svg.png"
}

response = requests.post(url, json=data).json()
print(response)
