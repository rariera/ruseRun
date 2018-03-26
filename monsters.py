m!/usr/bin/env python3

from interface import screen

zeroItems = []

def monstersUpdate(character, lvls):
    for i in lvls.lvl1:
        zeroItems.append(i)
    #zeroItems.append(character)
    if screen.location['lrow'] + 6 in range(monster[locationy] + 10, monster[locationy - 10]) or screen.location['lcol'] + 14 in range(monster[locationx] + 10, monster[locationx] - 10]):
        monstery = monster[locationy] - screen.location['lrow'] - 6
        monsterx = monster[locationx] - screen.location['lcol'] - 14
        if abs(monstery) < abs(monsterx) and monsterx != 0:
            if monsterx > 0:
                moveMonster(monster, down)
            elif monsterx < 0:
                moveMonster(monster, up)
        elif abs(monsterx) < abs(monstery) and monstery != 0:
            if monsterx > 0:
                moveMonster(monster, left)
            elif monsterx < 0:
                moveMonster(monster, right)
        else:
            ATTACK!!!!


#make a list of all the '0' things (i.e. character, items, money, etc.)
#pick character IF character less than 10 squares away in any direction
#else, pick the closed 0 thing, and make way towards until can't any more
#if item, then pickup. If character, then attack
