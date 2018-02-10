#!/usr/bin/env python3

from random import randint, choice
from colours import Colour
from classes import LevelItems

rainbow = Colour()
level_items = LevelItems(lvl1 = {})

class Item(object): 
    def __init__(self, name, tile, colour, type):
        self.name = name
        self.tile = tile
        self.colour = colour
        self.type = type

class Food(Item):
    def __init__(self, name, tile, colour, type, hunger):
        Item.__init__(self, name, tile, colour, type)
        self.hunger = hunger

class Weapon(Item):
    def __init__(self, name, tile, colour, type, damage):
        Item.__init__(self, name, tile, colour, type)
        self.damage = damage

class Armour(Item):
    def __init__(self, name, tile, colour, type, hp):
        Item.__init__(self, name, tile, colour, type)
        self.hp = hp

orange = Food(name = 'orange', tile = '%', colour = rainbow.yellow, type = 'food', hunger = 6)
branch = Weapon(name = 'branch', tile = ')', colour = rainbow.red, type = 'weaponry', damage = 3)
football = Weapon(name = 'football', tile = 'O', colour = rainbow.blue, type = 'weaponry', damage = 5)
blazer = Armour(name = 'blazer', tile = '(', colour = rainbow.green, type = 'armour', hp = 3)

itemdict = {
        'food': [orange],
        'weapons': [branch, football],
        'armour': [blazer]
        }

def itemChoose(floorlist):
    '''Chooses which item will be placed in which spot'''
    itemplaces = []
    for i in floorlist:
        num = randint(0, 10)
        if num == 0:
            itemplaces.append(i)
    for i in itemplaces:
        listnum = randint(0, 2)
        if listnum == 0:
            list = itemdict['food']
        elif listnum == 1:
            list = itemdict['weapons']
        elif listnum == 2:
            list = itemdict['armour']
        level_items.lvl1[i] = [choice(list)]
    return level_items

