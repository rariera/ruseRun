#!/usr/bin/env python3

from curses import wrapper, panel
import curses

curses.initscr()
pad1 = curses.newpad(40, 40) #creating a window that is 40x40

map = open('map.txt', 'r')
gameMap = map.read()


map2 = open('map2.txt', 'r')
gameMap2 = map2.read()

global location
location = {
    'lrow': 2,
    'lcol': 2,
    'pminrow': 5,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 30
    }

def mapinit():
    '''Initialises the map and interface'''
    pad1.box()  #a box appears around the window
    pad1.addstr(0, 0, gameMap)
    pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

def verify(direction, character):
    if direction == 'up':
        item = pad1.inch(location['lrow'] + 5, location['lcol'] + 14) & 0xff
        if item == ord('.'):
            yes = '.'
        elif item == ord('+'):
            yes = '+'
            pad1.erase()
            if character.level == 1:
                pad1.addstr(0, 0, gameMap2)
                character.level = 2
            elif character.level == 2:
                pad1.addstr(0, 0, gameMap)
                character.level = 1
        else:
            yes = False
        return yes
    elif direction == 'down':
        item = pad1.inch(location['lrow'] + 7, location['lcol'] + 14) & 0xff
        if item == ord('.'):
            yes = '.'
        elif item == ord('+'):
            yes = '+'
            pad1.erase()
            if character.level == 1:
                pad1.addstr(0, 0, gameMap2)
                character.level = 2
            elif character.level == 2:
                pad1.addstr(0, 0, gameMap)
                character.level = 1
        else:
            yes = False
        return yes
    elif direction == 'left':
        item = pad1.inch(location['lrow'] + 6, location['lcol'] + 13) & 0xff
        if item == ord('.'):
            yes = '.'
        elif item == ord('+'):
            yes = '+'
            pad1.erase()
            if character.level == 1:
                pad1.addstr(0, 0, gameMap2)
                character.level = 2
            elif character.level == 2:
                pad1.addstr(0, 0, gameMap)
                character.level = 1
        else:
            yes = False
        return yes
    elif direction == 'right':
        item = pad1.inch(location['lrow'] + 6, location['lcol'] + 15) & 0xff
        if item == ord('.'):
            yes = '.'
        elif item == ord('+'):
            yes = '+'
            pad1.erase()
            if character.level == 1:
                pad1.addstr(0, 0, gameMap2)
                character.level = 2
            elif character.level == 2:
                pad1.addstr(0, 0, gameMap)
                character.level = 1
        else:
            yes = False
        return yes




     

        
def moveChar(direction, character):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        yes = verify(direction, character)
        if yes == '.' or yes == '+':
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, yes)
            location['lrow'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    elif direction == 'down':
        yes = verify(direction, character)
        if yes == '.' or yes == '+':
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, yes)
            location['lrow'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    elif direction == 'left':
        yes = verify(direction, character)
        if yes == '.' or yes == '+':
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, yes)
            location['lcol'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    elif direction == 'right':
        yes = verify(direction, character)
        if yes == '.' or yes == '+':
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, yes)
            location['lcol'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@')
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
