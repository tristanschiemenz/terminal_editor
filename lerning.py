"""
import curses
from curses import wrapper
import time

#addstr - postiony,postionx,text,attributes
#init_pair(farb sets) - channel,foreground color, backgroundcolor
#stdscr.addstr(10,10,"Hello, World!",curses.color_pair(1) | curses.A_UNDERLINE)

def main(stdscr):
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLUE)
    GREEN_AND_BLUE = curses.color_pair(1)
    
    for i in range(1000):
        color = GREEN_AND_BLUE
        stdscr.clear()
        if i %2 == 0:
            color = GREEN_AND_BLUE | curses.A_REVERSE
            
        stdscr.addstr(f"Count: {i}",color)
        time.sleep(.0000000000000001)
        stdscr.refresh()
    stdscr.getch()
    
wrapper(main)
"""

# Import the curses module and initialize it
import curses

# initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

# Set up the user interface and create the main window
stdscr.addstr(0, 0, "Welcome to my terminal-based editor!")
stdscr.addstr(1, 0, "Type ':q' to quit.")

# create the main window
editor_win = curses.newwin(curses.LINES - 2, curses.COLS, 2, 0)
editor_win.scrollok(True)

# Define the main loop for the editor
stdscr.addstr(10, 20, "Hallo mein Schatz",curses.A_UNDERLINE | curses.A_BOLD)
stdscr.addstr(15, 40, "Hallo mein Schatz",curses.A_UNDERLINE | curses.A_BOLD)
stdscr.getch()

# Clean up and exit the program
curses.nocbreak()
curses.echo()
curses.endwin()
