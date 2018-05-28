#!/usr/bin/env python3

from interface import Interface
import time
import sys
from colours import Colour

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
