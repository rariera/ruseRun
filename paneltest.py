from curses import wrapper, panel
import curses

def main(stdscr):
    curses.initscr()
   
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

    
    
    
wrapper(main)