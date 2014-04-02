from random import choice

def simpsons(phenny, input):
	lines = open('simpsonsquotes.txt').read().splitlines()
	phenny.say(choice(lines))



simpsons.commands = ['simpsons']
simpsons.priority = 'low'
