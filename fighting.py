#!/usr/bin/env python3

from random import randint
from interface import Interface
from colours import Colour
from monsters import monsterDeath

rainbow = Colour()
screen = Interface()

def directFind(direction):
    if direction == 'up':
        y = screen.location['lrow'] + 5
        x = screen.location['lcol'] + 14
    elif direction == 'down':
        y = screen.location['lrow'] + 7
        x = screen.location['lcol'] + 14
    elif direction == 'left':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 13
    elif direction == 'right':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 15
    return y, x




def playerAttack(character, direction, level_monsters):
    xy = directFind(direction)
    y = xy[0]
    x = xy[1]
    monster = False
    if character.level == 1:
        level = level_monsters.lvl1
    else:
        level = level_monsters.lvl2
    for monsterlist in level:
        if monsterlist[0].y_coord == y and monsterlist[0].x_coord == x:
            monsterl = monsterlist
    if monsterl:
        monster = monsterlist[0]
        if randint(0, 2) == 0:
            #miss monster
            screen.addLine("You missed the " + monster.name, rainbow.magenta)
        else:
            #hit monster
            screen.addLine("You strike the " + monster.name, rainbow.green)
            if character.equipment['weapon']:
                damage = character.equipment['weapon'].damage
            else:
                damage = 3
            hits = damage + randint(0, 5)
            monster.HP = monster.HP - hits
            death = deathCheck(monster, monster.HP)
            if death == True:
                monsterDeath(character, monsterl, level_monsters)

def deathCheck(being, health):
    death = False
    if health <= 0:
        health = 0
        death = True
    return death
