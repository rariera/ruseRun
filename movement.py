#!/usr/bin/env python3

from interface import Interface
import curses
from colours import Colour
from map import settingCheck, inOut, upDown 
import string
from fighting import directFind, playerAttack, compass, reverseDirect
from begend import end


rainbow = Colour()
screen = Interface()


def verify(character, direction, level_monsters, level_items):
    if direction == 'up':
        levels = settingCheck(character, direction, level_monsters, level_items)
        rd = reverseDirect(direction)
    elif direction == 'down':
        levels = settingCheck(character, direction, level_monsters, level_items)
        rd = reverseDirect(direction)
    elif direction == 'left':
        levels = 'levels'
        rd = reverseDirect(direction)
    elif direction == 'right':
        levels = 'levels'
        rd = reverseDirect(direction)
    yx = directFind(rd)
    y = yx[0]
    x = yx[1]
    attrs = screen.getChar(screen.pad, y, x)
    return (attrs, levels)
        
def moveChar(character, direction, level_monsters, level_items):
    '''Moves the character symbol in accordance with the direction.'''
    attrs = verify(character, direction, level_monsters, level_items)
    item = attrs[0]
    levels = attrs[1]
    if item[0] == '+':
        inOut(character, direction, level_monsters, level_items) 
    elif item[0] == '>':
        upDown(character, direction, 'down')
    elif item[0] == '<':
        upDown(character, direction, 'up') 
    elif item[0] == '*':
        end(character)
    if item[0] in ['"', '.', ' ', '/', 'I', '-', '_', 'P'] or item[0] not in string.ascii_letters and item[0] != '#':
        compass(direction)
        if item[0] not in ['>', '<', '+']:
            yx = directFind(direction)
            y = yx[0]
            x = yx[1]
            screen.addChar(screen.pad, y, x, character.pc[0], character.pc[1])
        else:
            if item[0] == '<':
                item = ('>', rainbow.white)
            elif item[0] == '>':
                item = ('<', rainbow.white)
        screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg) 
        character.pc = item
    elif item[0] in string.ascii_letters:
        playerAttack(character, direction, level_monsters)
    screen.addString(screen.winstatus, 4, 2, 'Level: ' + str(character.level), rainbow.white)
    screen.addString(screen.winstatus, 5, 2, '(' + str(screen.location['lrow'] + 6) + ', ' + str(screen.location['lcol'] + 14) + ')', rainbow.white)
    screen.padRefresh()
    screen.winRefresh(screen.winstatus)
    return levels

