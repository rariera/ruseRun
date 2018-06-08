#!/usr/bin/env python3

from curses import wrapper, ascii
import curses
from checkcommand import checkAnswer, inputCheck
from map import mapinit
from begend import beginning

def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    loop = True
    beginning(stdscr)
#    while loop == False:
#        input = stdscr.getkey()
#        inputCheck(input)
    levels = mapinit()
    level_monsters = levels[0]
    level_items = levels[1]
    while loop == True:
        answer = stdscr.getkey()    #input a key
        levels = checkAnswer(answer, level_monsters, level_items)
        level_monsters = levels[0]
        level_items = levels[1]



 
 

        

    
wrapper(main)
