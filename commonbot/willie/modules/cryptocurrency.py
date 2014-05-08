# -*- coding: utf8 -*-
"""
cryptocurrency.py - Willie cryotocurrency Module
"""
from willie import web, tools
from willie.module import rule, commands, example

import requests
@commands('doge', 'dogecoin')
@example('.doge 10')
def doge(bot, trigger):
    
    r = requests.get("http://www.cryptocoincharts.info/v2/api/tradingPair/[doge_usd]")
    price = r.json()['price']
    try:
        mult = float(trigger.group(2))
        price = float(price) * mult
    except Exception as e:
        mult = 1
    bot.say("The price of {} dogecoin is {} USD".format(mult, price))