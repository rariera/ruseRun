#!/usr/bin/env python3

from interface import Interface
import time
import sys
from colours import Colour
import curses
from items import quipChar
import string
from tutorial import tutorial

screen = Interface()
rainbow = Colour()

def end(character):
    screen.overlay()
    maxyx = screen.getMax(screen.wininvent)
    y = maxyx[0]
    if character.HP <= 0:
        screen.addString(screen.wininvent, int(y / 2), 2, 'Ouch! You were savagely murdered...', rainbow.red)
    elif character.turns <= 0:
        screen.addString(screen.wininvent, int(y / 2), 2, 'Sorry, you ran out of time!', rainbow.red)
    else:
        screen.addString(screen.wininvent, int(y / 2), 2, 'Congratulations! you win!!', rainbow.yellow)
    screen.addString(screen.wininvent, int(y / 2) + 1, 2, 'Turns: ' + str(character.turns) + '/5000', rainbow.white)
    screen.winRefresh(screen.wininvent)
    time.sleep(10) 
    sys.exit("Thanks for Playing!")

def beginning(stdscr):
    screen.overlay()
    logo = open('ruseRampage2.txt', 'r')
    logo = logo.read()
    screen.addString(screen.wininvent, 1, 2, logo, rainbow.white)
    maxyx = screen.getMax(screen.wininvent)
    x = maxyx[1]
    screen.addString(screen.wininvent, 43, int(x/2) - 8, '[PRESS ENTER]', rainbow.green)
    screen.winRefresh(screen.wininvent)
    enter = False
    while enter == False:
        input = stdscr.getkey()
        if input == '''
''':
            enter = True
            screen.winClear(screen.wininvent)
            screen.winRefresh(screen.wininvent)
    #overlay, bring up logo & [press ENTER], when enter is pressed, finish function

def getName(stdscr, character):
    screen.addString(screen.wininvent, 2, 2, "Welcome to Ruse Rampage.", rainbow.yellow)
    screen.addString(screen.wininvent, 3, 2, "Please type in your name to begin, then press enter.", rainbow.white)
    screen.addString(screen.wininvent, 5, 2, "+-------------------+", rainbow.white)
    screen.addString(screen.wininvent, 6, 2, '|                   |', rainbow.white)
    screen.addString(screen.wininvent, 7, 2, "+-------------------+", rainbow.white)
    screen.winRefresh(screen.wininvent)
    enter = False
    cursor = 3
    name = []
    while enter == False:
        input = stdscr.getkey()
        if input == '''
''':
            name = ''.join(name)
            character.name = name
            screen.winClear(screen.wininvent)
            screen.winRefresh(screen.wininvent)
            enter = True
        elif input in string.printable:
            name.append(input)
            screen.addChar(screen.wininvent, 6, cursor, input, rainbow.yellow)
            screen.winRefresh(screen.wininvent)
            cursor += 1
        else:
            del name[-1]
            cursor -= 1
            screen.addChar(screen.wininvent, 6, cursor, ' ', rainbow.white)
            screen.winRefresh(screen.wininvent)

def getDifficulty(stdscr, character):
    weapon = character.equipment['weapon']
    if weapon == False:
        character.name = character.name + ' the Unarmed Student'
        phrase = '. Don\'t you think that was kind of dumb?'
    elif weapon.name == 'branch':
        character.name  = character.name + ' the Branch-Wielder'
        phrase = '.'
    elif weapon.name == 'football':
        character.name = character.name + ' the Football Player'
        phrase = '.'
    screen.addString(screen.wininvent, 2, 2, "Welcome, " + character.name + phrase, rainbow.yellow)
    screen.addString(screen.wininvent, 3, 2, "Please choose a difficulty level.", rainbow.yellow)
    screen.addString(screen.wininvent, 4, 4, "+-----------------+", rainbow.white)
    screen.addString(screen.wininvent, 5, 4, "| 1 - Easy        |", rainbow.white)
    screen.addString(screen.wininvent, 6, 4, "| 2 - Normal      |", rainbow.white)
    screen.addString(screen.wininvent, 7, 4, "| 3 - Hard        |", rainbow.white)
    screen.addString(screen.wininvent, 8, 4, "| 4 - INSANE      |", rainbow.white)
    screen.addString(screen.wininvent, 9, 4, "+-----------------+", rainbow.white) 
    screen.winRefresh(screen.wininvent)
    enter = False
    while enter == False:
        input = stdscr.getkey()
        if input == '1':
            character.difficulty = 'easy'
            enter = True
        elif input == '2':
            character.difficulty = 'normal'
            enter = True
        elif input == '3':
            character.difficulty = 'hard'
            enter = True
        elif input == '4':
            character.difficulty = 'insane'
            enter = True
    screen.winClear(screen.wininvent)
    screen.winRefresh(screen.wininvent)


