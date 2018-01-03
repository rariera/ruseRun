#!/usr/bin/env python3

from curses import wrapper, panel
import curses

curses.initscr()
pad1 = curses.newpad(40, 40) #creating a window that is 40x40

global location
location = {
    'lrow': 5,
    'lcol': 5,
    'pminrow': 5,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 30
    }

def mapinit():
    pad1.box()  #a box appears around the window
    gameMap = '''.............................>>>>>>>>>
............................>>>>>>>
......................>>>>>>>
......................>>>>>>>
.......%.............
.......%..............
...%%%%%%%%%..........
.......%..............
.......%..............
.......%....................
............................
............................
............................
............................'''
    pad1.addstr(0, 0, gameMap)
    
def charplace(character):
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

        
def moveChar(direction, character):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '.')
        location['lrow'] -= 1
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '@')
    elif direction == 'down':
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '.')
        location['lrow'] += 1
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '@')
    elif direction == 'left':
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '.')
        location['lcol'] -= 1
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '@')
    elif direction == 'right':
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '.')
        location['lcol'] += 1
        pad1.addch(location['lrow'] + 15, location['lcol'] + 15, '@')
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
