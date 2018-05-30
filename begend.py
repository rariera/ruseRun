#!/usr/bin/env python3

from interface import Interface
import time
import sys
from colours import Colour
import curses

screen = Interface()
rainbow = Colour()

def end(character):
    print("The end is nigh!!!!")
    screen.overlay()
    maxyx = screen.getMax(screen.wininvent)
    y = maxyx[0]
    screen.addString(screen.wininvent, int(y / 2), 2, 'Congratulations! you win!!', rainbow.yellow)
    screen.winRefresh(screen.wininvent)
    time.sleep(10) 
    sys.exit("Yay! You win!")

def beginning(stdscr):
    screen.overlay()
    logo = open('ruseRun2.txt', 'r')
    logo = logo.read()
    screen.addString(screen.wininvent, 1, 2, logo, rainbow.white)
    maxyx = screen.getMax(screen.wininvent)
    x = maxyx[1]
    screen.addString(screen.wininvent, 43, int(x/2) - 8, '[PRESS ENTER]', rainbow.green)
    screen.winRefresh(screen.wininvent)
    enter = False
    while enter == False:
        input = stdscr.getkey()
        if input == '''
''':
            enter = True
    #overlay, bring up logo & [press ENTER], when enter is pressed, finish function


