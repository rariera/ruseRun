#!/usr/bin/env python3

from interface import Interface
import curses
from colours import Colour
from map import settingCheck

rainbow = Colour()
screen = Interface()

def verify(character, direction, level_monsters, level_items):
    if direction == 'up':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 5, screen.location['lcol'] + 14)
        levels = settingCheck(character, direction, level_monsters, level_items)
    elif direction == 'down':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 7, screen.location['lcol'] + 14)
        levels = settingCheck(character, direction, level_monsters, level_items)
    elif direction == 'left':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 13)
        levels = 'levels'
    elif direction == 'right':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 15)
        levels = 'levels'
    if attrs[0] == '+':
        pad1.erase()
        if character.level == 1:
            screen.addString(screen.pad, 0, 0, gameMap2)
            character.level = 2
        elif character.level == 2:
            screen.addString(screen.pad, 0, 0, gameMap)
            character.level = 1
    return (attrs, levels)
        
def moveChar(character, direction, level_monsters, level_items):
    '''Moves the character symbol in accordance with the direction.'''
    attrs = verify(character, direction, level_monsters, level_items)
    item = attrs[0]
    levels = attrs[1]
    if direction == 'up':
        if item[0] != '#':
            screen.location['lrow'] -= 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg) 
            screen.addChar(screen.pad, screen.location['lrow'] + 7, screen.location['lcol'] + 14, character.pc[0], character.pc[1])
    elif direction == 'down':
        if item[0] != '#':
            screen.location['lrow'] += 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 5, screen.location['lcol'] + 14, character.pc[0], character.pc[1])
    elif direction == 'left':
        if item[0] != '#':
            screen.location['lcol'] -= 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 15, character.pc[0], character.pc[1])
    elif direction == 'right':
        if item[0] != '#':
            screen.location['lcol'] += 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 13, character.pc[0], character.pc[1])
    character.pc = item
    screen.addString(screen.winstatus, 4, 2, 'Level: ' + str(character.level), rainbow.white)
    screen.addString(screen.winstatus, 5, 2, '(' + str(screen.location['lrow'] + 6) + ', ' + str(screen.location['lcol'] + 14) + ')', rainbow.white)
    screen.padRefresh()
    screen.winRefresh(screen.winstatus)
    return levels

