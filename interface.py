#!/usr/bin/env python3

import curses

curses.initscr()
pad1 = curses.newpad(330, 410) #creating a window that is 40x40
window1 = curses.newwin(28, 30, 2, 40)
window2 = curses.newwin(15, 50, 31, 2)
window3 = curses.newwin(45, 70, 2, 2)
window4 = curses.newwin(45, 100, 2, 75)

class Interface(object):
    location = {
    'lrow': 60,
    'lcol': 2,
    'pminrow': 5,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 30
    }
    pad = pad1
    winstatus = window1
    windialogue = window2
    wininvent = window3
    wintest = window4
    
    def addChar(cls, window, y, x, char, colour):
        window.addch(y, x, char, colour)

    def addString(cls, window, y, x, string, colour):
        window.addstr(y, x, string, colour)

    def padRefresh(cls):

        pad1.refresh(cls.location['lrow'], cls.location['lcol'], cls.location['pminrow'], cls.location['pmincol'], cls.location['pmaxrow'], cls.location['pmaxcol'])
   
    def winRefresh(cls, window):
        window.refresh()

    def getChar(cls, window, y, x):
        attrs = window.inch(y, x)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
        return (char, color)
    
    def interinit(cls):
        cls.wininvent.erase()
        cls.wininvent.refresh()
        cls.winstatus.box()
        cls.winstatus.refresh()
        cls.windialogue.box()
        cls.windialogue.refresh()
        cls.wintest.box()
        cls.wintest.refresh()

        cls.padRefresh()

    def winClear(cls, window):
        window.erase()
