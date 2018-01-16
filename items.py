#!/usr/bin/env python3

from random import randint, choice
import curses

class Item(object):
    def __init__(self, name, tile, colour):
        self.name = name
        self.tile = tile
        self.colour = colour

branch = Item(name = 'branch', tile = ')', colour = curses.COLOR_YELLOW)
football = Item(name = 'football', tile = 'O', colour = curses.COLOR_WHITE)


itemlist = [branch, football]

def itemChoose(floorlist):
    itemplaces = []
    for i in floorlist:
        num = randint(0, 5)
        if num == 1:
            itemplaces.append(i)
    lvl1 = {}
    for i in itemplaces:
        lvl1[i] = choice(itemlist) 
    return lvl1

