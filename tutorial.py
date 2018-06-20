#!/usr/bin/env python3



tutorial1 = open('tutorial1.txt', 'r')
tutorial1 = tutorial1.read()

tutorial2 = open('tutorial2.txt', 'r')
tutorial2 = tutorial2.read()

tutorial3 = open('tutorial3.txt', 'r')
tutorial3 = tutorial3.read()


list = []
def tutorial(stdscr, character):
    #erase screen
    screen.addString(screen.pad, 0, 0, tutorial1, rainbow.white)
    screen.addLine("Welcome to the tutorial.", rainbow.white)
    screen.addLine("Let's get started - move around using the arrow keys", rainbow.white)

    #open up pad and put in first tutorial map
    #open comments and write something welcoming
    #write something about moving around
    #refresh everything
    #begin loop
    #get input
    #up, down, right, left, inventory will be normal
