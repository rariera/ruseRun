#!/usr/bin/env python3

import curses
import textwrap

stdscr = curses.initscr()
pad1 = curses.newpad(340, 430)
window1 = curses.newwin(28, 45, 2, 68)
window2 = curses.newwin(14, 70, 33, 2)
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
        textwrap.wrap(line, 67)
        cls.windialogue.addstr(11, 1, line, colour)
        empty = False
        while empty == False:
            ch = cls.getChar(cls.windialogue, 11, 1)
            if ch[0] == ' ':
                empty = True
            else:
                cls.windialogue.scroll(1)
        cls.windialogue.refresh()

    def addNstr(cls, window, y, x, line, n, colour):
        window.addnstr(y, x, line, n, colour)
        window.refresh()

    def interinit(cls):
        cls.wininvent.erase()
        cls.wininvent.refresh()
        cls.winstatus.border('|', '|', '-', '-', '+', '+', '+', '+')
        cls.winstatus.refresh() 
        cls.windialogue.touchwin()
        cls.windialogue.refresh()
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

    def reset(cls):
        '''Cleanup before terminating'''
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()

