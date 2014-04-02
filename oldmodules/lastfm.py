"""
lastfm.py - Phenny lastfm Module
Copyright 2013, Jin Park - jinpark.net
Uses oblique - https://github.com/nslater/oblique/
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, json
import string

def lastfm(phenny, input):
	htmlinput  = urllib.quote(input.group(2))
	url2 = 'http://tumbolia.appspot.com/lastfm/' + htmlinput + '/'
	defin = urllib.urlopen(url2).read()
	phenny.say(defin)

lastfm.commands = ['lastfm']
lastfm.priority = 'low'
lastfm.example = '.lastfm username'