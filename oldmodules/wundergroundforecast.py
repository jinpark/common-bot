"""
wundergroundforecast.py - Phenny Weather Underground Forecast Module
Copyright 2013, Jin Park - jinpark.net
Modified from https://github.com/russellb/phennymods/blob/master/wunderground.py
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib
import json

def wf1(phenny, input):
    """Weather Underground Forecast"""
    nickdict = dict(jin = '11361', Karura = 'v6n2z4', cbirkett = 'n2t1k5', vertigo = 'vancouver,wa', cetoole = 'redmond,wa', jewice = 'lulea,se', Fungi = 'tokyo,jp', PF = 'h3r3b6', locutox = 'YSCN', xand1x = 'l4e3v5', munch = 'h3a2k6')
    if input.nick in nickdict and str(input.group(2)) == 'None':
        loc = nickdict[input.nick]
    else:
        loc = input.group(2)

    #grab weather from api
    try:
        weather = json.loads(urllib.urlopen('http://api.wunderground.com/api/42c2a37f0486227b/conditions/almanac/astronomy/forecast/pws:0/q/' + loc +'.json').read())
    except:
        return
    if not weather:
        return

    #does the response contain an error
    if 'error' in weather['response']:
        phenny.say("wf: %s" % weather['response']['error']['description'])
        return
    #does the response contain extra 'results'
    elif 'results' in weather['response']:
        output = 'wf: Ambigious Search, options: '
        counter = 0
        for index in weather['response']['results']:
            if counter == 0:
                output += "%s %s %s " % (index['city'], index['state'], index['country'])
            else:
                output += "/ %s %s %s " % (index['city'], index['state'], index['country'])                
            counter += 1
        phenny.say(output)
        return

    #if we made it here, everything should be good
    try:
        #format the city name
        city = "[%s, %s, %s]" % \
        (weather['current_observation']['display_location']['city'],
        weather['current_observation']['display_location']['state'],
        weather['current_observation']['display_location']['country'])

        #output the averages, sunrise, moon
        #some locations don't have an almanac
        if weather['almanac']['airport_code'] != "":
            almanac_output = "Avg High: %sF, %sC Low: %sF, %sC " % \
            (weather['almanac']['temp_high']['normal']['F'],
            weather['almanac']['temp_high']['normal']['C'],
            weather['almanac']['temp_low']['normal']['F'],
            weather['almanac']['temp_low']['normal']['C'])
        else:
            almanac_output = ""
        '''
        #output sunrise w/ almanac if available
        phenny.say("%s %sSunrise: %s:%s Sunset: %s:%s" % \
        (city,
        almanac_output,
        weather['moon_phase']['sunrise']['hour'],
        weather['moon_phase']['sunrise']['minute'],
        weather['moon_phase']['sunset']['hour'],
        weather['moon_phase']['sunset']['minute'],
        ))
        

        #output the current weather
        phenny.say("%s Current: %s %sF, %sC Humidity: %s, Wind: %s" % \
        (city,
        weather['current_observation']['weather'],
        weather['current_observation']['temp_f'],
        weather['current_observation']['temp_c'],
        weather['current_observation']['relative_humidity'],
        weather['current_observation']['wind_string']))
        '''
        
        #output first 3 days of forcast (today, tomorrow, second day)
        period = 1
        fcast = city + " "
        for index in weather['forecast']['txt_forecast']['forecastday']:
            fcast += str("\x02" + index['title'] + "\x02 " + index['fcttext_metric'] + " ")
            period +=1
            if period >= 4: break
        phenny.say(fcast)
    except:
        return
#wf1.commands = ['wf']
#wf1.example = '.wf 11361'
