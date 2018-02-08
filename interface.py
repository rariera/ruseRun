#!/usr/bin/env python3

import curses


pad1 = curses.newpad(280, 280) #creating a window that is 40x40
window1 = curses.newwin(28, 30, 2, 40)
window2 = curses.newwin(15, 50, 31, 2)
window3 = curses.newwin(45, 70, 2, 2)


class Interface(object):
    def __init__(self):
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

    def padRefresh():
        pad1.refresh(self.location['lrow'], self.location['lcol'], self.location['pminrow'], self.location['pmincol'], self.location['pmaxrow'], self.location['pmaxcol'])
   
    def winRefresh(window):
        window.refresh()

    def getChar(window, y, x):
        window.inch(y, x)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
        return (char, color)
    
    def interinit():
        self.wininvent.erase()
        winRefresh(self.wininvent)
        self.winstatus.box()
        winRefresh(self.winstatus)
        self.windialogue.box()
        winRefresh(self.windialogue)

        padRefresh()       
