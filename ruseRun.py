#!/usr/bin/env python3

from curses import wrapper, ascii
import curses
from checkcommand import checkAnswer, inputCheck
from map import mapinit
from begend import beginning, initalisation, end
from classes import Character
import string

global character
character = Character(name = 'Steve', difficulty = 1, setting = 1, level = 1, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = {
    'weaponry': [],
    'armour': [],
    'food': []
    }, alphanum = list(string.ascii_lowercase + string.ascii_uppercase), equipment = {
        'weapon': False, 
        'armour': False
        }, HP = 50, cheats = False, token = 0, been = [1.1])


def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    loop = True
    beginning(stdscr)
    initalisation(stdscr, character)
#    while loop == False:
#        input = stdscr.getkey()
#        inputCheck(input)
    levels = mapinit()
    level_monsters = levels[0]
    level_items = levels[1]
    while loop == True:
        if character.state == 'end':
            end(character)
        answer = stdscr.getkey()    #input a key
        levels = checkAnswer(character, answer, level_monsters, level_items)
        level_monsters = levels[0]
        level_items = levels[1]



 
 

        

    
wrapper(main)
