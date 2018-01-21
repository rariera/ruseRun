#!/usr/bin/env python3

from curses import wrapper, panel
import curses
from interface import mapinit,  moveChar
from classes import Character

global character
character = Character(level = 1, pc = '.')

def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    mapinit()
    while True:
        answer = stdscr.getkey()    #input a key
        checkAnswer(answer, character)
        


def checkAnswer(answer, character):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up', character)
    elif answer == 'KEY_DOWN':
        moveChar('down', character)
    elif answer == 'KEY_LEFT':
        moveChar('left', character)
    elif answer == 'KEY_RIGHT':
        moveChar('right', character)


        

        

    
wrapper(main)
