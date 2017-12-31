#!/usr/bin/env python3

from curses import wrapper, panel
import curses
from interface import mapinit, charplace, moveChar

class Character(object):
    def __init__(self, cur_y, cur_x):
        self.cur_y = cur_y
        self.cur_x = cur_x

character = Character(cur_y = 2, cur_x = 2)

def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.initscr()
    mapinit()
    while True:
        answer = stdscr.getkey()    #input a key
        checkAnswer(answer)
        


def checkAnswer(answer, pad1):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up')
    elif answer == 'KEY_DOWN':
        moveChar('down')
    elif answer == 'KEY_LEFT':
        moveChar('left')
    elif answer == 'KEY_RIGHT':
        moveChar('right')


        

        

    
wrapper(main)
