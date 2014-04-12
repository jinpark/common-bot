"""
urbandictionary.py - bot Urban Dictionary Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/bot/
"""

from willie import module
import requests
import urllib
import string

@module.commands('ud')
def ud(bot, trigger):
    """Urban Dictionary Definition"""
    htmlinput  = urllib.quote(trigger.group(2))
    url = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
    try:
        json_response = requests.get(url).json()
        defin = json_response['list'][0]['word'] + ': ' + json_response['list'][0]['definition']
        permalink = json_response['list'][0]['permalink']
    except:
        defin = 'Bob broke something.'
    defin = defin.replace('\r\n', ' ').replace('[word]', ' ').replace('[/word]', ' ')
    bot.say(defin)

@module.commands('ude')
def ude(bot, trigger):
    """Urban Dictionary Example"""
    htmlinput  = urllib.quote(trigger.group(2))
    url = 'http://api.urbandictionary.com/v0/define?term=' + htmlinput
    try:
        json_response = requests.get(url).json()
        defin = json_response['list'][0]['word'] + ': ' + json_response['list'][0]['example']
        defin = defin.replace('\r\n', ' ')
    except:
        defin = 'No urban dictionary example found.'
    bot.say(defin)

