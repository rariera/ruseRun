from curses import wrapper, panel
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
    panelinit()
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
    window1.addstr(0, 0, gameMap)
    while True:
        #window3.addch(character.cur_y, character.cur_x , '@')
        #window3.refresh()
        answer = stdscr.getkey()    #input a key
        #checkAnswer(answer, window3)
        #window3.refresh()
        

def panelinit():
    window1 = curses.newwin(15, 30, 1, 1) #creating a window that is 15x30
    window1.erase()
    back_panel = panel.new_panel(window1)   #make a panel for the first window
    back_panel.top()
    window2 = curses.newwin(15, 30, 1, 1)   #creating a second window
    middle_panel = panel.new_panel(window2)
    window3 = curses.newwin(15, 30, 1, 1)
    front_panel = panel.new_panel(window3)
    window1.box()  #a box appears around the window
    panel.update_panels()
    doupdate()

def checkAnswer(answer, window3):
    '''decides what to do with the input'''
    if answer == 'KEY_UP':
        moveChar('up', window3)
    elif answer == 'KEY_DOWN':
        moveChar('down', window3)
    elif answer == 'KEY_LEFT':
        moveChar('left', window3)
    elif answer == 'KEY_RIGHT':
        moveChar('right', window3)


        
def moveChar(direction, window3):
    '''Moves the character symbol in accordance with the direction.'''
    window3.delch(character.cur_y, character.cur_x)
    if direction == 'up':
        character.cur_y -= 1
    elif direction == 'down':
        character.cur_y += 1
    elif direction == 'left':
        character.cur_x -= 1
    elif direction == 'right':
        character.cur_x += 1
        

    

wrapper(main)