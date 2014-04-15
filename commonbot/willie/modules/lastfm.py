# -*- coding: utf8 -*-
"""
lastfm.py - Willie LastFM Module
"""

from willie.module import commands, example
import requests

@commands('lastfm', 'lfm')
@example('.lastfm jinp6301')
def lastfm(bot, trigger):
    """.wiki search_term - finds wikipedia article and returns snippet of search_term"""
    user_name = trigger.group(2)
    if not user_name:
        bot.say("please add your lastfm username ex. .lastfm cbirkett")
    else:
        lastfm_np = requests.get("http://tumbolia.appspot.com/lastfm/" + user_name).text
        bot.say(lastfm_np)
        
  