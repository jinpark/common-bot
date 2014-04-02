"""
new-wea.py - Phenny Weather Module using Dark Sky API
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, simplejson, apikey, csv

degc = "\xc2\xb0C "
degf = "\xc2\xb0F "
forc = ['f','F','c','C']

def degree_to_direction(deg):
  if (337.5 <= deg <= 360) or (0 <= deg < 22.5):
    return "N"
  elif 22.5 <= deg < 67.5:
    return "NE"
  elif 67.5 <= deg < 112.6:
    return "E"
  elif 112.6 <= deg < 157.5:
    return "SE"
  elif 157.5 <= deg < 202.5:
    return "S"
  elif 202.5 <= deg < 247.5:
    return "SW"
  elif 247.5 <= deg < 292.5:
    return "W"
  elif 292.5 <= deg < 337.5:
    return "NW"

# def weajew(phenny, input):
#   """Displays weather using Dark Sky API"""
#   userinput = str(input.group(2))
#   #create dict to search for nick/location
#   with open('nickloc.csv', 'rU') as f:
#     z = csv.reader(f)
#     nickdict = {}
#     for key, val in z:
#       nickdict[key] = val
#   nickname1 = input.nick
#   nickname2 = nickname1.strip().lower()
#   if nickname2 in nickdict:
#     if userinput in forc:
#       loc = nickdict[nickname2] + " " + userinput
#     elif userinput == 'None':
#       loc = nickdict[nickname2]
#     else:
#       loc = userinput
#   else:
#     loc = userinput
#   if loc == 'None':
#     urlunits = 'ca' 
#   elif loc[-2:] == " C" or loc[-2:] == " c":
#     urlunits = 'ca'
#     loc = loc[:-2]
#   elif loc[-2:] == " F" or loc[-2:] == " f":
#     urlunits = 'us'
#     loc = loc[:-2]
#   else:
#     urlunits = 'ca'
#   locinput1 = loc.strip().lower().encode('utf8')
#   htmlinput = urllib.quote(locinput1)
#   url4 = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + htmlinput + '&sensor=true'
#   jsonResponse1 = simplejson.load(urllib.urlopen(url4))
#   longi = jsonResponse1['results'][0]['geometry']['location']['lng']
#   lati = jsonResponse1['results'][0]['geometry']['location']['lat']
#   loca = jsonResponse1['results'][0]['formatted_address']
#   url3 = 'https://api.forecast.io/forecast/' + apikey.darksky + '/' + str(lati) + ',' + str(longi) + '?units=' + urlunits
#   weajson = simplejson.load(urllib.urlopen(url3))
#   nowwea = weajson['currently']
#   units = weajson['flags']['units']
#   if units == 'us':
#     deg = degf
#     windspeedunits = "mph"
#   else:
#     deg = degc
#     windspeedunits = "km/h"
#   phennyout = str(int(round(nowwea["temperature"]))) + deg + nowwea["summary"] + ", Wind " + degreeToDirection(nowwea["windBearing"]) + " " + str(round(nowwea["windSpeed"],1)) + " " + windspeedunits + " in " + loca.encode('utf8') + ". " + "Feels like " + str(round(nowwea["apparentTemperature"],1))
#   loca.encode('utf8') + "."
#   phenny.say(phennyout)
# 
# weajew.commands = ['weajew']
# weajew.priority = 'low'
# weajew.example = '.weajew n2t1k5'

def weajew(phenny, input):
    """Display weather using Dark Sky API"""

    userinput = str(input.group(2))
    #create dict to search for nick/location
    with open('nickloc.csv', 'rU') as f:
      z = csv.reader(f)
      nickdict = {}
      for key, val in z:
        nickdict[key] = val
    nickname1 = input.nick
    nickname2 = nickname1.strip().lower()
    if nickname2 in nickdict:
      if userinput in forc:
        loc = nickdict[nickname2] + " " + userinput
      elif userinput == 'None':
        loc = nickdict[nickname2]
      else:
        loc = userinput
    else:
      loc = userinput
      
    user_location = urllib.quote(loc)
    user_units = 'si'
    
    geocode_url = ("http://maps.googleapis.com/maps/api/geocode/json?address={location}&sensor=true"
            .format(location=user_location)
            )
    geocode_data = simplejson.load(urllib.urlopen(geocode_url))
    geocode_first_result = geocode_data['results'][0]
    latitude = geocode_first_result['geometry']['location']['lat']
    longitude = geocode_first_result['geometry']['location']['lng']
    location = geocode_first_result['formatted_address']

    weather_url = ("{api_url}{api_key}/{latitude},{longitude}?units={units}"
            .format(api_url='https://api.forecast.io/forecast/',
                    api_key=apikey.darksky,
                    latitude=latitude,
                    longitude=longitude,
                    units=user_units)
            )
    weather_data = simplejson.load(urllib.urlopen(weather_url))
    weather = weather_data['currently']

    degrees_celcius = "\xc2\xb0C"
    degrees_fahrenheit = "\xc2\xb0F"

    if user_units == 'us':
        temperature_unit = degrees_fahrenheit
        wind_speed_unit = "mph"
    elif user_units == 'uk':
        temperature_unit = degrees_celcius
        wind_speed_unit = "mph"
    elif user_units == 'ca':
        temperature_unit = degrees_celcius
        wind_speed_unit = "km/h"
    elif user_units == 'si':
        temperature_unit = degrees_celcius
        wind_speed_unit = "m/s"

    output = ("{temperature}{temperature_unit} ({temperature_feel}) {conditions} | Wind {wind_direction} {wind_speed} {wind_speed_unit} | {location}"
            .format(temperature=round(weather["temperature"], 1),
                    temperature_unit=temperature_unit,
                    temperature_feel=round(weather["apparentTemperature"], 1),
                    conditions=weather["summary"],
                    wind_direction=degree_to_direction(weather["windBearing"]),
                    wind_speed=round(weather["windSpeed"], 1),
                    wind_speed_unit=wind_speed_unit,
                    location=location.encode('utf8'))
            )

    phenny.say(output)

weajew.commands = ['weajew', 'weat']
weajew.priority = 'low'
weajew.example = '.weajew stockholm, sweden'
