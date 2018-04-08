#!/usr/bin/env python3

from interface import screen
from classes import LevelMonsters

level_monsters = LevelMonsters(lvl1 = [], lvl2 = [])

class Monster(object):
    def __init__(self, name, tile, colour, HP, y_coord, x_coord):
        self.name = name
        self.tile = tile
        self.colour = colour
        self.HP = HP
        self.map = map
        self.y_coord = y_coord
        self.x_coord = x_coord

goblin = Monster(name = 'goblin', tile = 'g', colour = rainbow.green, HP = 5, map = 2, y_coord = 20, x_coord = 20) 

zeroItems = []

def moveChoose(monster, y, x, character):
    monstery = abs(monster.y_coord - y)
    monsterx = abs(monster.x_coord - x)
    if monstery < monsterx and monstery != 1:
        if monster.y_coord - y < 0:
            moveMonster(monster, 'up')
        else:
            moveMonster(monster, 'down')
    elif monsterx < monstery and monsterx != 1:
        if monster.x_coord - x < 0:
            moveMonster(monster, 'right')
        else:
            moveMonster(monster, 'left')
    elif monstery = 1 and monsterx = 1:
        if y == screen.location['lrow'] + 6:
            attackPlayer(character, monster)
        else:
            monsPickup(monster, lvls.lvl1((y, x)))



def monstersUpdate(character, lvls):
    for i in lvls.lvl1:
        zeroItems.append(i)
    #zeroItems.append(character)
    if screen.location['lrow'] + 6 in range(monster.y_coord + 10, monster.y_coord - 10) or screen.location['lcol'] + 14 in range(monster.x_coord + 10, monster.x_coord - 10):
        moveChoose(monster, screen.location['lrow'] + 6, screen.location['lcol'] + 14, character)
    else:
        closest_item = zero_items[0]
        for i in zero_items:
            if monster.y_coord - closest_item[0] + monster.x_coord - closest_item[1] >  monster.y_coord - i[0] + monster.x_coord - i[1]:
                closest_item = i
        moveChoose(monster, closest_item[0], closest_item[1], character)

         
        #make list of x-coords including items + character (character must be differentiated) 

#make a list of all the '0' things (i.e. character, items, money, etc.)
#pick character IF character less than 10 squares away in any direction
#else, pick the closed 0 thing, and make way towards until can't any more
#if item, then pickup. If character, then attack

#moveMonster, monsPickup, attackPlayer, monsCreate

monsters = [goblin]

def monsterChoose(floorlist):
    '''Chooses which monster will be placed in which spot'''
    monsterplaces = []
    for key in floorlist.keys():
        x = 1
        n = 1
        for i in floorlist:
            num = randint(0, 100)
            if num == 0:
                itemplaces.append(i)
        for i in itemplaces:
            monster = [choice(monsters)]
            monster.y_coord = i[0]
            monster.x_coord = i[1]
           if x == 1:
                level_monsters.lvl1.append(monster)
            elif x == 2:
                level_monsters.lvl2.append(monster)
        x += 1
    return level_monsters

def monsterAdd():
    for key in level_monsters.keys():
        for monster in key:
            prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)

