#!/usr/bin/env python3

def floorList():
    '''Generates list of available floor spaces on this floor'''
    floorlist = {'level1': [], 'level2': []}
    for f in floorlist.keys():
        for i in range(-1, 280):
            for k in range(0, 280):
                item = screen.getChar(screen.pad, i, k)
                if item[0] == '.' or item[0] == '"':
                    loc = (i, k)
                    floorlist[f].append(loc)
    return floorlist

def itemChoose(floorlist):
    '''Chooses which item will be placed in which spot'''
    itemplaces = []
    for key in floorlist.keys():
        x = 1
        for i in key:
            num = randint(0, 100)
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
            if x == 1:
                level_items.lvl1[i] = [choice(list)]
            elif x == 2:
                level_items.lvl2[i] = [choice(list)]
        x += 1
    return level_items



def mapinit():
    '''Initialises the map and interface'''
    screen.interinit()
    screen.addString(screen.pad, 0, 0, gameMap1, rainbow.white)
    screen.padRefresh()
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist)
    itemAdd(level_items, 1)
    level_monsters = monsterChoose(floorlist)
    monsterAdd(level_monsters)
    screen.addChar(screen.pad, screen.location['lrow'] + 6, screen.location['lcol'] + 14, '@', rainbow.yellow_bg)
    screen.padRefresh()
    return level_items.lvl1


