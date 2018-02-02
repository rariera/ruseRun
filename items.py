#!/usr/bin/env python3

import curses
from random import randint, choice

curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

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

orange = Food(name = 'orange', tile = '%', colour = curses.color_pair(3), hunger = 6)
branch = Weapon(name = 'branch', tile = ')', colour = curses.color_pair(1), damage = 3)
football = Weapon(name = 'football', tile = 'O', colour = curses.color_pair(4), damage = 5)
blazer = Armour(name = 'blazer', tile = '(', colour = curses.color_pair(2), hp = 3)

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
    lvl1 = {}
    for i in itemplaces:
        listnum = randint(0, 2)
        if listnum == 0:
            list = itemdict['food']
        elif listnum == 1:
            list = itemdict['weapons']
        elif listnum == 2:
            list = itemdict['armour']
        lvl1[i] = [choice(list)] 
    return lvl1

