#!/usr/bin/env python3

from colours import Colour
from interface import Interface
from items import itemChoose
from monsters import monsterChoose, monsterAdd

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
        lineNum = 219
    else:
        map = gameMap2
        lineNum = 320
    return (map, lineNum)
   

def lineCount(character):
    level = mapChoose(character)
    lineNum = level[1]
    return lineNum 

def settingCheck(character, direction):
    lineNum = lineCount(character)
    changing = False
    if direction == 'up' and screen.location['lrow'] + 6 <= 1:
        changing = True
        screen.addString(screen.windialogue, 4, 2, 'Check #1', rainbow.yellow)
        screen.winRefresh(screen.windialogue)
        if character.level == 2:
            character.level = 1
            lineNum = lineCount(character)
            screen.location['lrow'] = lineNum - 8
    elif direction == 'down' and screen.location['lrow'] + 6  >= lineNum:
        changing = True
        if character.level == 1:
            screen.addString(screen.windialogue, 5, 2, 'Check #2', rainbow.green)
            screen.winRefresh(screen.windialogue)
            character.level = 2
            screen.location['lrow'] = 1
    if changing == True:
        level = mapChoose(character)
        map = level[0]
        screen.pad.erase()
        screen.addString(screen.pad, 0, 0, map, rainbow.white)
        lineNum = lineCount(character)
        itemAdd(level_items, character.level)
        monsterAdd(level_monsters, character.level)
        screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)



                 



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

def itemAdd(level_items, charlvl):
    if charlvl == 1:
        level = level_items.lvl1
    else:
        level = level_items.lvl2
    for key in level.keys():
        choicelist = level[key]
        item = choicelist[0]
        y = key[0]
        x = key[1]
        prev = screen.getChar(screen.pad, y, x)
        choicelist.append(prev[0])
        screen.addChar(screen.pad, y, x, item.tile, item.colour)
    screen.padRefresh()

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
    screen.padRefresh()
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist, 1)
    itemAdd(level_items, 1)
    global level_monsters
    level_monsters = monsterChoose(floorlist, 1)
    monsterAdd(level_monsters, 1)
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_items.lvl1

