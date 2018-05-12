#!/usr/bin/env python3

from random import randint, choice
from colours import Colour
from classes import LevelItems

rainbow = Colour()
level_items = LevelItems(lvl1 = {}, lvl2 = {}, lvl3 = {})

class Item(object): 
    def __init__(self, name, tile, colour, type, letter):
        self.name = name
        self.tile = tile
        self.colour = colour
        self.type = type
        self.letter = letter

class Food(Item):
    def __init__(self, name, tile, colour, type, letter,  hunger):
        Item.__init__(self, name, tile, colour, type, letter)
        self.hunger = hunger

class Weapon(Item):
    def __init__(self, name, tile, colour, type, letter, damage):
        Item.__init__(self, name, tile, colour, type, letter)
        self.damage = damage

class Armour(Item):
    def __init__(self, name, tile, colour, type, letter, hp):
        Item.__init__(self, name, tile, colour, type, letter)
        self.hp = hp

orange = Food(name = 'orange', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 6)
branch = Weapon(name = 'branch', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 3)
football = Weapon(name = 'football', tile = ')', colour = rainbow.blue, type = 'weaponry', letter = '!', damage = 5)
blazer = Armour(name = 'blazer', tile = '(', colour = rainbow.green, type = 'armour', letter = '!', hp = 3)

itemdict = {
        'food': [orange],
        'weapons': [branch, football],
        'armour': [blazer]
        }

def itemChoose(floorlist, charlvl):
    '''Chooses which item will be placed in which spot'''
    itemplaces = []
    for i in floorlist:
        num = randint(0, 100)
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
        if charlvl == 1:
            level_items.lvl1[i] = [choice(list)]
        elif charlvl == 2:
            level_items.lvl2[i] = [choice(list)]
        elif charlvl == 3:
            level_items.lvl3[i] = [choice(list)]
    return level_items

