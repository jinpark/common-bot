"""
score.py - Phenny Time/Zone Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import csv
import operator

def score(phenny, input):
    """Add or Remove points """
    with open('nickpoint.csv', 'rU') as f:
        z = csv.reader(f)
        nickdict = {}
        for key, val in z:
            nickdict[key] = int(val)
	f.close()
                
    if input.group(2) == None:
        phenny.reply("Please do .score <someone's nick> <some positive or negative value>")

    totalinput1 = input.group(2)
    
    try:
        totalinput = totalinput1.split(' ')
        nick_input = totalinput[0]
        pointinput = totalinput[1].strip()
        cleannick = nick_input.strip().lower()
    
        if cleannick in nickdict:
            if pointinput == '+':
                newpoint = int(nickdict[cleannick]) + 1
                nickdict[cleannick] = newpoint
            elif pointinput == '-':
                newpoint = int(nickdict[cleannick]) - 1
                nickdict[cleannick] = newpoint
            else:
                phenny.say("Please do .score <someone's nick> <+ or ->")
                return
        else:
            if pointinput == '+':
                nickdict[cleannick] = 1
            elif pointinput == '-':
                nickdict[cleannick] = -1
            else:
                phenny.say("Please do .score <someone's nick> <+ or ->")
                return
        
        with open('nickpoint.csv', 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in nickdict.items()]
        
        phenny.say(str(nick_input) + ' now has ' + str(nickdict[cleannick]) + ' points.')
    except:
        phenny.say("Please do .score <someone's nick> <+ or ->")


score.commands = ['point', 'pt', 'score']
score.priority = 'low'
score.example = '.point jin +'
score.thread = False

def pointnick(phenny, input):
    with open('nickpoint.csv', 'rU') as f:
        z = csv.reader(f)
        nickdict = {}
        for key, val in z:
            nickdict[key] = int(val)
	f.close()
    
    cleannick = input.group(2).strip().lower()
    
    if cleannick in nickdict:
        phenny.say(str(input.group(2)) + ' has ' + str(nickdict[cleannick]) + ' points.')
    else:
        phenny.say(str(input.group(2)) + ' has no points.')
    
pointnick.commands = ['findscore', 'findpoints']
pointnick.priority = 'low'
pointnick.example = '.findscore jin'
pointnick.thread = False

def scoreboard(phenny, input):
    with open('nickpoint.csv', 'rU') as f:
        z = csv.reader(f)
        nickdict = {}
        for key, val in z:
            nickdict[key] = int(val)
	f.close()
	
	sorted_score = sorted(nickdict.iteritems(), key=operator.itemgetter(1), reverse=True)
	
	phenny_string = ""
	for i in range(len(sorted_score)):
		phenny_string = phenny_string + "{} is #{} with {} points. ".format(sorted_score[i][0], i + 1, sorted_score[i][1])
		
	phenny.say(phenny_string)
	
scoreboard.commands = ['scoreboard']
scoreboard.priority = 'low'
scoreboard.example = '.scoreboard'
scoreboard.thread = False
	
	
    
    
    
    