#!/usr/bin/env python3

from random import randint, choice
import curses

class Item(object):
    def __init__(self, name, tile, colour):
        self.name = name
        self.tile = tile
        self.colour = colour

class Food(Item):
    def __init__(self, name, tile, colour, hunger):
        Item.__init__(self, name, tile, colour)
        self.hunger = hunger

class Weapon(Item):
    def __init__(self, name, tile, colour, damage):
        Item.__init__(self, name, tile, colour)
        self.damage = damage

class Armour(Item):
    def __init__(self, name, tile, colour, hp):
        Item.__init__(self, name, tile, colour)
        self.hp = hp

orange = Food(name = 'orange', tile = '%', colour = curses.COLOR_YELLOW, hunger = 6)
branch = Weapon(name = 'branch', tile = ')', colour = curses.COLOR_RED, damage = 3)
football = Weapon(name = 'football', tile = 'O', colour = curses.COLOR_BLUE, damage = 5)
blazer = Armour(name = 'blazer', tile = '(', colour = curses.COLOR_GREEN, hp = 3)

itemdict = {
        'food': [orange],
        'weapons': [branch, football],
        'armour': [blazer]
        }

def itemChoose(floorlist):
    '''Chooses which item will be placed in which spot'''
    itemplaces = []
    for i in floorlist:
        num = randint(0, 5)
        if num == 1:
            itemplaces.append(i)
    lvl1 = {}
    for i in itemplaces:
        listnum = randint(0, 2)
        if listnum == 0:
            list = itemdict['food']
        elif listnum == 1:
            list = itemdict['weapons']
        elif listnum == 2:
            list = itemdict['armour']
        lvl1[i] = choice(list) 
    return lvl1

