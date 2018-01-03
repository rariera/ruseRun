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
    pad1.addch(character.cur_y, character.cur_x , '@')    
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

        
def moveChar(direction, character):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        if character.cur_y <= location['pminrow'] + 3:
            if location['pminrow'] != 0:
              #  location['pminrow'] -= 1
                location['pmaxrow'] -= 1
                location['lrow'] += 1
            pad1.addch(character.cur_y, character.cur_x, '#') 
            character.cur_y -= 1
        else:
            pad1.addch(character.cur_y, character.cur_x, '?') 
            character.cur_y -= 1
    elif direction == 'down':
        pad1.addch(character.cur_y, character.cur_x, '.')
        character.cur_y += 1
    elif direction == 'left':
        pad1.addch(character.cur_y, character.cur_x, '.')
        character.cur_x -= 1
    elif direction == 'right':
        pad1.addch(character.cur_y, character.cur_x, '.')
        character.cur_x += 1
        pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
        
