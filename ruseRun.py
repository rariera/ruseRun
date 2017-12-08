from curses import wrapper
import curses

class Character(object):
    def __init__(self, pc, cur_y, cur_x):
        self.pc = pc
        self.cur_y = cur_y
        self.cur_x = cur_x

character = Character(pc = '.', cur_y = 2, cur_x = 2)

def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.initscr()
    window = curses.newwin(15, 30, 1, 1) #creating a window that is 15x30
    window.box()  #a box appears around the window
    gameMap = '''.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................
.............................'''
    window.addstr(0, 0, gameMap)
    stdscr.refresh()
    while True:
        window.addch(character.cur_y, character.cur_x , '@')
        window.refresh()
        answer = stdscr.getkey()    #input a key
        checkAnswer(answer, window)
        window.refresh()
        


def checkAnswer(answer, window):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up', window)
    elif answer == 'KEY_DOWN':
        moveChar('down', window)
    elif answer == 'KEY_LEFT':
        moveChar('left', window)
    elif answer == 'KEY_RIGHT':
        moveChar('right', window)
    
def moveChar(direction, window):
    '''Moves the character symbol in accordance with the direction.'''
    if direction == 'up':
        character.pc = window.getch(character.cur_y - 1, character.cur_x)   #gets the character previously in the space, so it can be replaced later.
        #window.addstr(character.cur_y, character.cur_x, str(character.pc))
        #character.cur_y -= 1
    elif direction == 'down':
        character.pc = window.inch(character.cur_y + 1, character.cur_x)
        window.addstr(character.cur_y, character.cur_x, str(character.pc))
        character.cur_y += 1
    elif direction == 'left':
        character.pc = window.instr(character.cur_y, character.cur_x - 1, 1)
        window.addstr(character.cur_y, character.cur_x, str(character.pc))
        character.cur_x -= 1
    elif direction == 'right':
        character.pc = window.instr(character.cur_y, character.cur_x + 1, 1)
        print(character.pc)
        window.addstr(character.cur_y, character.cur_x, str(character.pc))
        character.cur_x += 1
        

    

wrapper(main)