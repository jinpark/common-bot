# -*- coding: utf8 -*-
"""
userinfo.py - Willie Yahoo! Weather Module
Copyright 2008, Sean B. Palmer, inamidst.com
Copyright 2012, Edward Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://willie.dftba.net
"""

from willie import web
from willie.module import commands, example

import re
import requests
import apikey


def setup(bot):
    # Having a db means pref's exists. Later, we can just use `if bot.db`.
    if bot.db and not bot.db.preferences.has_columns('lastfm'):
        bot.db.preferences.add_columns(['lastfm'])

    if bot.db and not bot.db.preferences.has_columns('weather_units'):
        bot.db.preferences.add_columns(['weather_units'])

@commands('userinfo', 'userdata')
@example('.userinfo --lastfm bob')
def userinfo(bot, trigger):
    """.userinfo --lastfm bob --weather si - Adds user specific data (lastfm and weather units) (use .setlocation for location specific thingies)"""

    user_input = trigger.group(2)
    split_input = re.split("--|\s", user_input)
    if 'lastfm' in split_input:
        lastfm_update(bot, trigger, split_input)
    elif 'weather' in split_input:
        weather_update(bot, trigger, split_input)


def lastfm_update(bot, trigger, split_input):
    try:
        lastfm_index = split_input.index('lastfm')
        lastfm_username = split_input[lastfm_index + 1]
        if bot.db:
            bot.db.preferences.update(trigger.nick, {'lastfm': lastfm_username})
            bot.say("Your lastfm username {} is saved.".format(lastfm_username))
            updated = True
        else:
            bot.say("database has not been configured. lastfm username cannot be saved.")
            return
    except:
        bot.say('Lastfm update failed')

def weather_update(bot, trigger, split_input):
    try:
        weather_index = split_input.index('weather')
        weather_units = split_input[weather_index + 1]
        if weather_units in ['SI', 'si', 'Si']:
            preference = 'si'
        elif weather_units in ['us', 'US']:
            preference = 'us'
        else:
            bot.say("database has not been configured. weather preferences cannot be saved.")
            return
        bot.db.preferences.update(trigger.nick, {'weather_units': preference})
        bot.say("Your weather units preference {} is saved.".format(preference))
        updated = True
    except:
        bot.say('weather update failed')
