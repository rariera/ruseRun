#!/usr/bin/env python3

from interface import Interface
from classes import LevelMonsters
from colours import Colour
from random import randint, choice, sample, uniform
from itemcmds import floorList
import string
from fighting import deathCheck, charDeath
from finder import levelm

rainbow = Colour()
screen = Interface()
level_monsters = LevelMonsters(lvl1_1 = [], lvl1_2 = [], lvl2_1 = [], lvl2_2 = [], lvl2_3 = [], lvl2_4 = [], lvl3_1 = [], lvl3_2 = [], lvl3_3 = [])

class Monster(object):
    def __init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map):
        self.y_coord = y_coord
        self.x_coord = x_coord
        self.name = name
        self.tile = tile
        self.colour = colour
        self.HP = HP
        self.attack = attack
        self.map = map

class Goblin(Monster):
    def __init__(self, y_coord, x_coord, name='goblin', tile='g', colour=rainbow.green, HP=5, attack = 6, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Cow(Monster):
    def __init__(self, y_coord, x_coord, name='cow', tile='c', colour=rainbow.green, HP=20, attack = 2, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Rat(Monster):
    def __init__(self, y_coord, x_coord, name='rat', tile='r', colour=rainbow.green, HP=9, attack = 8, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Kobold(Monster):
    def __init__(self, y_coord, x_coord, name='kobold', tile='k', colour=rainbow.yellow, HP=10, attack = 5, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Bull(Monster):
    def __init__(self, y_coord, x_coord, name='bull', tile='b', colour=rainbow.yellow, HP=13, attack = 10,  map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Adder(Monster):
    def __init__(self, y_coord, x_coord, name='adder', tile='a', colour=rainbow.yellow, HP=14, attack = 12, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Chicken(Monster):
    def __init__(self, y_coord, x_coord, name='giant chicken', tile='C', colour=rainbow.red, HP=30, attack = 10, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)

class Ogre(Monster):
    def __init__(self, y_coord, x_coord, name='ogre', tile='O', colour=rainbow.red, HP=20, attack = 19, map=2):
        Monster.__init__(self, y_coord, x_coord, name, tile, colour, HP, attack, map)


zeroItems = []

def moveChoose(monsterlist, closest_y, closest_x, character):
    '''The move that the monster takes is chosen'''
    monster = monsterlist[0]
    monstery = abs(monster.y_coord - closest_y) #number of moves up/down to reach @
    monsterx = abs(monster.x_coord - closest_x) #number of moves left/right to reach @
    proximity = monstery + monsterx #proximity is the number of moves to reach @
    if monstery > 1 or monsterx > 1:
        if monstery > monsterx or monstery == monsterx:
            if monster.y_coord - closest_y < 0:
                moveMonster(monsterlist, 'down')
            elif monster.y_coord - closest_y > 0:
                moveMonster(monsterlist, 'up')
        elif monsterx > monstery:
            if monster.x_coord - closest_x < 0:
                moveMonster(monsterlist, 'right')
            elif monster.x_coord - closest_x > 0:
                moveMonster(monsterlist, 'left')
    elif monstery <= 1 and monsterx <= 1:
        if closest_y == screen.location['lrow'] + 6:
            monsterAttack(character, monsterlist)

def moveMonster(monsterlist, direction):
    '''The monster is actually moved'''
    monster = monsterlist[0]
    previous = monsterlist[1]
    if direction == 'up':
        move = monsVerify(monster.y_coord - 1, monster.x_coord)
        if move == True:
            monster.y_coord -= 1
            screen.addChar(screen.pad, monster.y_coord + 1, monster.x_coord, previous[0], previous[1])
            del monsterlist[1]
            prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
            monsterlist.append(prev)
    elif direction == 'down':
        move = monsVerify(monster.y_coord + 1, monster.x_coord)
        if move == True:
            monster.y_coord += 1
            screen.addChar(screen.pad, monster.y_coord - 1, monster.x_coord, previous[0], previous[1])
            del monsterlist[1]
            prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
            monsterlist.append(prev)
    elif direction == 'left':
        move = monsVerify(monster.y_coord, monster.x_coord - 1)
        if move == True:
            monster.x_coord -= 1
            screen.addChar(screen.pad, monster.y_coord, monster.x_coord + 1, previous[0], previous[1])
            del monsterlist[1]
            prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
            monsterlist.append(prev)
    elif direction == 'right':
        move = monsVerify(monster.y_coord, monster.x_coord + 1)
        if move == True:
            monster.x_coord += 1
            screen.addChar(screen.pad, monster.y_coord, monster.x_coord - 1, previous[0], previous[1])
            del monsterlist[1]
            prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
            monsterlist.append(prev)
    screen.addChar(screen.pad, monster.y_coord, monster.x_coord, monster.tile, monster.colour)
    screen.padRefresh()

def monsVerify(y_coord, x_coord):
    '''The monster movement is verified'''
    place = screen.getChar(screen.pad, y_coord, x_coord)
    move = False
    if place[0] in ['"', '.', ' ', '/', 'I', '-', '_', 'P'] or place[0] not in string.ascii_letters and place[0] != '#':
        move = True
    return move


def monstersUpdate(character, level_monsters):
    '''The monsters are updated'''
    level = levelm(character.level, character.setting, level_monsters) 
    floorlist = floorList()
    sampleSize = len(floorlist) / 100
    zeroItems = sample(floorlist, int(sampleSize))
    for monsterlist in level:
        monster = monsterlist[0]
        if screen.location['lrow'] + 6 in range(monster.y_coord - 30, monster.y_coord + 30) and screen.location['lcol'] + 14 in range(monster.x_coord - 30, monster.x_coord + 30):
            if screen.location['lrow'] + 6 in range(monster.y_coord - 10, monster.y_coord + 10) or screen.location['lcol'] + 14 in range(monster.x_coord - 10, monster.x_coord + 10):
                moveChoose(monsterlist, screen.location['lrow'] + 6, screen.location['lcol'] + 14, character)
            else: 
                closest_item = zeroItems[0]
                for i in zeroItems:
                    if monsterlist[0].y_coord - closest_item[0] + monsterlist[0].x_coord - closest_item[1] >  monsterlist[0].y_coord - i[0] + monsterlist[0].x_coord - i[1]:
                        closest_item = i
                moveChoose(monsterlist, closest_item[0], closest_item[1], character)


def monsterChoose(floorlist, charlvl, charset, density=500):
    '''Chooses which monster will be placed in which spot'''
    monsterplaces = []
    level = levelm(charlvl, charset, level_monsters) 
    for i in floorlist:
        num = randint(0, density)
        if num == 1:
             monsterplaces.append(i) 
    for x in monsterplaces:
        ranges = [[Goblin(y_coord = x[0], x_coord = x[1]), Cow(y_coord = x[0], x_coord = x[1]), Rat(y_coord = x[0], x_coord = x[1])], [Kobold(y_coord = x[0], x_coord = x[1]), Adder(y_coord = x[0], x_coord = x[1]), Bull(y_coord = x[0], x_coord = x[1])], [Chicken(y_coord = x[0], x_coord = x[1]), Ogre(y_coord = x[0], x_coord = x[1])]]
        num = randint(0, 151)
        if num in range(0, 100):
            monster = choice(ranges[0])
        elif num in range(100, 150):
            monster = choice(ranges[1])
        else:
            monster = choice(ranges[2])
        monsterlist = [monster]
        level.append(monsterlist)
    return level_monsters

def monsterAdd(level_monsters, charlvl, charset):
    '''The monsters are added to the map (for the first time)'''
    level = levelm(charlvl, charset, level_monsters)
    x = 0
    for monsterlist in level:
        x += 1
        monster = monsterlist[0]
        prev = screen.getChar(screen.pad, monster.y_coord, monster.x_coord)
        monsterlist.append(prev)
        screen.addChar(screen.pad, monster.y_coord, monster.x_coord, monster.tile, monster.colour)
    screen.padRefresh()

def monsterAttack(character, monsterlist):
    '''The monsters attack the player'''
    monster = monsterlist[0]
    num = randint(0, 10)
    if num in [0, 1]:
        screen.addLine("The " + monster.name + " missed you.", rainbow.white)
    elif num in [2, 3]: 
        screen.addLine("The " + monster.name + " hit you but did no damage", rainbow.white)
    else:
        screen.addLine("The " + monster.name + " hit you.", rainbow.white)
        hits = monster.attack + randint(-2, 2)
        if character.difficulty == 1:
            num = 0.8
        elif character.difficulty == 2:
            num = 1
        elif character.difficulty == 3:
            num = 1.2
        else:
            num = uniform(0, 1.5)
        hits = int(hits * num)
        character.HP = character.HP - hits
        death = deathCheck(character.HP, True)
        if death == True:
            charDeath(character)
    

