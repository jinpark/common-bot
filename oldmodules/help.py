#!/usr/bin/env python
"""
docs.py - Phenny Information Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def docs(phenny, input):
	phenny.msg(input.nick,'addloc (adds location to bot. Linked with your nick. Works with .wea and .tz) - ex. .addloc new york, ny')
	phenny.msg(input.nick,'btc (bitcoin) - ex. .btc')
	phenny.msg(input.nick,'c (calc) - ex. .c 1+1')
	phenny.msg(input.nick,'def (define) - ex. .def bailiwick')
	phenny.msg(input.nick,'ety (etymology) - ex. .ety bailiwick')
	phenny.msg(input.nick,'imdb (IMDb Movie Information) - ex. .imdb Moneyball')
	phenny.msg(input.nick,'py (python) - ex. .py print [x for x in range(10)]')
	phenny.msg(input.nick,'rt (Rotten Tomato) - ex. .rt Moneyball')
	phenny.msg(input.nick,'seen (last seen) - ex. .seen vertigo')
	phenny.msg(input.nick,'tr (translate) - ex. .tr hola or ex. .tr hello -en -sp')
	phenny.msg(input.nick,'track (track package) DISABLED UNTIL FURTHER NOTICE - ex. .track 951835170698260 fedex' )
	phenny.msg(input.nick,'tz (timezone) - ex. tz 10001 or .tz jin if location has been added')
	phenny.msg(input.nick,'wea (current weather) - ex. .wea 10001 or .wea if location has been added')
	phenny.msg(input.nick,'wf (weather forcast) - ex. .wf 10001')
	phenny.msg(input.nick,'wiki (wikipedia) - ex. .wiki hello kitty')
	phenny.msg(input.nick,'ud (urban dictionary definition) - ex. .ud PF')
	phenny.msg(input.nick,'ude (urban dictionary example - ex. .ude PF')
	phenny.msg(input.nick,'lastfm (last playing on lastfm) - ex. .lastfm jooize')


docs.commands = ['help']

'''
btc (bitcoin)
ex. btc

c (calc)
ex. c 1+1

def (define)
ex. def word

ety (etymology)
ex. .ety word

imdb (IMDb)
ex. .imdb Moneyball

py (python) - ex. .py print [x for x in range(10)]

rt (Rotten Tomato) - ex. .rt Moneyball

seen (last seen) - ex. .seen vertigo

tr (translate) - ex. .tr hola or ex. .tr hello -en -sp

track (track package) - ex. .track 951835170698260 fedex

tz (timezone) - ex. tz 11361

wea (current weather) - ex. .wea 11361

wf (weather forcast) - ex. .wf 10001

wiki (wikipedia) - ex. .wiki hello kitty
'''