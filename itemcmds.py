#!/usr/bin/env python3

from colours import Colour
from interface import Interface
from items import itemChoose

rainbow = Colour()
screen = Interface()

#map2 = open('map2.txt', 'r')
#gameMap2 = map2.read()

level1 = open('farm.txt', 'r')
gameMap1 = level1.read()

level2 = open('Oval.txt', 'r')
gameMap2 = level2.read()

def mapChoose(character):
    if character.level == 1:
        map = gameMap1
    else:
        map = gameMap2
    return map
   

def lineCount(character):
    map = mapChoose(character)
    i = 0
    for line in map:
        i = i + 1
    return i

def settingCheck(character, direction):
    lineNum = lineCount(character)
    if direction == 'up' and screen.location['lrow'] + 6 <= 1:
        if character.level == 2:
            character.level = 1
            screen.location['lrow'] = lineNum - 6
    elif direction == 'down' and screen.location['lrow'] + 6 == lineNum:
        if character.level == 1:
            character.level = 2
            screen.location['lrow'] = 1
        map = mapChoose(character)
        screen.pad.erase()
        screen.addString(screen.pad, 0, 0, map)
        lineNum = lineCount(character)
        itemAdd()
        screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)



                 



def floorList():
    '''Generates list of available floor spaces on this floor'''
    floorlist = {'level1': [], 'level2': []}
    for f in floorlist.keys():
        for i in range(-1, 280):
            for k in range(0, 280):
                item = screen.getChar(screen.pad, i, k)
                if item[0] == '.' or item[0] == '"':
                    loc = (i, k)
                    floorlist[f].append(loc)
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
        invent = list[0]
        if invent in character.inventory[invent.type]:
            index = character.inventory[invent.type].index(invent)
            letter_item = character.inventory[invent.type][index]
            invent.letter = letter_item.letter
        else:
            invent.letter = character.alphanum[0]
            character.alphanum.remove(invent.letter)
        character.inventory[invent.type].append(invent)
        del level_items.lvl1[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)]

def putDown(character):
    level_items.lvl1[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)] = [item, character.pc]
    character.pc = (item.tile, item.colour)

def inventory(character):
    screen.addString(screen.wininvent, 0, 0, 'Inventory:', rainbow.blue)
    character.state = 'inventory'
    line = 2
    index = 0
    for i in character.inventory.keys():
        if len(character.inventory[i]) > 0:
            screen.addString(screen.wininvent, line, 0, i.upper(), rainbow.yellow)
            numbers = {}
            for n in character.inventory[i]:
                number = character.inventory[i].count(n)
                numbers[n] = number
            line += 1
            for k in numbers.keys():
                screen.addString(screen.wininvent, line, 0, k.letter + ' - ' + k.name + '(' + str(numbers[k]) + ')', rainbow.white)
                line += 1
                index += 1
            line += 1 

def openDesc(character, input):
    item = 0
    for list in character.inventory:
        for i in character.inventory[list]:
            if i.letter == input:
                item = i
                continue
    if item != 0:
        screen.winClear(screen.wininvent)
        screen.addString(screen.wininvent, 0, 0, item.name.upper(), rainbow.blue)
        screen.winRefresh(screen.wininvent)

def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
    screen.addString(screen.pad, 0, 0, gameMap1, rainbow.white)
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist)
    itemAdd()
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_items.lvl1

