#!/usr/bin/env python3



def directFind(direction):
    if direction == 'up':
        y = screen.location['lrow'] + 5
        x = screen.location['lcol'] + 14
    elif direction == 'down':
        y = screen.location['lrow'] + 7
        x = screen.location['lcol'] + 14
    elif direction == 'left':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 13
    elif direction == 'right':
        y = screen.location['lrow'] + 6
        x = screen.location['lcol'] + 15
    return y, x




def playerAttack(character, direction, level_monsters):
            

