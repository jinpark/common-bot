"""
clock.py - Willie Clock Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Copyright 2012, Edward Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net
"""
import pytz
import datetime
from willie.module import commands, example, OP

import requests
import apikey


def setup(bot):
    #Having a db means pref's exists. Later, we can just use `if bot.db`.
    if bot.db and not bot.db.preferences.has_columns('tz'):
        bot.db.preferences.add_columns(['tz'])
    if bot.db and not bot.db.preferences.has_columns('time_format'):
        bot.db.preferences.add_columns(['time_format'])


@commands('t', 'time', 'tz')
@example('.t America/New_York')
def f_time(bot, trigger):
    """Returns the current time."""
    tz_or_nick = trigger.group(2)

    tz = 'UTC'
    location = 'UTC'
    message = ''

    if tz_or_nick:
        tz_or_nick = tz_or_nick.strip()
        #We have a tz. If it's in all_timezones, we don't need to do anything
        #more, because we know it's valid. Otherwise, we have to check if it's
        #supposed to be a user, or just invalid
        if tz_or_nick in pytz.all_timezones:
            tz = tz_or_nick
            location = tz_or_nick
        elif bot.db and tz_or_nick in bot.db.preferences:
            # get tz from db if exists
            nick = tz_or_nick
            tz = bot.db.preferences.get(tz_or_nick, 'tz')
            if not tz:
                bot.say("I'm sorry, I don't know %s's timezone" % nick)
                return
            location = bot.db.preferences.get(nick, 'location')
        else:
            try:
                # incase stuff fails
                url_location = tz_or_nick
                osm_url = 'http://nominatim.openstreetmap.org/search?q=' + url_location + '&format=json'
                location_json = requests.get(osm_url).json()
                latitude = location_json[0]['lat']
                longitude = location_json[0]['lon']
                location = location_json[0]['display_name']
                geonames_url = 'http://api.geonames.org/timezoneJSON?lat=' + latitude + '&lng=' + longitude + '&username=' + apikey.geonames_username
                timezone_json = requests.get(geonames_url).json()
                tz = timezone_json['timezoneId']
            except:
                tz = 'UTC'
                location = 'UTC'
    tzi = pytz.timezone(tz)
    now = datetime.datetime.now(tzi)

    tformat = ''
    if bot.db:
        if trigger.nick in bot.db.preferences:
            tformat = bot.db.preferences.get(trigger.nick, 'time_format')
        if not tformat and trigger.sender in bot.db.preferences:
            tformat = bot.db.preferences.get(trigger.sender, 'time_format')

    bot.say(message + location + ": " + now.strftime(tformat or "%F | %T %Z"))


@commands('settz')
@example('.settz America/New_York')
def update_user(bot, trigger):
    """
    Set your preferred time zone. Most timezones will work, but it's best to
    use one from http://dft.ba/-tz
    """
    if bot.db:
        tz = trigger.group(2)
        if not tz:
            bot.reply("What timzeone do you want to set? Try one from "
                         "http://dft.ba/-tz")
            return
        if tz not in pytz.all_timezones:
            bot.reply("I don't know that time zone. Try one from "
                         "http://dft.ba/-tz")
            return

        bot.db.preferences.update(trigger.nick, {'tz': tz})
        if len(tz) < 7:
            bot.say("Okay, " + trigger.nick +
                        ", but you should use one from http://dft.ba/-tz if "
                        "you use DST.")
        else:
            bot.reply('I now have you in the %s time zone.' % tz)
    else:
        bot.reply("I can't remember that; I don't have a database.")


@commands('settimeformat', 'settf')
@example('.settf %FT%T%z')
def update_user_format(bot, trigger):
    """
    Sets your preferred format for time. Uses the standard strftime format. You
    can use http://strftime.net or your favorite search engine to learn more.
    """
    if bot.db:
        tformat = trigger.group(2)
        if not tformat:
            bot.reply("What format do you want me to use? Try using"
                         " http://strftime.net to make one.")

        tz = ''
        if bot.db:
            if trigger.nick in bot.db.preferences:
                tz = bot.db.preferences.get(trigger.nick, 'tz')
            if not tz and trigger.sender in bot.db.preferences:
                tz = bot.db.preferences.get(trigger.sender, 'tz')
        now = datetime.datetime.now(pytz.timezone(tz or 'UTC'))
        timef = ''
        try:
            timef = now.strftime(tformat)
        except:
            bot.reply("That format doesn't work. Try using"
                         " http://strftime.net to make one.")
            return
        bot.db.preferences.update(trigger.nick, {'time_format': tformat})
        bot.reply("Got it. Your time will now appear as %s. (If the "
                     "timezone is wrong, you might try the settz command)"
                     % timef)
    else:
        bot.reply("I can't remember that; I don't have a database.")


@commands('channeltz')
@example('.chantz America/New_York')
def update_channel(bot, trigger):
    """
    Set the preferred time zone for the channel.
    """
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    if bot.db:
        tz = trigger.group(2)
        if not tz:
            bot.reply("What timzeone do you want to set? Try one from "
                         "http://dft.ba/-tz")
            return
        if tz not in pytz.all_timezones:
            bot.reply("I don't know that time zone. Try one from "
                         "http://dft.ba/-tz")
            return

        bot.db.preferences.update(trigger.sender, {'tz': tz})
        if len(tz) < 7:
            bot.say("Okay, " + trigger.nick +
                        ", but you should use one from http://dft.ba/-tz if "
                        "you use DST.")
        else:
            bot.reply('I now have you in the %s time zone.' % tz)
    else:
        bot.reply("I can't remember that; I don't have a database.")


@commands('setchanneltimeformat', 'setctf')
@example('setctf %FT%T%z')
def update_channel_format(bot, trigger):
    """
    Sets your preferred format for time. Uses the standard strftime format. You
    can use http://strftime.net or your favorite search engine to learn more.
    """
    if bot.privileges[trigger.sender][trigger.nick] < OP:
        return
    if bot.db:
        tformat = trigger.group(2)
        if not tformat:
            bot.reply("What format do you want me to use? Try using"
                         " http://strftime.net to make one.")

        tz = ''
        if bot.db:
            if trigger.nick in bot.db.preferences:
                tz = bot.db.preferences.get(trigger.nick, 'tz')
            if not tz and trigger.sender in bot.db.preferences:
                tz = bot.db.preferences.get(trigger.sender, 'tz')
        now = datetime.datetime.now(pytz.timezone(tz or 'UTC'))
        timef = ''
        try:
            timef = now.strftime(tformat)
        except:
            bot.reply("That format doesn't work. Try using"
                         " http://strftime.net to make one.")
            return
        bot.db.preferences.update(trigger.sender, {'time_format': tformat})
        bot.reply("Got it. Times in this channel  will now appear as %s "
                     "unless a user has their own format set. (If the timezone"
                     " is wrong, you might try the settz and channeltz "
                     "commands)" % timef)
    else:
        bot.reply("I can't remember that; I don't have a database.")
