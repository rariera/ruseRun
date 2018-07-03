#!/usr/bin/env python3

from interface import Interface
from colours import Colour
from itemcmds import pickUp, inventory, openDesc, putDown, equipItem, unequipItem, wearItem, takeOff, eatItem
from movement import moveChar
from finder import reverseDirect, directFind, compass
from items import Spaghetti, Helmet, Saw
import string

screen = Interface()
rainbow = Colour()

tutorial1 = open('tutorial1.txt', 'r')
tutorial1 = tutorial1.read()

tutorial2 = open('tutorial2.txt', 'r')
tutorial2 = tutorial2.read()

tutorial3 = open('tutorial3.txt', 'r')
tutorial3 = tutorial3.read()


list = ["That's it!", "See those three coloured symbols over there? Those are items. You can pick one up by standing on top of it and pressing 'g'", "Congrats. View items you've picked up in the inventory (open the inventory by pressing 'i', and exit by pressing enter.", "Once in the inventory, press the letter which corresponds to the item to find out more about it.", "All monsters are represented by coloured letters. Monsters will attempy to kill you. To attack them, walk into them.", "Well done. The '+' to your right is a door. Walking into a door will allow you to enter or exit a building.", "In the top right of the room are some stairs. These are represented by either '<' (upstairs), and '>' (downstairs).", "Well done - you have completed the tutorial. At the bottom of this room are *****. Walk into them to complete the tutorial. This is also used in-game to represent the finish line."]

def tutorial(stdscr, character):
    '''the function for the tutorial'''
    character.pc = ('.', ord('.'))
    screen.addString(screen.pad, 0, 0, tutorial1, rainbow.white)
    screen.location['lrow'] = -1
    screen.location['lcol'] = -6
    screen.addChar(screen.pad, 9, 36, '%', rainbow.yellow)
    screen.addChar(screen.pad, 9, 38, '(', rainbow.blue)
    screen.addChar(screen.pad, 9, 40, ')', rainbow.red)
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    screen.addLine("Welcome to the tutorial.", rainbow.white)
    screen.addLine("Let's get started - move around using the arrow keys", rainbow.white)
    enter = False
    picked = False
    character.state = 't1'
    while enter == False:
        answer = stdscr.getkey()
        if character.state == 't1':
            if answer == 'KEY_UP':
                enter = tutMove(character, 'up', enter)
            elif answer == 'KEY_DOWN':
                enter = tutMove(character, 'down', enter)
            elif answer == 'KEY_LEFT':
                enter = tutMove(character, 'left', enter)
            elif answer == 'KEY_RIGHT':
                enter = tutMove(character, 'right', enter)
            elif answer == 'g':
                tutItems(character, picked)
            elif answer == 'i':
                screen.overlay()
                inventory(character)
                character.state = 't2'
            elif answer == ' ':
                ans = stdscr.getkey()
                if ans == ' ':
                    enter = True
                    screen.location['lrow'] = 60
                    screen.location['lcol'] = 2
        elif character.state == 't2':
            if answer in string.ascii_lowercase or answer in string.ascii_uppercase and answer not in character.alphanum:
                item = openDesc(character, answer)
                if item:
                    character.state = item
            elif answer == '''
    ''':
                screen.interinit()
                character.state = 'game'
                stats(character)


def tutMove(character, direction, enter):
    '''The character moves around in the tutorial'''
    item = tutVerify(character, direction)
    if item[0] != '#':
        if item[0] == ':':
            screen.addLine(list[0], rainbow.white)
            del list[0]
            character.pc = ('.', ord('.'))
        compass(direction)
        if item[0] not in ['>', '<', '+', '*']:
            yx = directFind(direction)
            y = yx[0]
            x = yx[1]
            screen.addChar(screen.pad, y, x, character.pc[0], character.pc[1])
            character.pc = (item[0], ord(item[0]))
        else:
            enter = tutChange(character, item[0], enter)
        screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
        screen.padRefresh()
    return enter

def tutVerify(character, direction):
    '''The characters movements are verified in the tutorial'''
    rd = reverseDirect(direction)
    yx = directFind(rd)
    y = yx[0]
    x = yx[1]
    attrs = screen.getChar(screen.pad, y, x)
    return attrs

def tutChange(character, sign, enter):
    '''The tutorial levels are changed'''
    if sign == '+':
        screen.addString(screen.pad, 0, 0, tutorial2, rainbow.white)
    elif sign in ['>', '<']:
        screen.addString(screen.pad, 0, 0, tutorial3, rainbow.white)
    else:
        enter = True
        screen.location['lrow'] = 60
        screen.location['lcol'] = 2
    screen.padRefresh()
    return enter

def tutItems(character, picked):
    '''the items for the tutorial are placed'''
    item = False
    if screen.location['lrow'] + 6 == 9 and screen.location['lcol'] + 14 == 36:
        item = Spaghetti()
        item.letter = 'a'
    elif screen.location['lrow'] + 6 == 9 and screen.location['lcol'] + 14 == 38:
        item = Helmet()
        item.letter = 'b'
    elif screen.location['lrow'] + 6 == 9 and screen.location['lcol'] + 14 == 40:
        item = Saw
        item.letter = 'c'
    if item:
        if picked == False:
            picked = True
            for i in range(0, 1):
                screen.addLine(list[0], rainbow.white)
                del list[0]
        character.inventory[item.type].append(item)
        character.pc = ('.', ord('.'))



