from curses import wrapper
import curses
def main(stdscr):
    '''The main function which will run throughout the game.'''
    curses.initscr()
    window = curses.newwin(15, 30, 1, 1) #creating a window that is 15x15
    window.box()  #a box appears around the window
    gameMap = '''
####################
###.#...############
###.#.#.############
###.#.#.############
###.#.##############
###.#.##############
###...##############
####################'''
    window.addstr(5, 5, gameMap)
    cur_x = 2
    cur_y = 2
    stdscr.refresh()
    while True:
        window.addch(cur_y, cur_x  , '@')
        window.refresh()
        answer = stdscr.getkey()    #input a key
        if answer == 'KEY_UP':
            window.addch(cur_y, cur_x, '.')
            cur_y -= 1
        elif answer == 'KEY_DOWN':
            window.addch(cur_y, cur_x, '.')
            cur_y += 1
        elif answer == 'KEY_LEFT':
            window.addch(cur_y, cur_x, '.')
            cur_x -= 1
        elif answer == 'KEY_RIGHT':
            window.addch(cur_y, cur_x, '.')
            cur_x += 1
    
        

    

wrapper(main)