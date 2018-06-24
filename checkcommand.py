#!/usr/bin/env python3

import types
import curses
from movement import moveChar
from interface import Interface
from itemcmds import pickUp, inventory, openDesc, putDown, equipItem, unequipItem, wearItem, takeOff, eatItem
from monsters import monstersUpdate
from colours import Colour
import string

screen = Interface()
rainbow = Colour()

def inputCheck(input):
    if input == 'KEY_UP':
        pass
        #key up
        #need arrows, some letters, enter

def checkAnswer(character, answer, level_monsters, level_items):
    '''decides what to do with the input'''
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
        elif answer == '~':
            if character.cheats == True:
                character.cheats = False
            else:
                character.HP = 100000
                character.cheats = True
        if type(levels) is types.MethodType:
            level_monsters = levels[0]
            level_items = levels[1] 
        if overlaid == False and character.cheats == False:
            monstersUpdate(character, level_monsters)
            stats(character) 
        elif overlaid == False:
            stats(character) 
    elif character.state == 'inventory':
        if answer in string.ascii_lowercase or answer in string.ascii_uppercase and answer not in character.alphanum:
            item = openDesc(character, answer)
            if item:
                character.state = item
        elif answer == '''
''':
            screen.interinit()
            character.state = 'game'
            stats(character)
        else:
            pass 
    else:
        if answer == 'd':
            putDown(character, character.state, level_items)
            character.state = 'inventory'
            screen.overlay()
            inventory(character)
        elif answer == 'q':
            equipItem(character, character.state)
            item = openDesc(character, character.state)
        elif answer == 'u':
            unequipItem(character, character.state)
            item = openDesc(character, character.state)
        elif answer == 'w':
            wearItem(character, character.state)
            item = openDesc(character, character.state)
        elif answer == 't':
            takeOff(character, character.state)
            item = openDesc(character, character.state)
        elif answer == 'e':
            eatItem(character, character.state)
            character.state = 'inventory'
            screen.overlay()
            inventory(character)
        elif answer == '''
''':
            character.state = 'inventory'
            screen.overlay()
            inventory(character)
    return level_monsters, level_items


def stats(character):
    if character.HP < 50:
        character.token += 1
    if character.token >= 2:
        character.HP += 1
        character.token = 0
    weapon = character.equipment['weapon']
    if weapon == False:
        weapon = 'None'
    else:
        weapon = weapon.name
    armour = character.equipment['armour']
    if armour == False:
        armour = 'None'
    else:
        armour = armour.name
    if character.setting == 1:
        floor = '| Floor: 1 OUT'
    else:
        floor = '| Floor: ' + str(character.setting - 1) + ' IN  '
    screen.addString(screen.winstatus, 1, 2, character.name, rainbow.yellow)
    screen.addString(screen.winstatus, 3, 2, 'HP: ' + '-------------------------', rainbow.white)
    screen.addNstr(screen.winstatus, 3, 6, '=========================', int(character.HP / 2), rainbow.green)
    screen.addString(screen.winstatus, 4, 2, 'Level: ' + str(character.level), rainbow.white)
    screen.addString(screen.winstatus, 5, 2, '(' + str(screen.location['lrow'] + 6) + ', ' + str(screen.location['lcol'] + 14) + ')', rainbow.white)
    screen.addString(screen.winstatus, 4, 11, floor, rainbow.white)
    screen.addString(screen.winstatus, 6, 2, 'Weapon: ' + weapon, rainbow.white) 
    screen.addString(screen.winstatus, 7, 2, 'Armour: ' + armour, rainbow.white) 
    screen.winRefresh(screen.winstatus)
