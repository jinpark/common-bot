# -*- coding: utf8 -*-
"""
ascii.py - Willie ascii spam Module
"""

from willie.module import commands, example


@commands('cat')
@example('.cat')
def cat(bot, trigger):
	bot.say("         __..--''``---....___   _..._    __")
	bot.say("     _.-'    .-/';  `        ``<._  ``.''_ `.")
	bot.say(" _.-' _..--.'_    \                    `( ) )")
	bot.say("(_..-'    (< _     ;_..__               ; `'")
	bot.say("           `-._,_)'      ``--...____..-'")


@commands('love')
@example('.love')
def love(bot, trigger):
	bot.say("(   )  (   )  / _ \(_  v  _)(   _)  (_ v _)/ _ \(  | |  )")
	bot.say(" | |    | |__( (_) ) \   /   | E_     \ / ( (_) )| |_| |")
	bot.say("(___)  (_____)\___/   \_/   (____)   (___) \___/ (_____)")
