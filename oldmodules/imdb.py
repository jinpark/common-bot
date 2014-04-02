"""
imdb.py - Phenny IMDB Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""
ia = IMDb()
def imdb(phenny, input):
   """IMDb Information"""

   movie_title = input.group(2)
   s_result = ia.search_movie(movie_title)
   try:
      first_result=s_result[0]
      ia.update(first_result)
      rating1 = first_result['rating']
      short_title=first_result['title']
      year1 = first_result['year']
      runtime1 = first_result['runtime'][0]
      genres1 = ' | '.join(first_result['genre'])
      imdburl1 = ia.get_imdbURL(first_result).replace('http://akas.', 'http://', 1)
      phenny.say("\x02" + short_title + "\x02" + ' ' + '(' + str(year1) + ')' + ' ' + str(runtime1) + ' min, ' + str(rating1) + ' stars, ' + genres1 + ' -- ' + imdburl1)
   except:
      phenny.say('Movie not found')

imdb.commands = ['imdb']
imdb.priority = 'high'
imdb.example = '.imdb Moneyball'