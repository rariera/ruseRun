#!/usr/bin/env python3

from classes import Character
import curses

global character
character = Character(level = 1, pc = ('"', ord('"') & curses.A_COLOR), state = 'game', inventory = [])

def overlay():
    window3.touchwin()
    inventory()
    window3.refresh()

def checkAnswer(answer):
    '''decides what to do with the input'''
    if character.state == 'game':
        if answer == 'KEY_UP':
            moveChar('up')
        elif answer == 'KEY_DOWN':
            moveChar('down')
        elif answer == 'KEY_LEFT':
            moveChar('left')
        elif answer == 'KEY_RIGHT':
            moveChar('right')
        elif answer == 'g':
            pickUp()
        elif answer == 'i':
            overlay()
        elif answer == '''
''':
            interinit()
    elif character.state == 'inventory':
        pass

