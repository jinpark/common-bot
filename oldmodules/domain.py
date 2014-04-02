"""
domain.py - Phenny Time/Zone Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import requests
import urllib


def domain(phenny, input):
    try:
        r = requests.get('http://freedomainapi.com/?key=j9eokw730j&domain=' + urllib.quote(input.group(2).encode("utf-8")))
        rjson = r.json()
        if rjson['status'] == 'success':
            if rjson['available'] == True:
                status = 'available'
            else:
                status = 'unavailable'
    
        statusreport = str(rjson['domain']) + ' is ' + status + '.' 
        phenny.say(statusreport)
    except:
        phenny.say("Something went wrong. Most likely Bob's fault")

domain.commands = ['domain', 'd']
domain.priority = 'low'
domain.example = '.domain google.com'