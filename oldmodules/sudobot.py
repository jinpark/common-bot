"""
sudobot.py - Phenny Sudobot Module
Jin Park - jinpark.net

http://inamidst.com/phenny/
"""

from random import choice

KILL_METHODS = ['eviscerates jin.', 'assassinates jin.', 'eats jin.', 'tars and feathers jin.', 'makes jin dead.', 'decapitates jin.', 'rapes jin.']

def act(msg):
    action = '\x01ACTION %s\x01' % msg
    return action

def kill(phenny, input):
	person = input.group(2).strip()
	if not person:
		person = 'bob'
	phenny.say(act(choice(KILL_METHODS).replace('jin', person))) 
    
kill.commands = ['kill']
kill.priority = 'low'
kill.example = '.kill pf'

def make(phenny, input):
	user_input = input.group(2)
	if not user_input:
		reply = 'turns bob into a pretty lady'
        else:
            subject = user_input.split()[0]
            object = user_input.split(' ',1)[1]
            reply = "turns {} into {}".format(subject, object)
	phenny.say(act(reply)) 
    
make.commands = ['make']
make.priority = 'low'
make.example = '.make pf into a pretty lady'