def getWeapon(stdscr, character):
   screen.addString(screen.wininvent, 2, 2, "Welcome, " + character.name + ". Please choose a weapon.", rainbow.yellow)
   screen.addString(screen.wininvent, 3, 4, "+-----------------+", rainbow.white)
   screen.addString(screen.wininvent, 4, 4, "| 1 - unarmed     |", rainbow.white)
   screen.addString(screen.wininvent, 5, 4, "| 2 - branch      |", rainbow.white)
   screen.addString(screen.wininvent, 6, 4, "| 3 - soccer ball |", rainbow.white)
   screen.addString(screen.wininvent, 7, 4, "+-----------------+", rainbow.white)
   screen.winRefresh(screen.wininvent)
   enter = False
   while enter == False:
       input = stdscr.getkey()
       if input == '1':
           character.equipment['weapon'] = False
           enter = True
       elif input == '3':
           character.equipment['weapon'] = 3
           quipChar(character)
           enter = True
       elif input == '2':
           character.equipment['weapon'] = 2
           quipChar(character)
           enter = True
   screen.winClear(screen.wininvent)
   screen.winRefresh(screen.wininvent)

def menu(stdscr, character):
    screen.addString(screen.wininvent, 2, 2, 'Welcome, ' + character.name + ".", rainbow.yellow)
    choices = ["Begin Game", "Tutorial", 'Game Rules']
    index = 4
    enter = False
    screen.addString(screen.wininvent, 4, 4, "Begin Game", rainbow.white_bg)
    screen.addString(screen.wininvent, 5, 4, "Tutorial", rainbow.white)
    screen.addString(screen.wininvent, 5, 14, "[CAUTION]", rainbow.yellow)
    screen.addString(screen.wininvent, 6, 4, "Game Rules", rainbow.white)
    screen.addString(screen.wininvent, 7, 24, "Move using the arrow keys.", rainbow.yellow)
    screen.addString(screen.wininvent, 8, 20, "Choose an option by pressing ENTER", rainbow.yellow)
    screen.winRefresh(screen.wininvent)
    while enter == False:
        input = stdscr.getkey()
        if input == 'KEY_DOWN' and index < 6:
            index += 1
            screen.addString(screen.wininvent, index, 4, choices[index - 4], rainbow.white_bg)
            screen.addString(screen.wininvent, index - 1, 4, choices[index - 5], rainbow.white)
        elif input == 'KEY_UP' and index > 4:
            index -= 1
            screen.addString(screen.wininvent, index, 4, choices[index - 4], rainbow.white_bg)
            screen.addString(screen.wininvent, index + 1, 4, choices[index - 3], rainbow.white)
        elif input == '''
''':
            if index == 4:
                screen.winClear(screen.wininvent)
                getWeapon(stdscr, character)
                getDifficulty(stdscr, character)
                enter = True
            elif index == 5:
                enter = True
                screen.winClear(screen.wininvent)
                screen.winRefresh(screen.wininvent)
                tutorial(stdscr, character)
                screen.winClear(screen.wininvent)
                menu(stdscr, character)
            else:
                enter = True
                screen.winClear(screen.wininvent)
                screen.winRefresh(screen.wininvent)
                gameRules(character, stdscr)
        screen.winRefresh(screen.wininvent)

def gameRules(character, stdscr=False):
    rules = open('rules.txt', 'r')
    rules = rules.read()
    screen.addString(screen.wininvent, 0, 0, rules, rainbow.white)
    screen.addString(screen.wininvent, 8, 13, '%', rainbow.yellow)
    screen.addString(screen.wininvent, 9, 13, ')', rainbow.red)
    screen.addString(screen.wininvent, 10, 13, '(', rainbow.blue)
    screen.addString(screen.wininvent, 26, 2, "Press ENTER to exit.", rainbow.white)
    screen.winRefresh(screen.wininvent)
    if stdscr:
        enter = False
        while enter == False:
            input = stdscr.getkey()
            if input == """
""":
                enter = True
        screen.winClear(screen.wininvent)
        screen.winRefresh(screen.wininvent)
        menu(stdscr, character)

def initalisation(stdscr, character):
    getName(stdscr, character)
    menu(stdscr, character)

