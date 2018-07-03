#!/usr/bin/env python3

from random import randint, uniform
from interface import Interface
from colours import Colour
import sys
from finder import levelm, directFind, reverseDirect

rainbow = Colour()
screen = Interface()


def playerAttack(character, direction, level_monsters):
    '''The player attacks the monster.'''
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
                damage = 0
            hits = damage + randint(0, 6)
            if character.difficulty == 1:
                num = 1.2
            elif character.difficulty == 2:
                num = 1
            elif character.difficulty == 3:
                num = 0.8
            else:
                num = uniform(0, 1.5)
            hits = int(hits * num)
            monster.HP = monster.HP - hits
            death = deathCheck(monster.HP, False)
            if death == True:
                monsterDeath(character, monsterl, level_monsters)

def deathCheck(health, char):
    '''The charater/monster is checked to make sure that they are not DEAD'''
    death = False
    if health <= 0:
        health = 0
        death = True
    elif health <= 5 and char == True:
        screen.addLine("* * *LOW HITPOINT WARNING* * *", rainbow.red)
    return death

def monsterDeath(character, monsterlist, level_monsters):
    '''function for monster death'''
    monster = monsterlist[0]
    prev = monsterlist[1]
    screen.addLine("You kill the " + monster.name, rainbow.red)
    screen.addChar(screen.pad, monster.y_coord, monster.x_coord, prev[0], prev[1])
    level = levelm(character.level, character.setting, level_monsters)
    level.remove(monsterlist)
    #print that monster is dead


def charDeath(character):
    '''Function for character death'''
    screen.addLine("You die...", rainbow.white)
    character.state = 'end'
    #Maybe print inventory now?

