#!/usr/bin/env python3

from colours import Colour
from interface import Interface
from items import itemChoose

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

def itemAdd(level_items, charlvl):
    '''Adds the items on the current level to the pad'''
    if charlvl == 1:
        level = level_items.lvl1
    else:
        level = level_items.lvl2
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
    if character.level == 1:
        level = level_items.lvl1
    else:
        level = level_items.lvl2
    item = 0
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
        if invent in character.inventory[invent.type]:
            index = character.inventory[invent.type].index(invent)
            letter_item = character.inventory[invent.type][index]
            invent.letter = letter_item.letter
        else:
            invent.letter = character.alphanum[0]
            character.alphanum.remove(invent.letter)
        character.inventory[invent.type].append(invent)
        del level[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)]
        return level_monsters, level_items

def putDown(character, item, level_items):
    if character.level == 1:
        level = level_items.lvl1
    else:
        level = level_items.lvl2
    level[(screen.location['lrow'] + 6, screen.location['lcol'] + 14)] = [item, character.pc]
    character.pc = (item.tile, item.colour)
    character.inventory[item.type].remove(item)
    screen.addString(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_items

def inventory(character):
    screen.addString(screen.wininvent, 0, 0, 'Inventory:', rainbow.blue)
    character.state = 'inventory'
    line = 2
    index = 0
    for i in character.inventory.keys():
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
                index += 1
            line += 1 

def openDesc(character, input):
    item = False
    for list in character.inventory:
        for i in character.inventory[list]:
            if i.letter == input:
                item = i
                continue
    if item:
        screen.winClear(screen.wininvent)
        screen.addString(screen.wininvent, 0, 0, item.name.upper(), rainbow.blue)
        maxyx = screen.getMax(screen.wininvent)
        if item.type == 'food':
            string = '(e)at'
        elif item.type == 'weaponry':
            if character.equipment['weapon'] == item:
                string = '(u)nequip'
            else:
                string = 'e(q)uip'
        elif item.type == 'armour':
            if character.equipment['armour'] == item:
                string = '(t)ake off'
            else:
                string = '(w)ear'
        screen.addString(screen.wininvent, maxyx[0] - 2, 2, 'You can ' + string + ' or (d)rop this item.', rainbow.white)
        screen.winRefresh(screen.wininvent)
    return item


