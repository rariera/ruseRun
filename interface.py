#!/usr/bin/env python3

from random import randint
from curses import wrapper, panel
import curses
from items import itemChoose
from classes import Character
from colours import Colour

rainbow = Colour()

pad1 = curses.newpad(280, 280) #creating a window that is 40x40
window1 = curses.newwin(28, 30, 2, 40)
window2 = curses.newwin(15, 50, 31, 2)
window3 = curses.newwin(45, 70, 2, 2)

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


global character
character = Character(level = 1, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = [])


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

def itemAdd():
    for i in level_items.lvl1.items():
        tuple = i[0]
        y = tuple[0]
        x = tuple[1]
        list = i[1]
        item = list[0]
        prev = pad1.inch(y, x) & 0xff
        list.append(prev)
        pad1.addch(y, x, item.tile, item.colour)

def pickUp():
    item = 0
    for i in level_items.lvl1.keys():
        if i == (location['lrow'] + 6, location['lcol'] + 14):
            item = i
    if item != 0:
        list = level_items.lvl1[item]
        character.pc = (list[1], rainbow.white)
        pad1.addch(item[0], item[1], list[1])
        character.inventory.append(list[0])
        del level_items.lvl1[(location['lrow'] + 6, location['lcol'] + 14)]

def putDown():
    level_items.lvl1[(location['lrow'] + 6, location['lcol'] + 14)] = [item, character.pc]
    character.pc = (item.tile, item.colour)

def inventory():
    types = {
            'food': [],
            'weaponry': [],
            'armour': []
            }
    for i in character.inventory:
        types[i.type].append(i)
    window3.addstr(0, 0, 'Inventory:', rainbow.blue)
    line = 2
    for i in types.keys():
        if len(types[i]) > 0:
            window3.addstr(line, 0, i.upper(), rainbow.yellow)
            numbers = {}
            for n in types[i]:
                number = types[i].count(n)
                numbers[n] = number
            line += 1
            for k in numbers.keys():
                window3.addstr(line, 0, k.name + '(' + str(numbers[k]) + ')', rainbow.white)
                line += 1
            line += 1

def interinit():
    window3.erase()
    window3.refresh()
    window1.box()
    window1.refresh()
    window2.box()
    window2.refresh()
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

def overlay():
    window3.touchwin()
    inventory()
    window3.refresh()

def mapinit():
    '''Initialises the map and interface'''
    interinit()
    pad1.box()  #a box appears around the window
    pad1.addstr(0, 0, gameMap, rainbow.white)
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist)
    itemAdd()
    pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
    pad1.subpad(25, 25, 2, 2)
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
    return level_items.lvl1

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
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg) 
            pad1.addch(location['lrow'] + 7, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'down':
        item = verify(direction)
        if item[0] != '#':
            location['lrow'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 5, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'left':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 6, location['lcol'] + 15, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'right':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 6, location['lcol'] + 13, character.pc[0], character.pc[1])
            character.pc = item
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
