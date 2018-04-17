#!/usr/bin/env python3

from interface import Interface
from itemcmds import floorList, itemChoose, itemAdd
from monsters import monsterChoose, monsterAdd
from colours import Colour

screen = Interface()
rainbow = Colour()

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

def settingCheck(character, direction, level_monsters, level_items):
    lineNum = lineCount(character)
    changing = False
    if direction == 'up' and screen.location['lrow'] + 6 <= 1:
        changing = True
        if character.level == 2:
            character.level = 1
            lineNum = lineCount(character)
            screen.location['lrow'] = lineNum - 8
    elif direction == 'down' and screen.location['lrow'] + 6  >= lineNum:
        changing = True
        if character.level == 1:
            character.level = 2
            screen.location['lrow'] = 1
            if character.cleared < 1:
                character.cleared = 1
    if changing == True:
        level = mapChoose(character)
        map = level[0]
        screen.pad.erase()
        screen.addString(screen.pad, 0, 0, map, rainbow.white)
        lineNum = lineCount(character)
        if character.cleared < character.level:
            levels = mapChange(character)
        else:
            itemAdd(level_items, character.level)
            monsterAdd(level_monsters, character.level)
            levels = 'levels'
        screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
        return levels

def mapChange(character):
    floorlist = floorList()
    level_items = itemChoose(floorlist, character.level)
    itemAdd(level_items, character.level)
    level_monsters = monsterChoose(floorlist, character.level)
    monsterAdd(level_monsters, character.level)
    return level_monsters, level_items

def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
    screen.addString(screen.pad, 0, 0, gameMap1, rainbow.white)
    screen.padRefresh()
    floorlist = floorList()
    level_items = itemChoose(floorlist, 1)
    itemAdd(level_items, 1)
    level_monsters = monsterChoose(floorlist, 1)
    monsterAdd(level_monsters, 1)
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_monsters, level_items

