#!/usr/bin/env python3

import types
from classes import Character
import curses
from movement import moveChar
from interface import Interface
from itemcmds import pickUp, inventory, openDesc, putDown, equipItem, unequipItem
import string
from monsters import monstersUpdate

global character
character = Character(setting = 1, level = 1, cleared = 0, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = {
    'weaponry': [],
    'armour': [],
    'food': []
    }, alphanum = list(string.ascii_lowercase + string.ascii_uppercase), equipment = {
        'weapon': False, 
        'armour': False
        }, HP = 50)

screen = Interface()

def inputCheck(input):
    if input == 'KEY_UP':
        pass
        #key up
        #need arrows, some letters, enter

def checkAnswer(answer, level_monsters, level_items):
    '''decides what to do with the input'''
    screen.vline(20, 20)
    item = False
    if character.state == 'game':
        overlaid = False
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
            screen.overlay()
            inventory(character)
            overlaid = True
        if type(levels) is types.MethodType:
            level_monsters = levels[0]
            level_items = levels[1] 
#        if overlaid == False:
#            monstersUpdate(character, level_monsters)
    elif character.state == 'inventory':
        if answer in string.ascii_lowercase or answer in string.ascii_uppercase:
            item = openDesc(character, answer)
            character.state = item
        elif answer == '''
''':
            screen.interinit()
            character.state = 'game'
    else:
        if answer == 'd':
            putDown(character, character.state, level_items)
            character.state = 'inventory'
            screen.overlay()
            inventory(character)
        elif answer == 'q':
            equipItem(character, character.state)
        elif answer == 'u':
            unequipItem(character, character.state)
        elif answer == '''
''':
            character.state = 'inventory'
            screen.overlay()
            inventory(character)
    return level_monsters, level_items


