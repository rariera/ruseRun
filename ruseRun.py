#!/usr/bin/env python3

from curses import wrapper, ascii
import curses
from checkcommand import checkAnswer
from itemcmds import mapinit


def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    lvls = mapinit()
    while True:
        answer = stdscr.getkey()    #input a key
        character = checkAnswer(answer)
        #monstersUpdate(character, lvls)


 
 
#options = {
#        'KEY_UP': moveChar('up'),
#        'KEY_DOWN': moveChar('down'),
#        'KEY_LEFT': moveChar('left'),
#        'KEY_RIGHT': moveChar('right')

        

    
wrapper(main)
