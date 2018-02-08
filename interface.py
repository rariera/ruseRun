#!/usr/bin/env python3

from random import randint
from curses import wrapper, ascii
import curses
from items import itemChoose
from colours import Colour

rainbow = Colour()

pad1 = curses.newpad(280, 280) #creating a window that is 40x40
window1 = curses.newwin(28, 30, 2, 40)
window2 = curses.newwin(15, 50, 31, 2)
window3 = curses.newwin(45, 70, 2, 2)

map = open('farm.txt', 'r')
gameMap = map.read()


map2 = open('map2.txt', 'r')
gameMap2 = map2.read()

class Interface(object):
    def __init__(self, location, pad, winstatus, windialogue, wininvent):
        self.location = {
    'lrow': 2,
    'lcol': 2,
    'pminrow': 5,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 30
    }
        self.pad = pad1
        self.winstatus = window1
        self.windialogue = window2
        self.wininvent = window3
    
    def addChar(window, y, x, char, colour):
        window.addch(y, x, char, colour)

    def addString(window, y, x, string, colour):
        window.addstr(y, x, string, colour)

    def padRefresh()
        pad1.refresh(self.location['lrow'], self.location['lcol'], self.location['pminrow'], self.location['pmincol'], self.location['pmaxrow'], self.location['pmaxcol'])
   
    def winRefresh(window):
        window.refresh()

    def getChar(window, y, x):
        window.inch(y, x)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
        return (char, color)


def interinit():
    window3.erase()
    window3.refresh()
    window1.box()
    window1.refresh()
    window2.box()
    window2.refresh()

    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

def overlay():
    window3.touchwin()
    inventory()
    window3.refresh()






def mapinit():
    '''Initialises the map and interface'''
    interinit()
    pad1.box()  #a box appears around the window
    pad1.addstr(0, 0, gameMap, rainbow.white)
    floorlist = floorList()
    global level_items
    level_items = itemChoose(floorlist)
    itemAdd()
    pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
    pad1.subpad(25, 25, 2, 2)
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])
    return level_items.lvl1






       
