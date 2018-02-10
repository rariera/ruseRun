#!/usr/bin/env python3

from colours import Colour
from interface import Interface
from items import itemChoose

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
            item = screen.getChar(screen.pad, i, k)
            if item[0] == '.' or item[0] == '"':
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
        prev = screen.getChar(screen.pad, y, x)
        list.append(prev[0])
        screen.addChar(screen.pad, y, x, item.tile, item.colour)

def pickUp(character):
    item = 0
    for i in level_items.lvl1.keys():
        if i == (screen.location['lrow'] + 6, screen.location['lcol'] + 14):
            item = i
    if item != 0:
        list = level_items.lvl1[item]
        character.pc = (list[1], rainbow.white)
        screen.addString(screen.pad, item[0], item[1], list[1], rainbow.white)
        character.inventory.append(list[0])
        del level_items.lvl1[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)]

def putDown(character):
    level_items.lvl1[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)] = [item, character.pc]
    character.pc = (item.tile, item.colour)

def inventory(character):
    types = {
            'food': [],
            'weaponry': [],
            'armour': []
            }
    for i in character.inventory:
        types[i.type].append(i)
    screen.addString(screen.wininvent, 0, 0, 'Inventory:', rainbow.blue)
    line = 2
    for i in types.keys():
        if len(types[i]) > 0:
            screen.addString(screen.wininvent, line, 0, i.upper(), rainbow.yellow)
            numbers = {}
            for n in types[i]:
                number = types[i].count(n)
                numbers[n] = number
            line += 1
            for k in numbers.keys():
                screen.addString(screen.wininvent, line, 0, k.name + '(' + str(numbers[k]) + ')', rainbow.white)
                line += 1
            line += 1

def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
    screen.addString(screen.pad, 0, 0, gameMap, rainbow.white)
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist)
    itemAdd()
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_items.lvl1

