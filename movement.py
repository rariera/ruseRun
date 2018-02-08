#!/usr/bin/env python3


def verify(direction):
    if direction == 'up':
        attrs = pad1.inch(location['lrow'] + 5, location['lcol'] + 14)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'down':
        attrs = pad1.inch(location['lrow'] + 7, location['lcol'] + 14)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'left':
        attrs = pad1.inch(location['lrow'] + 6, location['lcol'] + 13)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    elif direction == 'right':
        attrs = pad1.inch(location['lrow'] + 6, location['lcol'] + 15)
        char = chr(attrs & curses.A_CHARTEXT)
        color = attrs & curses.A_COLOR
    if char == '+':
        pad1.erase()
        if character.level == 1:
            pad1.addstr(0, 0, gameMap2)
            character.level = 2
        elif character.level == 2:
            pad1.addstr(0, 0, gameMap)
            character.level = 1
    item = (char, color)
    return item
        
def moveChar(direction):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        item = verify(direction)
        if item[0] != '#':
            location['lrow'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg) 
            pad1.addch(location['lrow'] + 7, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'down':
        item = verify(direction)
        if item[0] != '#':
            location['lrow'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 5, location['lcol'] + 14, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'left':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] -= 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 6, location['lcol'] + 15, character.pc[0], character.pc[1])
            character.pc = item
    elif direction == 'right':
        item = verify(direction)
        if item[0] != '#':
            location['lcol'] += 1
            pad1.addch(location['lrow'] + 6, location['lcol'] + 14, '@', rainbow.yellow_bg)
            pad1.addch(location['lrow'] + 6, location['lcol'] + 13, character.pc[0], character.pc[1])
            character.pc = item
    pad1.refresh(location['lrow'], location['lcol'], location['pminrow'], location['pmincol'], location['pmaxrow'], location['pmaxcol'])

