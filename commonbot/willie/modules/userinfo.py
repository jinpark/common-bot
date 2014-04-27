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

@commands('userinfo')
@example('.userinfo --lastfm bob')
def userinfo(bot, trigger):
    """.userinfo --lastfm bob - Adds user specific data (use .setlocation for location specific thingies)"""

    user_input = trigger.group(2)
    split_input = re.split("--|\s", user_input)
    try:
        lastfm_index = split_input.index('lastfm')
        lastfm_username = split_input[lastfm_index + 1]
        bot.db.preferences.update(trigger.nick, {'lastfm': lastfm_username})
        bot.say("Your lastfm username {} is saved.".format(lastfm_username))
    except:
        bot.say('user info not saved. Blame bob.')
