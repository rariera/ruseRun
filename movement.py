#!/usr/bin/env python3

from interface import Interface
import curses
from colours import Colour

rainbow = Colour()
screen = Interface()

def verify(character, direction):
    if direction == 'up':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 5, screen.location['lcol'] + 14)
    elif direction == 'down':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 7, screen.location['lcol'] + 14)
    elif direction == 'left':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 13)
    elif direction == 'right':
        attrs = screen.getChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 15)
    if attrs[0] == '+':
        pad1.erase()
        if character.level == 1:
            screen.addString(screen.pad, 0, 0, gameMap2)
            character.level = 2
        elif character.level == 2:
            screen.addString(screen.pad, 0, 0, gameMap)
            character.level = 1
    return attrs
        
def moveChar(character, direction):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        item = verify(character, direction)
        if item[0] != '#':
            screen.location['lrow'] -= 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg) 
            screen.addChar(screen.pad, screen.location['lrow'] + 7, screen.location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'down':
        item = verify(character, direction)
        if item[0] != '#':
            screen.location['lrow'] += 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 5, screen.location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'left':
        item = verify(character, direction)
        if item[0] != '#':
            screen.location['lcol'] -= 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 15, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'right':
        item = verify(character, direction)
        if item[0] != '#':
            screen.location['lcol'] += 1
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
            screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 13, character.pc[0], character.pc[1])
            character.pc = item
    screen.padRefresh()

