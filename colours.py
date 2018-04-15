#!/usr/bin/env python3

import curses
class Colour(object):
    def __init__(self):
        curses.initscr()
        curses.start_color()

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_YELLOW)

        self.red = curses.color_pair(1)
        self.green = curses.color_pair(2)
        self.yellow = curses.color_pair(3)
        self.blue = curses.color_pair(4)
        self.magenta = curses.color_pair(5)
        self.cyan = curses.color_pair(6)
        self.white = curses.color_pair(7)
        self.yellow_bg = curses.color_pair(8)
 
