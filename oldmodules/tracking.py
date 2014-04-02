"""
tracking.py - Phenny Package Tracking Module
Copyright 2013, Jin Park - jinpark.net
API used from AfterShip
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
http://jinpark.net
"""

import requests
import time

def tracking(phenny, input):
	"""Package Tracking using AfterShip API"""
    #newloc = dict(ca = 'canada-post', us = 'usps')
	if input.group(2) == 'couriers':
		phenny.msg(input.nick, 'List of couriers - http://pastebin.com/hLuPNXc8')
	elif input.group(2).lower() == 'pf':
		phenny.say('In bed with munch')
	else:
		try:
			track = input.group(2).split(' ')

			url = 'https://api.aftership.com/v2/trackings.json/'
			values = {'api_key':'d362658619a687b15e62ada6638e71d7c9c2daa7', 'tracking_number': track[0], 'courier': track[1]}

			r = requests.post(url,data = values)

			time.sleep(3)

			url1 = 'https://api.aftership.com/v2/trackings.json/?api_key=' + 'd362658619a687b15e62ada6638e71d7c9c2daa7' + '&tracking_number=' + track[0] + '&courier=' + track[1]

			resp = requests.get(url1)

			tracktime =  resp.json()['checkpoints'][-1]['checkpoint_time']
			trackmessage =  resp.json()['checkpoints'][-1]['message']

			if resp.json()['checkpoints'][-1]['tag'] is None:
				tag = ''
			else:
				tag =  resp.json()['checkpoints'][-1]['tag']
			if resp.json()['checkpoints'][-1]['city'] is None:
				city = ''
			else:
				city =  resp.json()['checkpoints'][-1]['city']
			if resp.json()['checkpoints'][-1]['city'] is None:
				state = ''
			else:
				state = resp.json()['checkpoints'][-1]['state']
			if resp.json()['checkpoints'][-1]['country_name'] is None:
				country = ''
			else:
				country =  resp.json()['checkpoints'][-1]['country_name']
			phenny.reply('Time: ' + tracktime + ' ' + 'Location: ' + city + ' ' + state + ' ' + country + ' ' + 'Tag: ' + tag + ' ' + 'Message: ' + trackmessage)
		except:
			phenny.reply("Something went wrong. It's probably bob's fault!")
#		except Exception,e:
#			phenny.reply(str(e))


#tracking.commands = ['track']
tracking.priority = 'low'
tracking.example = '.track 951835170698260 fedex'

