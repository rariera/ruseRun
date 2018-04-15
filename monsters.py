#!/usr/bin/env python3

from interface import Interface
from classes import LevelMonsters
from colours import Colour
from random import randint, choice


rainbow = Colour()
screen = Interface()
level_monsters = LevelMonsters(lvl1 = [], lvl2 = [])

class Monster(object):
    def __init__(self, y_coord, x_coord, name, tile, colour, HP, map):
        self.y_coord = y_coord
        self.x_coord = x_coord
        self.name = name
        self.tile = tile
        self.colour = colour
        self.HP = HP
        self.map = map

class Goblin(Monster):
    def __init__(self, y_coord, x_coord, name='goblin', tile='g', colour=rainbow.green, HP=5, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, map)

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
    elif monstery == 1 and monsterx == 1:
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


#goblin = Monster(name = 'goblin', tile = 'g', colour = rainbow.green, HP = 5, map = 2, y_coord = 20, x_coord = 20) 
#monsters = [goblin]

def monsterChoose(floorlist, charlvl, density=75):
    '''Chooses which monster will be placed in which spot'''
    monsterplaces = []
    if charlvl == 1:
        level = level_monsters.lvl1
    else:
        level = level_monsters.lvl2
    for i in floorlist:
        num = randint(0, density)
        if num == 1:
             monsterplaces.append(i) 
    for x in monsterplaces:
#       monster = choice(monsters)
        monster = Goblin(y_coord=x[0], x_coord=x[1])
#       monster.y_coord = x[0]
#       monster.x_coord = x[1]
        monsterlist = [monster]
        level.append(monsterlist)
    return level_monsters

def monsterAdd(level_monsters, charlvl):
    if charlvl == 1:
        level = level_monsters.lvl1
    else:
        level = level_monsters.lvl2
    x = 0
    for monsterlist in level:
        x += 1
        monster = monsterlist[0]
        prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
        monsterlist.append(prev[0])
        screen.addChar(screen.pad, monster.y_coord, monster.x_coord, monster.tile, monster.colour)
    screen.addString(screen.wintest, 2, 2, str(x), rainbow.cyan)
    screen.winRefresh(screen.wintest)
    screen.padRefresh()

