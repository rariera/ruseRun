#!/usr/bin/env python3

from random import randint
from curses import wrapper, panel
import curses
from items import itemChoose
from classes import Character

curses.initscr()
pad1 = curses.newpad(280, 280) #creating a window that is 40x40
window1 = curses.newwin(40, 30, 2, 40)



map = open('farm.txt', 'r')
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



curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
global character
character = Character(level = 1, pc = ('.', ord('.') & curses.A_COLOR))


def floorList():
    '''Generates list of available floor spaces on this floor'''
    floorlist = []
    for i in range(-1, 280):
        for k in range(0, 280):
            item = pad1.inch(i, k) & 0xff
            if item == ord('.') or item == ord('"'):
                loc = (i, k)
                floorlist.append(loc)
    return floorlist

def itemAdd(lvl1):
    for i in lvl1.items():
        tuple = i[0]
        y = tuple[0]
        x = tuple[1]
        item = i[1]
        pad1.addch(y, x, item.tile, item.colour)

def pickUp():
   for i in lvl1.items():
       tuple = i[0]

def recordprev(lvl1):
    for i in lvl1.items():
        pch = pad1.inch(y, x) & 0xff
        under1[i] =  [item, pch]
    


def interinit():
    window1.box()
    window1.refresh()

def mapinit():
    '''Initialises the map and interface'''
    interinit()
    pad1.box()  #a box appears around the window
    pad1.addstr(0, 0, gameMap, curses.color_pair(7))
    floorlist = floorList()
    lvl1 = itemChoose(floorlist)
    itemAdd(lvl1)
    pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    pad1.subpad(25, 25, 2, 2)
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
    return lvl1

def verify(direction):
    if direction == 'up':
        attrs = pad1.inch(location['lrow'] + 5, location['lcol'] + 14)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'down':
        attrs = pad1.inch(location['lrow'] + 7, location['lcol'] + 14)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'left':
        attrs = pad1.inch(location['lrow'] + 6, location['lcol'] + 13)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'right':
        attrs = pad1.inch(location['lrow'] + 6, location['lcol'] + 15)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    if char == '+':
        pad1.erase()
        if character.level == 1:
            pad1.addstr(0, 0, gameMap2)
            character.level = 2
        elif character.level == 2:
            pad1.addstr(0, 0, gameMap)
            character.level = 1
    item = (char, color)
    return item
        
def moveChar(direction):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        item = verify(direction)
        if item[0] != '#':
            location['lrow'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 7, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'down':
        item = verify(direction)
        if item[0] != '#':
            location['lrow'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 5, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'left':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 6, location['lcol'] + 15, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'right':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
            pad1.addch(location['lrow'] + 6, location['lcol'] + 13, character.pc[0], character.pc[1])
            character.pc = item
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
