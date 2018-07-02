#!/usr/bin/env python3

import types
import curses
from movement import moveChar
from interface import Interface
from itemcmds import pickUp, inventory, openDesc, putDown, equipItem, unequipItem, wearItem, takeOff, eatItem
from monsters import monstersUpdate
from colours import Colour
import string
from begend import gameRules

screen = Interface()
rainbow = Colour()

def checkAnswer(character, answer, level_monsters, level_items):
    '''decides what to do with the input'''
    item = None
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
        elif answer == '?':
            overlaid = True
            screen.overlay()
            gameRules(character)
            character.state = 'rule'
        if type(levels) is types.MethodType:
            level_monsters = levels[0]
            level_items = levels[1] 
        if overlaid == False and character.cheats == False:
            monstersUpdate(character, level_monsters)
            stats(character)
            turnCount(character)
        elif overlaid == False:
            stats(character) 
            turnCount(character)
    elif character.state == 'rule':
        if answer == '''
''':
            screen.interinit()
            character.state = 'game'
            stats(character)           
    elif character.state == 'inventory':
        if answer in string.ascii_lowercase and answer != 'i':
            item = openDesc(character, answer)
            if item:
                character.state = item
        elif answer == '''
''' or answer == 'i':
            screen.interinit()
            character.state = 'game'
            stats(character)
        else:
            pass 
    else:
        # character.state == item
        item = character.state
        if answer == 'd':
            putDown(character, item, level_items)
            showInventory(character)
        elif answer == 'q':
            equipItem(character, item)
            showInventory(character)
        elif answer == 'u':
            unequipItem(character, item)
            showInventory(character)
        elif answer == 'w':
            wearItem(character, item)
            showInventory(character)
        elif answer == 't':
            takeOff(character, item)
            showInventory(character)
        elif answer == 'e' and item.type == 'food':
            eatItem(character, item)
            showInventory(character)
        elif answer == 'e' and item.type == 'weaponry':
            equipItem(character, item)
            showInventory(character)
        elif answer == '''
''':
            showInventory(character)
    return level_monsters, level_items

def showInventory(character):
    character.state = 'inventory'
    screen.overlay()
    inventory(character)

def turnCount(character):
    character.turns += 1
    if character.turns >= 5000:
        end(character)

def stats(character):
    if character.HP < 100:
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
    screen.addString(screen.winstatus, 3, 2, 'HP: ' , rainbow.white)
    screen.addString(screen.winstatus, 3, 14, '-------------------------', rainbow.white)
    screen.addString(screen.winstatus, 3, 6, str(character.HP) + '/100', rainbow.white)
    screen.addNstr(screen.winstatus, 3, 14, '=========================', int(character.HP / 4), rainbow.green)
    screen.addString(screen.winstatus, 4, 2, 'Level: ' + str(character.level), rainbow.white)
    screen.addString(screen.winstatus, 5, 2, '(' + str(screen.location['lrow'] + 6) + ', ' + str(screen.location['lcol'] + 14) + ')', rainbow.white)
    screen.addString(screen.winstatus, 4, 11, floor, rainbow.white)
    screen.addString(screen.winstatus, 6, 2, 'Weapon: ' + weapon + (20-len(weapon)) * ' ', rainbow.white)
    screen.addString(screen.winstatus, 7, 2, 'Armour: ' + armour + (20-len(armour)) * ' ', rainbow.white)
    screen.addString(screen.winstatus, 8, 2, 'Turns Remaining: ' + str(5000 - character.turns), rainbow.white)
    screen.winRefresh(screen.winstatus)

