#!/usr/bin/env python3

from interface import Interface
import time
import sys
from colours import Colour
import curses
from items import quipChar
import string

screen = Interface()
rainbow = Colour()

def end(character):
    print("The end is nigh!!!!")
    screen.overlay()
    maxyx = screen.getMax(screen.wininvent)
    y = maxyx[0]
    screen.addString(screen.wininvent, int(y / 2), 2, 'Congratulations! you win!!', rainbow.yellow)
    screen.winRefresh(screen.wininvent)
    time.sleep(10) 
    sys.exit("Yay! You win!")

def beginning(stdscr):
    screen.overlay()
    logo = open('ruseRun2.txt', 'r')
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

def getTutorial(stdscr, character):
    pass

def initalisation(stdscr, character):
    getName(stdscr, character)
    getWeapon(stdscr, character)
    getDifficulty(stdscr, character)
