"""
google_search.py - Willie Google Search
"""

from willie.module import commands, example

import requests

@commands('g', 'google')
@example('.g San Francisco')
def google_search(bot, trigger):
    payload = {'q': trigger.group(2)}
    json_response = requests.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0', params=payload).json()
    results = json_response['responseData']['results']
    if not results:
    	bot.say('No results found.')
    else:
    	first_result = results[0]
    	bot.say(u"{} - {}".format(first_result['unescapedUrl'], first_result['titleNoFormatting']))