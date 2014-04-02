
ia = IMDb()
def movies(phenny, input):
		movie_title = input.group(2)
		s_result = ia.search_movie(movie_title)
		first_result=s_result[0]
		ia.update(first_result)
		rating=first_result['rating']
		short_title=first_result['title']
		year1 = first_result['year']
		runtime1 = first_result['runtime'][0]
		genres1 = ', '.join(first_result['genre'])

		rt1 = RT().search(movie_title)
		rttitle = rt1[0]['title']
		rtcscore = rt1[0]['ratings']['critics_score']
		rtascore = rt1[0]['ratings']['audience_score']
		try:
			rtcconsensus = rt1[0]['critics_consensus']
		except:
			rtcconsensus = 'No consensus yet.'
		phenny.reply("\x02" + short_title + "\x02" + ' ' + '(' + str(year1) + ')' + ', ' + str(runtime1) + ' mins | ' + genres1)
		phenny.reply("\x02" + rttitle + "\x02" + ' has a critics rating of ' + str(rtcscore) + ' and has an audience rating of ' + str(rtascore) + '. The critics consensus is: ' + rtcconsensus )

movies.commands = ['mv']
movies.priority = 'low'