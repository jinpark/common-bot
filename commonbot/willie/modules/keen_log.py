# -*- coding: utf8 -*-
"""
keen-logging.py - keen logging Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/bot/
"""

from willie import module
import requests
import apikey
import keen

# @module.rule('.*')
# @module.unblockable
def keen_log(bot, message):
    "Log every message in a channel to keen"
    # setup keen keys
    keen.project_id = apikey.keen_project_id
    keen.write_key = apikey.keen_write_key
    keen.read_key = apikey.keen_read_key
    # if this is a private message and we're not logging those, return early
    if message.sender.is_nick() and not bot.config.chanlogs.privmsg:
        return

    channel = bot.origin.sender.lstrip("#")
    nick = str(bot.origin.nick)

    # determine which message type
    if message.startswith("\001ACTION ") and message.endswith("\001"):
        message_type = "ACTION"
        message = message[8:-1]
    else:
        message_type = "MESSAGE"

    message_dict = {'type': message_type, 'channel': channel, 'nick': nick, 'text': message}

    keen.add_event('message', {'type': message_type, 'channel': channel, 'nick': nick, 'text': message})
    

