#!/usr/bin/env python3

from interface import Interface
from items import itemChoose
from itemcmds import floorList, itemAdd
from monsters import monsterChoose, monsterAdd
from colours import Colour
from finder import directFind, compass

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
    '''the map is chosen'''
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
    '''the lines are counted'''
    level = mapChoose(character)
    lineNum = level[1]
    return lineNum 

def settingCheck(character, direction, level_monsters, level_items):
    '''The level is changed if need be.'''
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
    '''the characters location is checked to see if the character has been there before'''
    item = character.level + (character.setting / 10)
    if item in character.been:
        itemAdd(level_items, character.level, character.setting)
        monsterAdd(level_monsters, character.level, character.setting)
        levels = 'levels'
    else:
        levels = mapChange(character)
    return levels


def beenAdd(character):
    '''the location is added to the places that the character has been'''
    item = character.level + (character.setting / 10)
    character.been.append(item)

def mapChange(character):
    '''The map is changes (for when the character has not been there before'''
    floorlist = floorList()
    level_items = itemChoose(floorlist, character.level, character.setting)
    itemAdd(level_items, character.level, character.setting)
    level_monsters = monsterChoose(floorlist, character.level, character.setting)
    monsterAdd(level_monsters, character.level, character.setting)
    beenAdd(character)
    return level_monsters, level_items

def settingChange(character, direction, level_monsters, level_items):
    '''the level is changed (for when the character has been there before'''
    level = mapChoose(character)
    map = level[0]
    screen.pad.erase()
    screen.addString(screen.pad, 0, 0, map, rainbow.white)
    itemAdd(level_items, character.level, character.setting)
    monsterAdd(level_monsters, character.level, character.setting)
    screen.padRefresh()

def teleport(character, direction, level_monsters, level_items):
    '''The passage between A block and C block is used'''
    if character.level == 2:
        #going into quad (level = 3, set = 2)
        character.level = 3
        character.setting = 2
        settingChange(character, direction, level_monsters, level_items)  
        beenCheck(character, level_monsters, level_items)
        screen.location['lrow'] = -6
        num = screen.location['lcol'] - 350
        screen.location['lcol'] = 224 + num         
    else:
        #going into oval, (lvl = 2, set = 4)
        character.level = 2
        character.setting = 4
        settingChange(character, direction, level_monsters, level_items)
        beenCheck(character, level_monsters, level_items)
        screen.location['lrow'] = 272
        num = screen.location['lcol'] - 224
        screen.location['lcol'] = 350 + num

def upDown(character, direction, lift, level_monsters = False, level_items = False):
    '''The stairs are operated'''
    compass(direction)
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
    '''The doors are operated in and out'''
    compass(direction)
    character.pc = ('+', rainbow.white)
    if character.setting == 1:
        #going inside
        character.setting = 2
        if character.level == 2 and screen.location['lrow'] in range(270, 280):
            character.setting = 3
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


