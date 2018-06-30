#!/usr/bin/env python3

from curses import wrapper, ascii
import curses
from checkcommand import checkAnswer, inputCheck, stats
from map import mapinit
from begend import beginning, initalisation, end
from classes import Character
import string
from interface import Interface
from colours import Colour

screen = Interface()
rainbow = Colour()

global character
character = Character(name = 'Steve', difficulty = 1, setting = 1, level = 1, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = {
    'weaponry': [],
    'armour': [],
    'food': []
    }, alphanum = list(string.ascii_lowercase + string.ascii_uppercase), equipment = {
        'weapon': False, 
        'armour': False
        }, HP = 100, cheats = False, token = 0, been = [1.1], turns = 0)

string = '''Welcome to Ruse Rampage!
You wake up in the top-left corner of the farm.
You don't know how you got here.
All you know is you must get out - before the janitor locks the front gates!'''

def main(stdscr):
    '''The main function which will run throughout the game.'''
    character.alphanum.remove('i')
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    loop = True
    beginning(stdscr)
    initalisation(stdscr, character)
    levels = mapinit()
    level_monsters = levels[0]
    level_items = levels[1]
    stats(character)
    screen.addLine(string, rainbow.yellow)
    while loop == True:
        if character.state == 'end':
            end(character)
        answer = stdscr.getkey()    #input a key
        levels = checkAnswer(character, answer, level_monsters, level_items)
        level_monsters = levels[0]
        level_items = levels[1]

wrapper(main)
