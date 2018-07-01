#!/usr/bin/env python3

from colours import Colour
from interface import Interface
from items import itemChoose, leveli
import re

rainbow = Colour()
screen = Interface()


def floorList():
    '''Generates list of available floor spaces on this floor'''
    floorlist = []
    for i in range(-1, 280):
        for k in range(0, 280):
            item = screen.getChar(screen.pad, i, k)
            if item[0] == '.' or item[0] == '"':
                loc = (i, k)
                floorlist.append(loc)
    return floorlist

def itemAdd(level_items, charlvl, charset):
    '''Adds the items on the current level to the pad'''
    level = leveli(charlvl, charset, level_items) 
    for key in level.keys():
        choicelist = level[key]
        item = choicelist[0]
        y = key[0]
        x = key[1]
        prev = screen.getChar(screen.pad, y, x)
        choicelist.append(prev)
        screen.addChar(screen.pad, y, x, item.tile, item.colour)
    screen.padRefresh()

def pickUp(character, level_monsters, level_items):
    level = leveli(character.level, character.setting, level_items)
    item = 0
    coords = 0
    for i in level.keys():
        if i == (screen.location['lrow'] + 6, screen.location['lcol'] + 14):
            coords = i
    if coords != 0:
        itemlist = level[coords]
        prev = itemlist[1]
        character.pc = (prev[0], prev[1])
        screen.addString(screen.pad, coords[0], coords[1], prev[0], prev[1])
        invent = itemlist[0]
        screen.addString(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
        if invent in character.inventory['food']:
            index = character.inventory[invent.type].index(invent)
            letter_item = character.inventory[invent.type][index]
            invent.letter = letter_item.letter
        else:
            invent.letter = character.alphanum[0]
            character.alphanum.remove(invent.letter)
        character.inventory[invent.type].append(invent)
        del level[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)]
        article = 'a'
        if not invent.countable or invent.name[-1] == 's':
            article = 'some'
        elif re.search('^[aeiou]', invent.name):
            article = 'an'
        screen.addLine("You picked up " + article + ' ' + invent.name + '.', rainbow.white)
        return level_monsters, level_items

def putDown(character, item, level_items):
    level = leveli(character.level, character.setting, level_items)
    level[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)] = [item, character.pc]
    character.pc = (item.tile, item.colour)
    character.inventory[item.type].remove(item)
    screen.addString(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    if character.equipment['armour'] == item:
        character.equipment['armour'] = False
    character.alphanum.insert(0, item.letter)
    return level_items

def inventory(character):
    screen.addString(screen.wininvent, 0, 0, 'Inventory:', rainbow.blue)
    character.state = 'inventory'
    line = 2
    for i in character.inventory.keys():
        if i == 'food':
            if len(character.inventory[i]) > 0:
                screen.addString(screen.wininvent, line, 0, i.upper(), rainbow.yellow)
                numbers = {}
                for n in character.inventory[i]:
                    number = character.inventory[i].count(n)
                    numbers[n] = number
                line += 1
                for k in numbers.keys():
                    screen.addString(screen.wininvent, line, 0, k.letter + ' - ' + k.name + '(' + str(numbers[k]) + ')', rainbow.white)
                    line += 1
                line += 1 
        else:
            if len(character.inventory[i]) > 0:
                screen.addString(screen.wininvent, line, 0, i.upper(), rainbow.yellow)
                line += 1
                numbers = []
                for n in character.inventory[i]:
                    numbers.append(n)
                for i in numbers:
                    if i == character.equipment['weapon'] or i == character.equipment['armour']:
                        colour = rainbow.green
                        string = '[Equipped]'
                    else:
                        colour = rainbow.white
                        string = ''
                    screen.addString(screen.wininvent, line, 0, i.letter + ' - ' + i.name + string, colour) 
                    line += 1
    screen.winRefresh(screen.wininvent)

def equipItem(character, item):
    if item.type == 'weaponry' and character.equipment['weapon'] != item:
        character.equipment['weapon'] = item

def unequipItem(character, item):
    if item.type == 'weaponry' and character.equipment['weapon'] == item:
       character.equipment['weapon'] = False

def wearItem(character, item):
    if item.type == 'armour':
        character.equipment['armour'] = item

def takeOff(character, item):
    if item.type == 'armour' and character.equipment['armour'] == item:
        character.equipment['armour'] = False

def eatItem(character, item):
    character.HP += item.hunger
    if character.HP >= 100:
        character.HP = 100
    character.inventory[item.type].remove(item)
   

def openDesc(character, input):
    item = False
    for list in character.inventory:
        for i in character.inventory[list]:
            if i.letter == input:
                item = i
                continue
    if item:
        screen.winClear(screen.wininvent)
        screen.addString(screen.wininvent, 2, 1, item.name.upper(), rainbow.blue) 
        screen.addString(screen.wininvent, 2, len(item.name) + 4, item.tile, item.colour)
        screen.addString(screen.wininvent, 4, 1, 'Type: ' + item.type.capitalize(), rainbow.white)
        if item.type == 'food':
            screen.addString(screen.wininvent, 5, 1, 'HP: ' + str(item.hunger), rainbow.white)
        elif item.type == 'armour':
            screen.addString(screen.wininvent, 5, 1, 'Defence: ' + str(item.hp), rainbow.white)
        else:
            screen.addString(screen.wininvent, 5, 1, 'ATK: ' + str(item.damage), rainbow.white)
        maxyx = screen.getMax(screen.wininvent)
        if item.type == 'food':
            line = '(e)at'
        elif item.type == 'weaponry':
            if character.equipment['weapon'] == item:
                line = '(u)nequip'
            else:
                line = 'e(q)uip'
        elif item.type == 'armour':
            if character.equipment['armour'] == item:
                line = '(t)ake off'
            else:
                line = '(w)ear'
        screen.addString(screen.wininvent, maxyx[0] - 2, 2, 'You can ' + line + ' or (d)rop this item.', rainbow.white)
        screen.winRefresh(screen.wininvent)
    return item
