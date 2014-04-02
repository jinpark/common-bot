"""
pokemon.py - Phenny Pokedex Module
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

from pokedex.db import connect, tables, util
from pokedex.lookup import PokedexLookup
lookup = PokedexLookup()

def pokeinfo(pokemon):
  evolution = [] 
  for poke in pokemon.evolution_chain.species:
    evolution.append(poke.name)

  evolution_chain = ", ".join(evolution)

  flavor = " ".join(pokemon.flavor_text[0].flavor_text.replace("\n", " ").strip().split())

  typeList = []
  for types in pokemon.default_pokemon.types:
    typeList.append(types.name)

  types = ", ".join(typeList)

  return_string = "\x02" + pokemon.name + "\x02" + ", the " + pokemon.genus + " pokemon " + "(#" + str(pokemon.id) +"\x02" + ", Generation: " + "\x02" + str(pokemon.generation.id) + ")" + "\x02" + "  Types: " + "\x02" + types + "." + "\x02" + "  Evolution chain: " + "\x02" + evolution_chain + "." + "\x02" + "  Description: " + "\x02" + flavor
  
  return return_string

def pokedex(phenny, input):
  newsession = connect()
  try:
    new_input = input.group(2)
    pokemon = util.get(newsession, tables.PokemonSpecies, new_input.lower())

    phenny.say(pokeinfo(pokemon))
  except:
    try:
      new_input = lookup.lookup(input.group(2), ['pokemon', '@en'])[0].name
      pokemon = newsession.query(tables.PokemonSpecies).filter_by(name=new_input).one()
      phenny.say(pokeinfo(pokemon))
    except:
      phenny.say("Pokemon \"" + input.group(2) + "\" not found")

pokedex.commands = ['pokedex', 'dex', 'pokemon']
pokedex.priority = 'low'
pokedex.example = '.pokedex gyarados'
