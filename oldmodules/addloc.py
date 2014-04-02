import csv
import os
import unicodedata

def addloc(phenny, input):
	with open('nickloc.csv', 'rU') as f:
	    z = csv.reader(f)
	    names = {}
	    for key, val in z:
	        names[key] = val

	nickname = input.nick
	if input.group(2) == None:
		phenny.reply("Please do .addloc <your city>")
	else:
		names[nickname.strip().lower()] = unicodedata.normalize('NFKD', input.group(2)).encode('ascii','ignore')

	with open('nickloc.csv','w') as f:
	    w = csv.writer(f)
	    for key, val in names.items():
	        w.writerow([key, val])

	phenny.reply("Location Added")

addloc.commands = ['addloc']
addloc.priority = 'low'