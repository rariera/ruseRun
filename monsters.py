#!/usr/bin/env python3

from interface import Interface
from classes import LevelMonsters
from colours import Colour
from random import randint, choice, sample
from itemcmds import floorList

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

def moveChoose(monsterlist, closest_y, closest_x, character):
    monster = monsterlist[0]
    monstery = abs(monster.y_coord - closest_y) #number of moves up/down to reach @
    monsterx = abs(monster.x_coord - closest_x) #number of moves left/right to reach @
    proximity = monstery + monsterx #proximity is the number of moves to reach @
    if monstery > 1 or monsterx > 1:
        if monstery > monsterx:
            if monster.y_coord - closest_y < 0:
                moveMonster(monsterlist, 'up')
            else:
                moveMonster(monsterlist, 'down')
        elif monsterx > monstery:
            if monster.x_coord - closest_x < 0:
                moveMonster(monsterlist, 'right')
            else:
                moveMonster(monsterlist, 'left')
    #elif monstery == 1 and monsterx == 1:
     #   if closest_y == screen.location['lrow'] + 6:
      #      attackPlayer(character, monster)
       # else:
        #    monsPickup(monster, lvls.lvl1((y, x)))

def moveMonster(monsterlist, direction):
    monster = monsterlist[0]
    if direction == 'up':
        move = monsVerify(monster.y_coord - 1, monster.x_coord)
        if move == True:
            monster.y_coord -= 1
            screen.addChar(screen.pad, monster.y_coord + 1, monster.x_coord, monsterlist[1], rainbow.white)
    elif direction == 'down':
        move = monsVerify(monster.y_coord + 1, monster.x_coord)
        if move == True:
            monster.y_coord += 1
            screen.addChar(screen.pad, monster.y_coord - 1, monster.x_coord, monsterlist[1], rainbow.white)
    elif direction == 'left':
        move = monsVerify(monster.y_coord, monster.x_coord - 1)
        if move == True:
            monster.x_coord -= 1
            screen.addChar(screen.pad, monster.y_coord, monster.x_coord + 1, monsterlist[1], rainbow.white)
    elif direction == 'right':
        move = monsVerify(monster.y_coord, monster.x_coord + 1)
        if move == True:
            monster.x_coord += 1
            screen.addChar(screen.pad, monster.y_coord, monster.x_coord - 1, monsterlist[1], rainbow.white)
    del monsterlist[1]
    prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
    monsterlist.append(prev[0])
    screen.addChar(screen.pad, monster.y_coord, monster.x_coord, monster.tile, monster.colour)
    screen.padRefresh()

def monsVerify(y_coord, x_coord):
    place = screen.getChar(screen.pad, y_coord, x_coord)
    move = True
    if place[0] == '#':
        move = False
    return move


def monstersUpdate(character, level_monsters):
    if character.level == 1:
        level = level_monsters.lvl1
    else:
        level = level_monsters.lvl2
    floorlist = floorList()
    sampleSize = len(floorlist) / 100
    zeroItems = sample(floorlist, int(sampleSize))
    for monsterlist in level:
        monster = monsterlist[0]
        if screen.location['lrow'] + 6 in range(monster.y_coord - 50, monster.y_coord + 50) and screen.location['lcol'] + 14 in range(monster.x_coord - 50, monster.x_coord + 50):
            screen.addString(screen.wintest, 2, 2, 'monstersUpdate()', rainbow.red)
            screen.winRefresh(screen.wintest)
            if screen.location['lrow'] + 6 in range(monster.y_coord - 10, monster.y_coord + 10) or screen.location['lcol'] + 14 in range(monster.x_coord - 10, monster.x_coord + 10):
                moveChoose(monsterlist, screen.location['lrow'] + 6, screen.location['lcol'] + 14, character)
            else: 
                closest_item = zeroItems[0]
                for i in zeroItems:
                    if monsterlist[0].y_coord - closest_item[0] + monsterlist[0].x_coord - closest_item[1] >  monsterlist[0].y_coord - i[0] + monsterlist[0].x_coord - i[1]:
                        closest_item = i
                moveChoose(monsterlist, closest_item[0], closest_item[1], character)
    screen.addString(screen.wintest, 4, 2, 'End', rainbow.green)
    screen.winRefresh(screen.wintest)

         
        #make list of x-coords including items + character (character must be differentiated) 

#make a list of all the '0' things (i.e. character, items, money, etc.)
#pick character IF character less than 10 squares away in any direction
#else, pick the closed 0 thing, and make way towards until can't any more
#if item, then pickup. If character, then attack

#moveMonster, monsPickup, attackPlayer, monsCreate



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
        monster = Goblin(y_coord=x[0], x_coord=x[1])
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
    screen.padRefresh()

