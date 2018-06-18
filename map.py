#!/usr/bin/env python3

from interface import Interface
from itemcmds import floorList, itemChoose, itemAdd
from monsters import monsterChoose, monsterAdd
from colours import Colour
from fighting import compass, directFind

screen = Interface()
rainbow = Colour()

farm1 = open('farm1.txt', 'r')
farm1 = farm1.read()

farm2 = open('farm2.txt', 'r')
farm2 = farm2.read()

oval1 = open('oval1.txt', 'r')
oval1 = oval1.read()

oval2 = open('oval2.txt', 'r')
oval2 = oval2.read()

oval3 = open('oval3.txt', 'r')
oval3 = oval3.read()

oval4 = open('oval4.txt', 'r')
oval4 = oval4.read()

quad1 = open('quad1.txt', 'r')
quad1 = quad1.read()

quad2 = open('quad2.txt', 'r')
quad2 = quad2.read()

quad3 = open('quad3.txt', 'r')
quad3 = quad3.read()

gameMap = {
        'lvl1': [farm1, farm2],
        'lvl2': [oval1, oval2, oval3, oval4],
        'lvl3': [quad1, quad2, quad3]
        }

def mapChoose(character):
    if character.level == 1:
        map = gameMap['lvl1']
        map = map[character.setting - 1]
        lineNum = 219
    elif character.level == 2:
        map = gameMap['lvl2']
        map = map[character.setting - 1]
        lineNum = 332
    else:
        map = gameMap['lvl3']
        map = map[character.setting - 1]
        lineNum = 200
    return (map, lineNum)

def lineCount(character):
    level = mapChoose(character)
    lineNum = level[1]
    return lineNum 

def settingCheck(character, direction, level_monsters, level_items):
    lineNum = lineCount(character)
    changing = False
    levels = 'levels'
    if direction == 'up' and screen.location['lrow'] + 6 <= 0:
        changing = True
        if character.level == 2:
            character.level = 1
            lineNum = lineCount(character)
            screen.location['lrow'] = lineNum - 5
            screen.location['lcol'] += 20
        elif character.level == 3:
            character.level = 2
            lineNum = lineCount(character)
            screen.location['lrow'] = lineNum - 5
            screen.location['lcol'] += 75
    elif direction == 'down' and screen.location['lrow'] + 6  >= lineNum:
        changing = True
        if character.level == 1:
            character.level = 2
            screen.location['lrow'] = -6
            screen.location['lcol'] -= 20
        elif character.level == 2:
            character.level = 3
            screen.location['lrow'] = -6
            screen.location['lcol'] -= 75
    if changing == True:
        level = mapChoose(character)
        map = level[0]
        screen.pad.erase()
        screen.touchWin(screen.pad)
        screen.addString(screen.pad, 0, 0, map, rainbow.white)
        square = screen.getChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14)
        character.pc = (square[0], square[1])
        lineNum = lineCount(character)
        levels = beenCheck(character, level_monsters, level_items)
    return levels, changing

def beenCheck(character, level_monsters, level_items):
    item = character.level + (character.setting / 10)
    if item in character.been:
        itemAdd(level_items, character.level, character.setting)
        monsterAdd(level_monsters, character.level, character.setting)
        levels = 'levels'
    else:
        levels = mapChange(character)
    return levels


def beenAdd(character):
    item = character.setting + (character.level / 10)
    character.been.append(item)

def mapChange(character):
    floorlist = floorList()
    level_items = itemChoose(floorlist, character.level, character.setting)
    itemAdd(level_items, character.level, character.setting)
    level_monsters = monsterChoose(floorlist, character.level, character.setting)
    monsterAdd(level_monsters, character.level, character.setting)
    beenAdd(character)
    return level_monsters, level_items

def settingChange(character, direction, level_monsters, level_items):
    level = mapChoose(character)
    map = level[0]
    screen.pad.erase()
    screen.addString(screen.pad, 0, 0, map, rainbow.white)
    itemAdd(level_items, character.level, character.setting)
    monsterAdd(level_monsters, character.level, character.setting)
    screen.padRefresh()
    directions = directFind(direction)

def upDown(character, direction, lift, level_monsters, level_items):
    compass(direction)
    if lift == 'up':
        character.setting += 1
        settingChange(character, direction, level_monsters, level_items)
        beenCheck(character, level_monsters, level_items)
        character.pc = ('!', rainbow.white)
    else:
        character.setting -= 1
        settingChange(character, direction, level_monsters, level_items)
        character.pc = ('?', rainbow.white)

def inOut(character, direction, level_monsters, level_items): 
    character.pc = ('+', rainbow.white)
    if character.setting == 1:
        #going inside
        character.setting = 2
        settingChange(character, direction, level_monsters, level_items)
        beenCheck(character, level_monsters, level_items)
    else:
        #going outside
        character.setting = 1
        settingChange(character, direction, level_monsters, level_items)


def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
    screen.addString(screen.pad, 0, 0, farm1, rainbow.white)
    screen.padRefresh()
    floorlist = floorList()
    level_items = itemChoose(floorlist, 1, 1)
    itemAdd(level_items, 1, 1)
    level_monsters = monsterChoose(floorlist, 1, 1)
    monsterAdd(level_monsters, 1, 1)
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_monsters, level_items


