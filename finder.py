#!/usr/bin/env python3

from interface import Interface

screen = Interface()

def directFind(direction):
    '''the character direction is translated into terms the computer can understand'''
    if direction == 'up':
        y = screen.location['lrow'] + 7
        x = screen.location['lcol'] + 14
    elif direction == 'down':
        y = screen.location['lrow'] + 5
        x = screen.location['lcol'] + 14
    elif direction == 'left':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 15
    elif direction == 'right':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 13
    return y, x

def levelm(character_level, character_setting, level_monsters):
    '''The monsters level is allocated'''
    if character_level == 1:
        if character_setting == 1:
            level = level_monsters.lvl1_1
        else:
            level = level_monsters.lvl1_2
    elif character_level == 2:
        if character_setting == 1:
            level = level_monsters.lvl2_1
        elif character_setting == 2:
            level = level_monsters.lvl2_2
        elif character_setting == 3:
            level = level_monsters.lvl2_3
        else:
            level = level_monsters.lvl2_4
    elif character_level == 3:
        if character_setting == 1:
            level = level_monsters.lvl3_1
        elif character_setting == 2:
            level = level_monsters.lvl3_2
        else:
            level = level_monsters.lvl3_3
    return level


def compass(direction):
    '''character location is changed'''
    if direction == 'up':
        screen.location['lrow'] -= 1
    elif direction == 'down':
        screen.location['lrow'] += 1
    elif direction == 'left':
        screen.location['lcol'] -= 1
    elif direction == 'right':
        screen.location['lcol'] += 1

def reverseDirect(direction):
    '''the direction is reversed'''
    if direction == 'up':
        rd = 'down'
    elif direction == 'down':
        rd = 'up'
    elif direction == 'left':
        rd = 'right'
    elif direction == 'right':
        rd = 'left'
    return rd

