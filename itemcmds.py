#!/usr/bin/env python3

from colours import Colour
from interface import Interface

rainbow = Colour()
screen = Interface()

map = open('farm.txt', 'r')
gameMap = map.read()

map2 = open('map2.txt', 'r')
gameMap2 = map2.read()


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

def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
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

