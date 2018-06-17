#!/usr/bin/env python3

import curses

curses.initscr()
pad1 = curses.newpad(340, 430)
window1 = curses.newwin(28, 39, 2, 68)
window2 = curses.newwin(15, 50, 31, 2)
window3 = curses.newwin(48, 124, 2, 2)
window4 = curses.newwin(45, 100, 2, 75)

class Interface(object):
    location = {
    'lrow': 60,
    'lcol': 2,
    'pminrow': 3,
    'pmincol': 5,
    'pmaxrow': 30,
    'pmaxcol': 58
    }
    pad = pad1
    winstatus = window1
    windialogue = window2
    wininvent = window3
    wintest = window4
    
    def addChar(cls, window, y, x, char, colour):
        window.addch(y, x, char, colour)

    def vline(cls, y, x):
        cls.pad.vline(y, x, ' ', 10)
        cls.padRefresh()

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
    
    def addLine(cls, line, colour):
        cls.windialogue.scrollok(True)
        cls.windialogue.addstr(12, 2, line, colour)
        cls.windialogue.scroll(1)
        cls.windialogue.refresh()

    def addNstr(cls, window, y, x, line, n, colour):
        window.addnstr(y, x, line, n, colour)
        window.refresh()

    def interinit(cls):
        cls.wininvent.erase()
        cls.wininvent.refresh()
        cls.winstatus.box()
        cls.winstatus.refresh()
        cls.windialogue.refresh()
#        cls.wintest.refresh()
        cls.padRefresh()

    def overlay(cls):
        cls.wininvent.erase()
        cls.wininvent.touchwin()
        cls.wininvent.refresh()   

    def getMax(cls, window):
        maxyx = window.getmaxyx()
        return maxyx

    def touchWin(cls, window):
        window.touchwin()

    def winClear(cls, window):
        window.erase()
