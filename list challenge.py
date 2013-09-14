#!/usr/bin/python

games = ['pie', 'more pie', 'less pie']
foods = ['food', 'dessert', 'nomnom']
favorites = games + foods
print(favorites)
favorites.append('superFunStuff')
print(favorites)
del favorites[6]
print(favorites)
del favorites[5]
print(favorites)
favorites.append('happyMe')
favorites.append('Inconsistent :P')
print(favorites)
