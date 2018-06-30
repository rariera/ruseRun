#!/usr/bin/env python3

from random import randint, choice
from colours import Colour
from classes import LevelItems

rainbow = Colour()
level_items = LevelItems(lvl1_1 = {}, lvl1_2 = {}, lvl2_1 = {}, lvl2_2 = {}, lvl2_3 = {}, lvl2_4 = {}, lvl3_1 = {}, lvl3_2 = {}, lvl3_3 = {})

class Item(object): 
    def __init__(self, name, tile, colour, type, letter):
        self.name = name
        self.tile = tile
        self.colour = colour
        self.type = type
        self.letter = letter

class Food(Item):
    def __init__(self, name, tile, colour, type, letter,  hunger):
        Item.__init__(self, name, tile, colour, type, letter)
        self.hunger = hunger

class Weapon(Item):
    def __init__(self, name, tile, colour, type, letter, damage):
        Item.__init__(self, name, tile, colour, type, letter)
        self.damage = damage

class Armour(Item):
    def __init__(self, name, tile, colour, type, letter, hp):
        Item.__init__(self, name, tile, colour, type, letter)
        self.hp = hp

class Orange(Food):
    def __init__(self, name='orange', tile='%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 11):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Pizza(Food):
    def __init__(self, name = 'slice of pizza', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 9):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Ramen(Food):
    def __init__(self, name = 'ramen', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 8):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Sandwich(Food):
    def __init__(self, name = 'sandwich', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 13):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Oreos(Food):
    def __init__(self, name = 'oreos', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 7):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Spaghetti(Food):
    def __init__(self, name = 'spaghetti bolognaise', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 14):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Chocolate(Food):
    def __init__(self, name = 'chocolate', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 10):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class ButterChicken(Food):
    def __init__(self, name = 'butter chicken', tile = '%', colour = rainbow.yellow, type = 'food', letter = '!', hunger = 10):
        Food.__init__(self, name, tile, colour, type, letter, hunger)

class Branch(Weapon):
    def __init__(self, name = 'branch', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 3):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Football(Weapon):
    def __init__(self, name = 'football', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 5):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Textbook(Weapon):
    def __init__(self, name = 'maths textbook', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 6):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Hoe(Weapon):
    def __init__(self, name = 'hoe', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 8):
        Weapon.__init__ (self, name, tile, colour, type, letter, damage)

class Chisel(Weapon):
    def __init__(self, name = 'chisel', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 7):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Saw(Weapon):
    def __init__(self, name = 'saw', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 6):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Ruler(Weapon):
    def __init__(self, name = 'ruler', tile = ')', colour = rainbow.red, type = 'weaponry', letter = '!', damage = 5):
        Weapon.__init__(self, name, tile, colour, type, letter, damage)

class Blazer(Armour):
    def __init__(self, name = 'blazer', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 3):
        Armour.__init__(self, name, tile, colour, type, letter, hp)

class Cardboard(Armour):
    def __init__(self, name = 'cardboard box', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 4):
        Armour.__init__(self, name, tile, colour, type, letter, hp)

class SheetMetal(Armour):
    def __init__(self, name = 'sheet metal', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 7):
        Armour.__init__(self, name, tile, colour, type, letter, hp)

class ShinPads(Armour):
    def __init__(self, name = 'shin pads', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 6):
        Armour.__init__(self, name, tile, colour, type, letter, hp)

class Helmet(Armour):
    def __init__(self, name = 'bike helmet', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 8):
        Armour.__init__(self, name, tile, colour, type, letter, hp)

class Jersey(Armour):
    def __init__(self, name = 'senior jersey', tile = '(', colour = rainbow.blue, type = 'armour', letter = '!', hp = 9):
        Armour.__init__(self, name, tile, colour, type, letter, hp)


itemdict = {
        'food': [Orange(), Pizza(), Ramen(), Sandwich(), Oreos(), Spaghetti(), ButterChicken(), Chocolate()],
        'weapons': [Branch(), Football(), Textbook(), Hoe(), Chisel(), Saw(), Ruler()],
        'armour': [Blazer(), Cardboard(), SheetMetal(), ShinPads(), Helmet(), Jersey()]
        }

def quipChar(character):
    if character.equipment['weapon'] == 2:
        item = Branch()
        itemdict['weapons'].pop(0)
    elif character.equipment['weapon'] == 3:
        item = Football()
        itemdict['weapons'].pop(1)
    character.equipment['weapon'] = item
    character.inventory['weaponry'].append(item)
    character.equipment['weapon'].letter = character.alphanum[0]
    character.alphanum.remove(character.equipment['weapon'].letter)

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

def itemChoose(floorlist, charlvl, charset):
    '''Chooses which item will be placed in which spot'''
    itemplaces = []
    for i in floorlist:
        num = randint(0, 450)
        if num == 0:
            itemplaces.append(i)
    for i in itemplaces:
        listnum = randint(0, 2)
        if listnum == 0:
            list = itemdict['food']
        elif listnum == 1:
            list = itemdict['weapons']
        elif listnum == 2:
            list = itemdict['armour']
        level = leveli(charlvl, charset, level_items)
        level[i] = [choice(list)]
    return level_items

