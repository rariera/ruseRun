#!/usr/bin/env python3

from curses import wrapper, panel
import curses


pad1 = curses.newpad(40, 40) #creating a window that is 40x40


lrow = 2
lcol = 2
pminrow = 5
pmincol = 5
pmaxrow = 30
pmaxcol = 15


def mapinit():
    pad1.box()  #a box appears around the window
    gameMap = '''.............................>>>>>>>>>
............................>>>>>>>
......................>>>>>>>
......................>>>>>>>
......................
......................
......................
......................
......................
............................
............................
............................
............................
............................'''
    pad1.addstr(0, 0, gameMap)
    
def charplace():
    pad1.addch(character.cur_y, character.cur_x , '@')
    pad1.refresh(2, 2, 5, 5, 30, 13)
        

        
def moveChar(direction):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        pad1.addch(character.cur_y, character.cur_x, '.') 
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
    pad1.refresh(lrow, lcol, pminrow, pmincol, pmaxrow, pmaxcol)
        
