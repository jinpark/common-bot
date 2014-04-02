"""
urbandictionary.py - Phenny Urban Dictionary Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, json
import string

def ud(phenny, input):
	"""Urban Dictionary Definition"""
	if input.group(2) == 'jin penis':
		phenny.say('bob sensei is the kawaii-est')
	elif input.group(2) == 'jin ruins':
		phenny.say('bob sensei is the kawaii-est')
	elif input.group(2) == 'birkettlife':
		phenny.say('thuglife, canada style')
	else:
		htmlinput  = urllib.quote(input.group(2))
		url2 = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
		googleResponse = urllib.urlopen(url2)
		try:
			jsonResponse = json.loads(googleResponse.read())
			defin = jsonResponse['list'][0]['word'] + ': ' + jsonResponse['list'][0]['definition']
		except:
			defin = 'Bob broke something.'
		defin = defin.replace('Jin ', 'Bob ').replace('jin ', 'bob ').replace('\r\n', ' ').replace('[word]', ' ').replace('[/word]', ' ')
		phenny.say(defin)

ud.commands = ['ud']
ud.priority = 'low'
ud.example = '.ud pf'

def ude(phenny, input):
	"""Urban Dictionary Example"""
	if input.group(2) == 'jin penis':
		phenny.say('bob sensei is the kawaii-est')
	elif input.group(2) == 'jin ruins':
		phenny.say('bob sensei is the kawaii-est')	
	else:
		htmlinput  = urllib.quote(input.group(2))
		url2 = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
		googleResponse = urllib.urlopen(url2)
		try:
			jsonResponse = json.loads(googleResponse.read())
			defin = jsonResponse['list'][0]['word'] + ': ' + jsonResponse['list'][0]['example']
			defin = defin.replace('Jin ', 'Bob ')
			defin = defin.replace('jin ', 'bob ')
			defin = defin.replace('\r\n', ' ')
		except:
			defin = 'No urban dictionary example found.'
		phenny.say(defin)

ude.commands = ['ude']
ude.priority = 'low'
ude.example = '.ude pf'
