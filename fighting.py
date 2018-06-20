#!/usr/bin/env python3

from random import randint
from interface import Interface
from colours import Colour
import sys

rainbow = Colour()
screen = Interface()

def directFind(direction):
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

def leveli(character_level, character_setting, level_items):
    if character_level == 1:
        if character_setting == 1:
            level = level_items.lvl1_1
        else:
            level = level_items.lvl1_2
    elif character_level == 2:
        if character_setting == 1:
            level = level_items.lvl2_1
        elif character_setting == 2:
            level = level_items.lvl2_2
        elif character_setting == 3:
            level = level_items.lvl2_3
        else:
            level = level_items.lvl2_4
    else:
        if character_setting == 1:
            level = level_items.lvl3_1
        elif character_setting == 2:
            level = level_items.lvl3_2
        else:
            level = level_items.lvl3_3
    return level

def compass(direction):
    if direction == 'up':
        screen.location['lrow'] -= 1
    elif direction == 'down':
        screen.location['lrow'] += 1
    elif direction == 'left':
        screen.location['lcol'] -= 1
    elif direction == 'right':
        screen.location['lcol'] += 1

def reverseDirect(direction):
    if direction == 'up':
        rd = 'down'
    elif direction == 'down':
        rd = 'up'
    elif direction == 'left':
        rd = 'right'
    elif direction == 'right':
        rd = 'left'
    return rd

def playerAttack(character, direction, level_monsters):
    rd = reverseDirect(direction) 
    xy = directFind(rd)
    y = xy[0]
    x = xy[1]
    monster = False
    level = levelm(character.level, character.setting, level_monsters)
    monsterl = False
    for monsterlist in level:
        if monsterlist[0].y_coord == y and monsterlist[0].x_coord == x:
            monsterl = monsterlist
    if monsterl:
        monster = monsterl[0]
        if randint(0, 2) == 0:
            #miss monster
            screen.addLine("You missed the " + monster.name, rainbow.white)
        else:
            #hit monster
            screen.addLine("You strike the " + monster.name, rainbow.white)
            if character.equipment['weapon']:
                damage = character.equipment['weapon'].damage
            else:
                damage = 3
            hits = damage + randint(0, 5)
            monster.HP = monster.HP - hits
            death = deathCheck(monster, monster.HP, False)
            if death == True:
                monsterDeath(character, monsterl, level_monsters)

def deathCheck(being, health, char):
    death = False
    if health <= 0:
        health = 0
        death = True
    elif health <= 5 and char == True:
        screen.addLine("* * *LOW HITPOINT WARNING* * *", rainbow.red)
    return death

def monsterDeath(character, monsterlist, level_monsters):
    monster = monsterlist[0]
    prev = monsterlist[1]
    screen.addLine("You kill the " + monster.name, rainbow.red)
    screen.addChar(screen.pad, monster.y_coord, monster.x_coord, prev[0], prev[1])
    level = levelm(character.level, character.setting, level_monsters)
    level.remove(monsterlist)
    #print that monster is dead

def charDeath(character):
    screen.addLine("You die...", rainbow.white)
    sys.exit("You died. Better luck next time!")
    #Maybe print inventory now?


