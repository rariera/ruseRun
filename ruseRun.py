#!/usr/bin/env python3

from curses import wrapper, ascii
import curses
from interface import mapinit,  moveChar, pickUp, overlay, interinit


def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    mapinit()
    while True:
        answer = stdscr.getkey()    #input a key
        checkAnswer(answer)
        


def checkAnswer(answer):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up')
    elif answer == 'KEY_DOWN':
        moveChar('down')
    elif answer == 'KEY_LEFT':
        moveChar('left')
    elif answer == 'KEY_RIGHT':
        moveChar('right')
    elif answer == 'g':
        pickUp()
    elif answer == 'i':
        overlay()
    elif answer in ['d', '/n']:
        interinit()
    
        
#options = {
#        'KEY_UP': moveChar('up'),
#        'KEY_DOWN': moveChar('down'),
#        'KEY_LEFT': moveChar('left'),
#        'KEY_RIGHT': moveChar('right')

        

    
wrapper(main)
