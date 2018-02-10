#!/usr/bin/env python3

from classes import Character
import curses
from movement import moveChar
from interface import Interface
from itemcmds import pickUp, inventory


global character
character = Character(level = 1, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = [])

screen = Interface()

def overlay():
    screen.wininvent.touchwin()
    inventory(character)
    screen.winRefresh(screen.wininvent)

def checkAnswer(answer):
    '''decides what to do with the input'''
    if character.state == 'game':
        if answer == 'KEY_UP':
            moveChar(character, 'up')
        elif answer == 'KEY_DOWN':
            moveChar(character, 'down')
        elif answer == 'KEY_LEFT':
            moveChar(character, 'left')
        elif answer == 'KEY_RIGHT':
            moveChar(character, 'right')
        elif answer == 'g':
            pickUp(character)
        elif answer == 'i':
            overlay()
        elif answer == '''
''':
            screen.interinit()
    elif character.state == 'inventory':
        pass

