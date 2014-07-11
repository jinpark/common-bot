# -*- coding: utf8 -*-
"""
new-wikipedia.py - Willie Wikipedia Module
"""

from willie.module import commands, example
# import wikipedia
import wikiapi


@commands('w', 'wiki', 'wik')
@example('.w San Francisco')
def wiki(bot, trigger):
  """.wiki search_term - finds wikipedia article and returns snippet of search_term"""
  search_input = trigger.group(2)
  if not input:
    bot.say('You must enter a search term')
  else:
    # bot.say(wiki_search(search_input))
    bot.say(wikiapi_search(search_input))


# def wiki_search(search_input):
#     results = wikipedia.search(search_input, results=1)
#     if not results:
#       return "No results found."
#     try:
#       wp_page = wikipedia.page(results[0])
#     except wikipedia.exceptions.DisambiguationError as e:
#       wp_page = wikipedia.page(e.options[0])
#     summary = wp_page.summary
#     url = wp_page.url
#     url_length = len(url)
#     summary_length = len(summary)

#     if summary_length + url_length > 430:
#       new_summary_length = 430 - url_length
#       summary = summary[:new_summary_length] + u"..."

#     return u"{} - {}".format(summary, url)


def wikiapi_search(search_input):
    wiki = wikiapi.WikiApi()
    results = wiki.find(search_input)
    if not results:
      return "No results found."
    # try:
    wp_page = wiki.get_article(results[0])
    # except:
    #   return 'Bob broke something again'
    summary = wp_page.summary
    url = wp_page.url
    url_length = len(url)
    summary_length = len(summary)

    if summary_length + url_length > 400:
      new_summary_length = 400 - url_length
      summary = summary[:new_summary_length] + u"..."

    return u"{} - {}".format(summary, url)
