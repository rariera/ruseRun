#!/usr/bin/env python3

from random import randint
from curses import wrapper, panel
import curses
from items import itemChoose

curses.initscr()
pad1 = curses.newpad(40, 40) #creating a window that is 40x40
window1 = curses.newwin(40, 30, 2, 40)


map = open('map.txt', 'r')
gameMap = map.read()


map2 = open('map2.txt', 'r')
gameMap2 = map2.read()

global location
location = {
    'lrow': 2,
    'lcol': 2,
    'pminrow': 5,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 30
    }




def floorList():
    '''Generates list of available floor spaces on this floor'''
    floorlist = []
    for i in range(0, 40):
        for k in range(0, 40):
            item = pad1.inch(i, k) & 0xff
            if item == ord('.'):
                loc = (i, k)
                floorlist.append(loc)
    return floorlist

def itemAdd(lvl1):
    for i in lvl1.items():
        tuple = i[0]
        y = tuple[0]
        x = tuple[1]
        item = i[1]
        pad1.addch(y, x, item.tile)
        pad1.chgat(y, x, item.colour)

def interinit():
    window1.box()
    window1.refresh()

def mapinit():
    '''Initialises the map and interface'''
    interinit()
    pad1.box()  #a box appears around the window
    pad1.addstr(0, 0, gameMap)
    floorlist = floorList()
    lvl1 = itemChoose(floorlist)
    itemAdd(lvl1)
    pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])




def verify(direction, character):
    if direction == 'up':
        item = pad1.inch(location['lrow'] + 5, location['lcol'] + 14) & 0xff
    elif direction == 'down':
        item = pad1.inch(location['lrow'] + 7, location['lcol'] + 14) & 0xff
    elif direction == 'left':
        item = pad1.inch(location['lrow'] + 6, location['lcol'] + 13) & 0xff
    elif direction == 'right':
        item = pad1.inch(location['lrow'] + 6, location['lcol'] + 15) & 0xff
    if item == ord('+'):
        yes = '+'
        pad1.erase()
        if character.level == 1:
            pad1.addstr(0, 0, gameMap2)
            character.level = 2
        elif character.level == 2:
            pad1.addstr(0, 0, gameMap)
            character.level = 1
    else:
        yes = chr(item)
    return yes
        
def moveChar(direction, character):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        yes = verify(direction, character)
        if yes != '#':
            location['lrow'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 7, location['lcol'] + 14, character.pc)
            character.pc = yes
    elif direction == 'down':
        yes = verify(direction, character)
        if yes != '#':
            location['lrow'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 5, location['lcol'] + 14, character.pc)
            character.pc = yes
    elif direction == 'left':
        yes = verify(direction, character)
        if yes != '#':
            location['lcol'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 6, location['lcol'] + 15, character.pc)
            character.pc = yes
    elif direction == 'right':
        yes = verify(direction, character)
        if yes != '#':
            location['lcol'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 6, location['lcol'] + 13, character.pc)
            character.pc = yes
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
