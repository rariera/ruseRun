#!/usr/bin/env python3

from curses import wrapper, panel
import curses

class Character(object):
    def __init__(self, cur_y, cur_x):
        self.cur_y = cur_y
        self.cur_x = cur_x

character = Character(cur_y = 2, cur_x = 2)

def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.initscr()
    pad1 = curses.newpad(40, 40) #creating a window that is 40x40
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
    lrow = 2
    lcol = 2
    pminrow = 5
    pmincol = 5
    pmaxrow = 30
    pmaxcol = 15
    while True:
        pad1.addch(character.cur_y, character.cur_x , '@')
        pad1.refresh(2, 2, 5, 5, 30, 15)
        answer = stdscr.getkey()    #input a key
        checkAnswer(answer, pad1)
        pad1.refresh(lrow, lcol, pminrow, pmincol, pmaxrow, pmaxcol)
        


def checkAnswer(answer, pad1):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up', pad1)
    elif answer == 'KEY_DOWN':
        moveChar('down', pad1)
    elif answer == 'KEY_LEFT':
        moveChar('left', pad1)
    elif answer == 'KEY_RIGHT':
        moveChar('right', pad1)


        
def moveChar(direction, pad1):
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
        

    

wrapper(main)
