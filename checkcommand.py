#!/usr/bin/env python3

import types
from classes import Character
import curses
from movement import moveChar
from interface import Interface
from itemcmds import pickUp, inventory, openDesc
import string
from monsters import monstersUpdate

global character
character = Character(level = 1, cleared = 0, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = {
    'food': [],
    'weaponry': [],
    'armour': []
   }, alphanum = list(string.ascii_lowercase + string.ascii_uppercase))

screen = Interface()


def overlay():
    screen.wininvent.touchwin()
    inventory(character)
    screen.winRefresh(screen.wininvent)

def checkAnswer(answer, level_monsters, level_items):
    '''decides what to do with the input'''
    if character.state == 'game':
        levels = 'levels'
        if answer == 'KEY_UP':
            levels = moveChar(character, 'up', level_monsters, level_items)
        elif answer == 'KEY_DOWN':
            levels = moveChar(character, 'down', level_monsters, level_items)
        elif answer == 'KEY_LEFT':
            levels = moveChar(character, 'left', level_monsters, level_items)
        elif answer == 'KEY_RIGHT':
            levels = moveChar(character, 'right', level_monsters, level_items)
        elif answer == 'g':
            levels = pickUp(character, level_monsters, level_items)
        elif answer == 'i':
            overlay()
        if type(levels) is types.MethodType:
            level_monsters = levels[0]
            level_items = levels[1]
    elif character.state == 'inventory':
        if answer in string.ascii_lowercase or answer in string.ascii_uppercase:
            openDesc(character, answer)
        elif answer == '''
''':
            screen.interinit()
            character.state = 'game'
    monstersUpdate(character, level_monsters)
    return level_monsters, level_items


