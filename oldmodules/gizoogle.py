"""
gizoogle.py - gizoogle translation plugin for phenny
Copyright 2013, Jin Park - jinpark.net
Using www.gizoogle.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
http://jinpark.net
"""

import requests
from bs4 import BeautifulSoup
import urllib
import time


def giz(phenny, input):
	try:
		origtext = str(input.group(2))
		#htmlinput = urllib.quote(origtext)

		url = 'http://www.gizoogle.net/textilizer.php'
		values = {'translatetext': origtext}

		r = requests.post(url,data = values)

		soup = BeautifulSoup(r.text)
		gizoutput = soup.form.text.strip()
		phenny.say(gizoutput)
	except:
		phenny.say("Something went wrong. It's probably bob's fault!")



giz.commands = ['giz']
giz.priority = 'low'
giz.example = '.giz whats up'

