#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:12:24 2020

@author: 5306143
"""
import requests
import sys

#python CreateScanWithParameter.py g1OrMFHie1WUMqBY56g35khCAXmT783v (apitoken)

url = "http://10.10.236.123:8888/graphql/v1/"
token = sys.argv[1]
payload="{\"query\":\"mutation CreateScheduleItem($input: CreateScheduleItemInput!) {\\n  create_schedule_item(input: $input) {\\n    schedule_item {\\n      id\\n    }\\n  }\\n}\",\"variables\":{\"input\":{\"site_id\":\"7\"}}}"

headers = {
  'Authorization': token,
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))