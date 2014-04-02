"""
rottentomatoes.py - Phenny Rotten Tomatoes Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""
def rt(phenny, input):
	"""Rotten Tomatoes Movie Information"""
	try:
		rt1 = RT().search(input.group(2))
		rttitle = rt1[0]['title']
		rtcscore = rt1[0]['ratings']['critics_score']
		rtascore = rt1[0]['ratings']['audience_score']
		try:
			rtcconsensus = rt1[0]['critics_consensus']
		except:
			rtcconsensus = 'No consensus yet.'
		phenny.say("\x02" + rttitle + "\x02" + ' has a critics rating of ' + str(rtcscore) + ' and has an audience rating of ' + str(rtascore) + '. The critics consensus is: ' + rtcconsensus )
	except:
	 	phenny.say('No movie found')

rt.commands = ['rt']
rt.priority = 'low'
rt.example = '.rt Moneyball'