# -*- coding: utf8 -*-
"""
lastfm.py - Willie LastFM Module
"""

from willie.module import commands, example
import requests

@commands('lastfm', 'lfm')
@example('.lastfm bob')
def lastfm(bot, trigger):
    """.lastfm bob"""
    username = trigger.group(2)
    if not username:
        if bot.db and trigger.nick in bot.db.preferences:
            username = bot.db.preferences.get(trigger.nick, 'lastfm')
        if not username:
            return bot.msg(trigger.sender, "I don't know your lastfm username. " +
                           'Give me a username, like .lastfm bob, or save your username .userinfo --lastfm bob, for example.')

    lastfm_np = requests.get("http://tumbolia.appspot.com/lastfm/" + username).text
    bot.say(lastfm_np)
        
  